from textblob import TextBlob

def detect_mood(text):
    analysis = TextBlob(text)
    sentiment_score = analysis.sentiment.polarity  # Score between -1 (negative) to +1 (positive)
    
    if sentiment_score > 0.3:
        return "happy"
    elif sentiment_score < -0.3:
        return "sad"
    else:
        return "neutral"

# Test the function
if __name__ == "__main__":
    user_input = input("How are you feeling? ")
    mood = detect_mood(user_input)
    print(f"Detected Mood: {mood}")
