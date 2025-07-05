from Amazon_Data import reviews_summary as rs
# B00C6CCD8C is Amazon Standard Identification Number for 'RazoRock Alum Stick - 60 g - After Shave Stick'
# Select Random Reviews within Token Limit to Reduce API Costs
AI_summary=rs(asin='B00C6CCD8C',TARGET_TOKEN_LIMIT=500)
print(AI_summary)