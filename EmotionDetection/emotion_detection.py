import requests
import json

def emotion_detector(text_to_analyze):
    if not text_to_analyze.strip():
        return {
            'anger': None,
            'disgust': None,
            'fear': None,
            'joy': None,
            'sadness': None,
            'dominant_emotion': None
        }
    
    url = 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'
    myobj = { "raw_document": { "text": text_to_analyze } }
    header = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}
    response = requests.post(url, json=myobj, headers=header)
    
    if response.status_code == 400:
        return {
            'anger': None,
            'disgust': None,
            'fear': None,
            'joy': None,
            'sadness': None,
            'dominant_emotion': None
        }
    
    try:
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

# Test the function
if __name__ == "__main__":
    text = "I am so happy I am doing this."
    result = emotion_detector(text)
    print(result)
