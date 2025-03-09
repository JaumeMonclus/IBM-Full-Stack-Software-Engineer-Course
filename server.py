"""
Flask API for Emotion Detection
"""

from flask import Flask, request, jsonify
from EmotionDetection import emotion_detector

app = Flask(__name__)

@app.route('/emotionDetector', methods=['POST'])
def analyze_emotion():
    """
    API endpoint to analyze emotion from user input.
    Returns a JSON response with detected emotions.
    """
    data = request.get_json()

    if not data or 'text' not in data:
        return jsonify({"message": "Invalid Input. Please provide a JSON with a 'text' field."}), 400

    text_to_analyze = data['text']
    result = emotion_detector(text_to_analyze)

    if result['dominant_emotion'] is None:
        return jsonify({"message": "Invalid text! Please try again!"}), 400

    response_text = (
        f"For the given statement, the system response is 'anger': {result['anger']}, "
        f"'disgust': {result['disgust']}, 'fear': {result['fear']}, 'joy': {result['joy']} "
        f"and 'sadness': {result['sadness']}. The dominant emotion is {result['dominant_emotion']}."
    )

    return jsonify({"response": response_text}), 200

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
