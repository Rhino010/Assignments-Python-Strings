# Task 3: Review Summary

# Implement a script that takes the first 30 characters of a 
# review and appends "…" to create a summary. Ensure that the 
# summary does not cut off in the middle of a word.

# Example: "This product is really good. I'm...",


reviews = [
    "This product is really good. I'm impressed with its quality.",
    "The performance of this product is excellent. Highly recommended!",
    "I had a bad experience with this product. It didn't meet my expectations.",
    "Poor quality product. Wouldn't recommend it to anyone.",
    "The product was average. Nothing extraordinary about it."
]

summary = []
summary_list = []

char_count = 0
count = 0

while count < len(reviews):
    for i in reviews:
        count += 1
        x = i.split()
        for y in x:
            if char_count <= 30:
                summary.append(y)
                char_count=char_count + len(y) + 1
            else:
                summary_list.append(' '.join(summary)+'...')
                summary.clear()
                char_count = 0
                break

for i in summary_list:
    print(i)
    

    

          

