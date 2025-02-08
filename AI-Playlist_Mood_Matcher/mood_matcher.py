from textblob import TextBlob
import spotipy
from spotipy.oauth2 import SpotifyClientCredentials

# Spotify API Setup
client_id = "bc10bd47f5e44b72900a3f834d08822f"
client_secret = "a20e559a8493477dad45aa71b9493013"

sp = spotipy.Spotify(auth_manager=SpotifyClientCredentials(client_id, client_secret))

# Playlist mapping (Replace with real Spotify playlist URLs)
mood_playlists = {
    "happy": "https://open.spotify.com/playlist/4LB8WA44HMGXVh8nXP81pO?si=b3ea661290e046fb",
    "sad": "https://open.spotify.com/playlist/7vtJTPVqaviCokFLKpBpMW?si=a3422f9394954907",
    "neutral": "https://open.spotify.com/playlist/2GYHBifOLwNeRydd4jHTXk?si=c657c8b821344c77"
}

# Mood detection function
def detect_mood(text):
    analysis = TextBlob(text)
    sentiment_score = analysis.sentiment.polarity  
    
    if sentiment_score > 0.3:
        return "happy"
    elif sentiment_score < -0.3:
        return "sad"
    else:
        return "neutral"

# Main program
if __name__ == "__main__":
    user_input = input("How are you feeling today? ")
    mood = detect_mood(user_input)
    playlist = mood_playlists.get(mood, "No playlist found")

    print(f"Detected Mood: {mood}")
    print(f"Suggested Playlist: {playlist}")
