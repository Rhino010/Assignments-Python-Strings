# Remember to take your time and work through each question diligently! 
# Test your code, make sure it works, and try to find ways to improve. 
# Once you are happy and satisfied with your code, upload it to Github, 
# then turn in your Github link at the bottom of the page!


# Don't forget. Make sure this assignment is in it's own repository. Not mixed in with others!

# 1. Product Review Analysis
# Task 1: Keyword Highlighter

# Write a program that searches through reviews list and looks for 
# keywords such as "good", "excellent", "bad", "poor", and "average". 
# We want you to capitalize those keywords then print out each review. 
# Print out each review with the keywords in uppercase so they stand out.

# So for the first string in the reviews list, we want it to say: 
# "This product is really GOOD. I'm impressed with its quality."

# 1. Iterate over the keyword search list
# 2. Write a conditional to verify if 

reviews = [
    "This product is really good. I'm impressed with its quality.",
    "The performance of this product is excellent. Highly recommended!",
    "I had a bad experience with this product. It didn't meet my expectations.",
    "Poor quality product. Wouldn't recommend it to anyone.",
    "The product was average. Nothing extraordinary about it."
]

search_list = ['good', 'bad', 'poor', 'excellent', 'average']


new_list = []
for review in reviews:
    for keyword in search_list:
        if keyword in review:
            capital_keyword = review.replace(keyword, keyword.upper())
            new_list.append(capital_keyword)
print(new_list)

    
        

