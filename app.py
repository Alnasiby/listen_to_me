from flask import Flask, request, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

# Indian song suggestions with YouTube links
songs = {
    ("happy", "bollywood", "dance"): {
        "title": "Kala Chashma - Baar Baar Dekho",
        "link": "https://www.youtube.com/watch?v=k4yXQkG2s1E"
    },
    ("sad", "bollywood", "slow"): {
        "title": "Channa Mereya - Ae Dil Hai Mushkil",
        "link": "https://www.youtube.com/watch?v=284Ov7ysmfA"
    },
    ("romantic", "bollywood", "melody"): {
        "title": "Tum Mile - Tum Mile",
        "link": "https://www.youtube.com/watch?v=Z3kiDCQwBdU"
    },
    ("energetic", "punjabi", "party"): {
        "title": "Morni Banke - Badhaai Ho",
        "link": "https://www.youtube.com/watch?v=Q0BlC3hZLF8"
    },
    ("calm", "classical", "instrumental"): {
        "title": "Breathless - Shankar Mahadevan",
        "link": "https://www.youtube.com/watch?v=GfAuuU_yQZo"
    },
    # Add more entries as needed...
}

@app.route('/api/recommend', methods=['POST'])
def recommend():
    data = request.get_json()
    mood = data.get("mood", "").lower()
    genre = data.get("genre", "").lower()
    style = data.get("style", "").lower()

    key = (mood, genre, style)
    result = songs.get(key)

    if result:
        return jsonify({'title': result['title'], 'link': result['link']})
    else:
        return jsonify({'title': "😔 Sorry, no perfect match! Try another mood/genre/style.", 'link': None})

if __name__ == '__main__':
    app.run(debug=True)
