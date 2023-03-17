from flask import Flask, render_template, request, jsonify
import base64
import requests

app = Flask(__name__, static_url_path='/static')

dummy ={'data': 
        [
    {
    'gaze_percentage': 100.0, 
    'face_emotion':  {'disgust': 0.01222809309886645, 'fear': 32.72938005048605, 'surprise': 0.7012529174430417, 'neutral': 1.346287779555521, 'anger': 3.149491521476035, 'joy': 45.65146084172068, 'sadness': 16.409897820592235}, 
    'text_emotion': [{'label': 'anger', 'score': 0.023661362007260323}, {'label': 'disgust', 'score': 0.006093132775276899}, {'label': 'fear', 'score': 0.004496699199080467}, {'label': 'joy', 'score': 0.5762036442756653}, {'label': 'neutral', 'score': 0.2536909878253937}, {'label': 'sadness', 'score': 0.0070466771721839905}, {'label': 'surprise', 'score': 0.12880752980709076}], 
    'transcription': " Hey, just want to tell you you're doing good You're doing your absolute best you're trying your absolute hardest and that's what really matters Don't be so hard on yourself You're doing amazing and if nobody told you lately, I'm proud of you", 
    'text_sentiment': [{'label': 'POSITIVE', 'score': 0.9998641014099121}]}], 'is_generating': False, 'duration': 7.471308708190918, 'average_duration': 9.438956022262573}


@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        video = request.files['video'].read()
        data = getFocus(video)
        print(data)
        data = process_output(data)
        print("doing something with video")
        # print(output['duration'])
        data = data['data'][0]
        gaze_percentage = data['gaze_percentage']
        face_emotion = data['face_emotion']
        text_emotion = data['text_emotion']
        transcription = data['transcription']
        text_sentiment = data['text_sentiment']
        duration = dummy['duration']
        return render_template('index.html', gaze_percentage = gaze_percentage, face_emotion= face_emotion, text_emotion = text_emotion, 
                               text_sentiment = text_sentiment, transcription = transcription, duration = duration, show=True)
    else:
        return render_template('index.html', show=False)
    
def process_output(data):
    # Update the face_emotion data
    for item in data['data']:
        emotions = item['face_emotion']
        top_emotions = dict(sorted(emotions.items(), key=lambda x: x[1], reverse=True)[:3])
        item['face_emotion'] = top_emotions

    # Update the text_emotion data
    for item in data['data']:
        emotions = item['text_emotion']
        top_emotions = sorted(emotions, key=lambda x: x['score'], reverse=True)[:3]
        item['text_emotion'] = top_emotions
    return data

def getFocus(video):
    print("Getting Results...")

    file_data_base64 = base64.b64encode(video).decode('utf-8')

    response = requests.post(
        "https://abrar-adnan-speech-analyzer.hf.space/run/predict", 
        json={
                "data": [
                    {"name": "video.mp4", "data": file_data_base64},
                    file_data_base64
                    ]}
    ).json()
    print("done")
    # print(response.status_code)
    # print(response.content)
    # print(response.json())
    return response

if __name__ == '__main__':
    app.run(debug=True)