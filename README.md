# amazon-review-ai-summarizer
![image](https://github.com/user-attachments/assets/ebae7af4-80e1-4e66-8744-ef8c61ab82a9)

This project is developed by DrSavalan (mechsavalan@gmail.com).

## Description:

`amazon-review-ai-summarizer` is a Python project designed to provide concise **AI-powered summaries** of Amazon product reviews. It leverages the OpenAI API to analyze customer feedback, specifically identifying the **top 3 most prominent positive aspects and the top 3 most prominent negative aspects or common complaints**.

This tool is particularly useful for quickly grasping the general sentiment around a product without having to manually sift through hundreds or thousands of reviews. It efficiently processes a curated selection of verified reviews, optimizing for API cost by limiting the number of tokens sent to the OpenAI model.

## Features:

* **AI-Powered Summarization**: Utilizes OpenAI's language models to identify the **top 3 positive and top 3 negative themes** in customer reviews.

* **Cost-Effective**: Intelligently selects a subset of reviews within a defined token limit to minimize API usage costs.

* **Verified Review Focus**: Prioritizes analysis of verified purchases to ensure data reliability.

* **Clear Output**: Presents findings in an easy-to-read format, specifically highlighting the **top 3 positive and top 3 negative aspects**.

## How it Works:

1. **Data Loading**: Reads customer review data from a JSON file.

2. **Data Cleaning**: Pre-processes review text to remove irrelevant characters and standardize formatting.

3. **Tokenization**: Calculates token counts for each review to manage API costs.

4. **Smart Review Selection**: Randomly selects reviews within a specified token limit to create a concise input for the AI.

5. **AI Analysis**: Sends the selected reviews to the OpenAI API for summarization, with the prompt specifically guiding the AI to extract the **top 3 positive and top 3 negative aspects**.
   * **Note on API Connection**: Due to regional limitations in Iran, this project uses AvalAI as an intermediary for OpenAI API access. Users outside of Iran can typically connect directly to the OpenAI API without this intermediary.

6. **Output**: Returns a summary detailing the **top 3 positive and top 3 negative aspects**, along with the total number of reviews considered for the summary.

## Required Packages:

To run this project, you need to install the following Python packages. You can install them using pip:

```bash
pip install openai python-dotenv pandas tiktoken
```

## Data Requirement:

To run this project, you will need a dataset of Amazon product reviews. You can download the `All_Beauty.json` file (or similar product categories) from the following link:

https://amazon-reviews-2023.github.io/

Please place the downloaded JSON file in the same directory as your Python scripts.

## Example Output:

Here's an example of an AI-generated summary for the 'RazoRock Alum Stick - 60 g - After Shave Stick':

```
AI Reviews Summary Based on 325 Reviews:

**Analysis** Based on the customer reviews provided, I have identified the top three most prominent positive and negative aspects based on repetition and emphasis from the feedback.  

**Positive Aspects (Top 3, each up to 5 words!):** 1. Effective for small nicks/cuts  
2. Reduces razor burn and irritation  
3. Convenient and compact design  

**Negative Aspects (Top 3, each up to 5 words!):** 1. Stings or burns upon application  
2. Poor/different packaging in some cases  
3. Size smaller than expected  

These findings adhere to the frequency and tone of the feedback provided, without conflicting observations across positive and negative sentiments for the product.

```

## Ideal For:

* Product researchers

* E-commerce businesses

* Anyone seeking quick insights into product sentiment from Amazon reviews.
