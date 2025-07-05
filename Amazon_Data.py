import pandas as pd
import re
import tiktoken # Make sure you have this installed: pip install tiktoken
from AI_Hint import _perform_analysis_task as pt

def reviews_summary(asin='B00C6CCD8C',TARGET_TOKEN_LIMIT=500):
    # --- Load and Prepare DataFrame (as per your existing code) ---
    df = pd.read_json('All_Beauty.json', lines=True)

    df_rec = df[['verified','reviewerID', 'asin', 'overall','summary']].dropna()
    df_rec.columns = ['verified','user_id', 'item_id', 'rating','review'] # Rename the columns for clarity
    df_rec_verified = df_rec[df_rec['verified'] == True] # Only using the verified user reviews

    # B00C6CCD8C is Amazon Standard Identification Number for 'RazoRock Alum Stick - 60 g - After Shave Stick'
    df_target = df_rec_verified[df_rec_verified['item_id'] == asin].copy() # Solved SettingWithCopyWarning


    #print(f"Number of verified reviews for the target item: {len(df_target)}")

    # --- Cleaning Function (from previous turn) ---
    def clean_text_for_openai(text):
        if isinstance(text, bytes):
            try:
                text = text.decode('utf-8', errors='ignore')
            except UnicodeDecodeError:
                text = text.decode('latin-1', errors='ignore')
            except Exception as e:
                return ""
        elif not isinstance(text, str):
            text = str(text)

        cleaned_text = re.sub(r'[^\x20-\x7E\n\r\t]', '', text)
        cleaned_text = re.sub(r'\s+', ' ', cleaned_text).strip()
        return cleaned_text

    # Apply cleaning and get cleaned reviews
    df_target['review_cleaned'] = df_target['review'].apply(clean_text_for_openai)

    # --- Tiktoken Setup and Token Counting Function ---
    encoding = tiktoken.encoding_for_model("gpt-4o") # Or "gpt-3.5-turbo"

    def get_token_count(text_input):
        return len(encoding.encode(text_input))

    # Add a token count column to your DataFrame for individual reviews
    df_target['review_tokens'] = df_target['review_cleaned'].apply(get_token_count)

    # --- Select Random Reviews within Token Limit to Reduce API Costs ---

    selected_reviews = []
    current_token_sum = 0
    num_reviews_selected = 0

    # Shuffle the DataFrame to pick reviews randomly
    shuffled_reviews_df = df_target.sample(frac=1, random_state=42).reset_index(drop=True) # frac=1 shuffles all rows

    # Iterate through the shuffled reviews
    for index, row in shuffled_reviews_df.iterrows():
        review_text = row['review_cleaned']
        review_tokens = row['review_tokens']

        # We add 1 token for the newline character that will separate reviews
        # when we concatenate them later, to be more accurate.
        tokens_with_separator = review_tokens + 1

        if current_token_sum + tokens_with_separator <= TARGET_TOKEN_LIMIT:
            selected_reviews.append(review_text)
            current_token_sum += tokens_with_separator
            num_reviews_selected += 1
        else:
            # If adding this review exceeds the limit, stop
            break

    # Concatenate the selected reviews into a single string for the prompt
    random_reviews_for_prompt = "\n".join(selected_reviews)

    # Verify the final token count
    final_token_count = get_token_count(random_reviews_for_prompt)
    #print("\n--- Random Review selecting; to reduce the tokens sent and reduce the costs ---")
    #print(f"--- Random Review Selection Results ---")
    #print(f"Number of reviews selected: {num_reviews_selected}")
    #print(f"Total tokens in selected reviews (including separators): {final_token_count}")
    #print(f"Is total tokens less than or equal to {TARGET_TOKEN_LIMIT}? {final_token_count <= TARGET_TOKEN_LIMIT}")



    hint=pt(random_reviews_for_prompt,len(df_target))
    #print('\nAI Summary for Positive and Negative Aspects')
    #print(hint)
    return hint