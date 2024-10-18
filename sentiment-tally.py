# Develop a function that tallies the number of positive and 
# negative words in each review.  The function should return the total count of positive and negative words.

reviews = [
    "This product is really good. I'm impressed with its quality.",
    "The performance of this product is excellent. Highly recommended!",
    "I had a bad experience with this product. It didn't meet my expectations.",
    "Poor quality product. Wouldn't recommend it to anyone.",
    "The product was average. Nothing extraordinary about it."
]


positive_words = ["good", "excellent", "great", "awesome", "fantastic", "superb", "amazing",]
negative_words = ["bad", "poor", "terrible", "horrible", "awful", "disappointing", "subpar"]


def sentiment_counter(pos, neg):
    global reviews
    pos_count = 0
    neg_count = 0
    for i in reviews:
        x = [p for p in positive_words if p in i.lower()]
        y = [n for n in negative_words if n in i.lower()]
        if x:
            pos_count +=1
        
        elif y:
            neg_count += 1
    print(f"The total number of positive words is {pos_count} and total negative words are {neg_count}")

sentiment_counter(positive_words, negative_words)
    

