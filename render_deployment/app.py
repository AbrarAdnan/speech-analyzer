from flask import Flask, render_template, request
import base64
import requests

app = Flask(__name__, static_url_path='/static')

dummy = {
  "gaze_percentage": 100,
  "face_emotion": {
    "angry": 1.5938487265966819,
    "disgust": 0.01240325793125735,
    "fear": 47.68757721435881,
    "happy": 45.6566903932219,
    "sad": 3.1918139858520127,
    "surprise": 0.7046129829605734,
    "neutral": 1.1530537686272717
  },
  "text_emotion": [
    {
      "label": "anger",
      "score": 0.02366134524345398
    },
    {
      "label": "disgust",
      "score": 0.006093125324696302
    },
    {
      "label": "fear",
      "score": 0.004496702458709478
    },
    {
      "label": "joy",
      "score": 0.5762037634849548
    },
    {
      "label": "neutral",
      "score": 0.2536906599998474
    },
    {
      "label": "sadness",
      "score": 0.007046668324619532
    },
    {
      "label": "surprise",
      "score": 0.12880778312683105
    }
  ],
  "transcription": " Hey, just want to tell you you're doing good You're doing your absolute best you're trying your absolute hardest and that's what really matters Don't be so hard on yourself You're doing amazing and if nobody told you lately, I'm proud of you",
  "text_sentiment": [
    {
      "label": "POSITIVE",
      "score": 0.9998641014099121
    }
  ]
}


@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        video = request.files['video'].read()
        output = getFocus(video)
        print(output)
        return render_template('index.html', result=output["data"], duration = output["duration"],  show=True)
    else:
        return render_template('index.html', show=False)

def getFocus(video):
    print("Getting Results...")

    file_data_base64 = base64.b64encode(video).decode('utf-8')

    response = requests.post(
        "https://abrar-adnan-speech-analyzer.hf.space/run/predict", 
        json={
                "data": [
                    {"name": "video.mp4", "data": ""},
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