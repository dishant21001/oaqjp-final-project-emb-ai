<<<<<<< HEAD
from setuptools import setup, find_packages

setup(
    name='EmotionDetection',
    version='0.1',
    packages=find_packages(),
    install_requires=[
        'requests',
    ],
)
=======
import requests
import json

def emotion_detector(text_to_analyze):
    url = 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'
    myobj = { "raw_document": { "text": text_to_analyze } }
    header = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}
    response = requests.post(url, json=myobj, headers=header)
    
    try:
        # Print the raw response for debugging
        print("Raw response:", response.text)
        
        formatted_response = json.loads(response.text)
        
        if 'documentEmotion' not in formatted_response:
            raise KeyError("Key 'documentEmotion' not found in the response")
        
        emotions = formatted_response['documentEmotion']['emotionScores']
        scores = {emotion: emotions.get(emotion, 0) for emotion in ['anger', 'disgust', 'fear', 'joy', 'sadness']}
        dominant_emotion = max(scores, key=scores.get)
        
        return {
            'anger': scores['anger'],
            'disgust': scores['disgust'],
            'fear': scores['fear'],
            'joy': scores['joy'],
            'sadness': scores['sadness'],
            'dominant_emotion': dominant_emotion
        }
    
    except json.JSONDecodeError:
        return {"error": "Failed to parse JSON response"}
    except KeyError as e:
        return {"error": str(e)}
    except Exception as e:
        return {"error": f"An unexpected error occurred: {str(e)}"}


>>>>>>> e522eea349ff4c688a5b30cf1aaf80672e5cf648
