from flask import Flask, request, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

# Indian song suggestions
songs = {
    ("happy", "bollywood", "dance"): "Kala Chashma - Baar Baar Dekho",
    ("sad", "bollywood", "slow"): "Channa Mereya - Ae Dil Hai Mushkil",
    ("romantic", "bollywood", "melody"): "Tum Mile - Tum Mile",
    ("energetic", "punjabi", "party"): "Morni Banke - Badhaai Ho",
    ("calm", "classical", "instrumental"): "Breathless - Shankar Mahadevan",
    ("devotional", "hindi", "bhajan"): "Achyutam Keshavam - Krishna Bhajan",
    ("heartbroken", "bollywood", "emotional"): "Tujhe Bhula Diya - Anjaana Anjaani",
    ("motivated", "hindi", "inspirational"): "Zinda - Bhaag Milkha Bhaag",
    ("love", "tamil", "melody"): "Munbe Vaa - Sillunu Oru Kaadhal",
    ("nostalgic", "malayalam", "classic"): "Ponveene - Namukku Parkkan Munthiri Thoppukal",
}

@app.route('/api/recommend', methods=['POST'])
def recommend():
    data = request.get_json()
    mood = data.get("mood", "").lower()
    genre = data.get("genre", "").lower()
    style = data.get("style", "").lower()

    key = (mood, genre, style)
    song = songs.get(key, "😔 Sorry, no perfect match! Try another mood/genre/style.")

    return jsonify({'reply': song})

if __name__ == '__main__':
    app.run(debug=True)
