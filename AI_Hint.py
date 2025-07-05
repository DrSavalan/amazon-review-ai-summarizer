from openai import OpenAI
import os
from dotenv import load_dotenv

load_dotenv()  # Load environment variables from .env file; for your safety!
# --- Configuration ---
api_key = os.getenv("API_KEY")
# --- OpenAI Configuration (from your provided code) ---
client = OpenAI(
    api_key=api_key,  # Replace with your actual AvalAI API key
    base_url="https://api.avalai.ir/v1",
    # Base URL for AvalAI; This line is for Iranian who are under regional limitations; Remove it if you are not in Iran.
)




def _perform_analysis_task(random_reviews_for_prompt,reviews_number):
    prompt_text = f"""
                    I have a collection of customer reviews for a beauty product. 
                    Please read through them and identify the top 3 most prominent positive aspects and the 
                    top 3 most prominent negative aspects or common complaints.
                
                    Present your findings clearly.
                    
                    --- Customer Reviews ---
                    {random_reviews_for_prompt}
                    
                    --- Analysis ---
                    **Positive Aspects (Top 3, each up to 5 words!):**
                    *
                    *
                    *
                    **Negative Aspects (Top 3, each up to 5 words!):**
                    *
                    *
                    *
                    
                    Be careful that the positive and negative aspects do not contradict each other; If there is a discrepancy, look at the number of reviews to vote fairly!
                """
    response = client.chat.completions.create(
        model="gpt-4o",  # Or another vision-capable model
        messages=[
            {
                "role": "user",
                "content": [
                    {"type": "text",
                     "text": prompt_text},
                ],
            }
        ],
    )

    # 5. Display the trading hint
    hint = response.choices[0].message.content
    hint='AI Reviews Summary Based on '+str(reviews_number)+ ' Reviews:\n\n' +hint
    return hint
