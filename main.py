
positive_words = [
    "good", "great", "happy", "joy", "awesome", "excellent", "fortunate", "fantastic", "love", "like"
]
negative_words = [
    "bad", "terrible", "sad", "hate", "awful", "poor", "worst", "angry", "dislike", "unfortunate"
]
def preprocess(text):
    import re
    text = text.lower()                      
    text = re.sub(r'[^\w\s]', '', text)       
    tokens = text.split()                    
    return tokens


def analyze_sentiment(text):
    tokens = preprocess(text)
    pos_count = sum(1 for word in tokens if word in positive_words)
    neg_count = sum(1 for word in tokens if word in negative_words)

    if pos_count > neg_count:
        sentiment = "Positive"
    elif neg_count > pos_count:
        sentiment = "Negative"
    else:
        sentiment = "Neutral"

    return {
        "positive_words": pos_count,
        "negative_words": neg_count,
        "sentiment": sentiment
    }


if __name__ == "__main__":
    sample_text = input("Enter a sentence: ")
    result = analyze_sentiment(sample_text)
    print("Sentiment:", result["sentiment"])
    print("Positive words:", result["positive_words"])
    print("Negative words:", result["negative_words"])