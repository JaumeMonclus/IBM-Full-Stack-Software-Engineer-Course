import requests
import json

# Watson NLP API URL & Headers
URL = "https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict"
HEADERS = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}

def emotion_detector(text_to_analyze):
    """Function to analyze emotion in a given text using Watson NLP API."""
    # Define the input JSON payload
    input_json = {"raw_document": {"text": text_to_analyze}}
    if not text_to_analyze:
        return{
            'anger': None,
            'disgust': None,
            'fear': None,
            'joy': None,
            'sadness': None,
            "dominant_emotion": None
        }
    try:
        # Make a POST request to the Watson NLP API
        response = requests.post(URL, headers=HEADERS, json=input_json)
        
        if respnse.status_code == 400:
            return{
                'anger': None,
                'disgust': None,
                'fear': None,
                'joy': None,
                'sadness': None,
                "dominant_emotion": None
            }
        
        response.raise_for_status()  # Raise an error for bad status codes
        
        
        data = response.json()

        # Extract emotions from response
        emotions = data["emotionPredictions"][0]["emotion"]

        # Store the emotions in a dictionary
        emotion_scores = {
            "anger": emotions.get("anger", 0),
            "disgust": emotions.get("disgust", 0),
            "fear": emotions.get("fear", 0),
            "joy": emotions.get("joy", 0),
            "sadness": emotions.get("sadness", 0)
        }

        # Find the dominant emotion (emotion with the highest score)
        dominant_emotion = max(emotion_scores, key=emotion_scores.get)

        # Return formatted results
        return {
            "anger": emotion_scores["anger"],
            "disgust": emotion_scores["disgust"],
            "fear": emotion_scores["fear"],
            "joy": emotion_scores["joy"],
            "sadness": emotion_scores["sadness"],
            "dominant_emotion": dominant_emotion
        }

    except requests.exceptions.RequestException as e:
        return {"error": str(e)}
