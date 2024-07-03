"""
This module provides a Flask web application for emotion detection.

The application includes the following endpoints:
- '/' : Renders the home page with the input form.
- '/emotionDetector' : Handles GET requests for emotion detection and returns
  the result in JSON format.
"""

from flask import Flask, request, jsonify, render_template
from EmotionDetection import emotion_detector

app = Flask(__name__)

@app.route('/')
def home():
    """
    Render the home page with the input form.
    """
    return render_template('index.html')

@app.route('/emotionDetector', methods=['GET'])
def emotion_detection():
    """
    Handle the GET request for emotion detection.

    Returns:
        JSON: Formatted result or error message.
    """
    text_to_analyze = request.args.get('textToAnalyze', '')
    result = emotion_detector(text_to_analyze)
    if result['dominant_emotion'] is None:
        return jsonify({'response': "Invalid text! Please try again."})

    formatted_result = (
        f"For the given statement, the system response is 'anger': {result['anger']}, "
        f"'disgust': {result['disgust']}, 'fear': {result['fear']}, 'joy': {result['joy']} "
        f"and 'sadness': {result['sadness']}. The dominant emotion is {result['dominant_emotion']}."
    )
    return jsonify({'response': formatted_result})

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)
