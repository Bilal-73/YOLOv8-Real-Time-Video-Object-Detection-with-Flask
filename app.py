import os
from flask import Flask, render_template, request, redirect, url_for, Response
from ultralytics import YOLO
import cv2

app = Flask(__name__)
UPLOAD_FOLDER = 'uploads'
os.makedirs(UPLOAD_FOLDER, exist_ok=True)
model = YOLO("yolov8n.pt")

video_path = None  # Global variable to store video path

@app.route('/', methods=['GET', 'POST'])
def index():
    global video_path
    if request.method == 'POST':
        file = request.files['video']
        if file:
            video_path = os.path.join(UPLOAD_FOLDER, file.filename)
            file.save(video_path)
            return redirect(url_for('video'))
    return render_template('index.html')

def generate_frames():
    global video_path
    cap = cv2.VideoCapture(video_path)
    while cap.isOpened():
        success, frame = cap.read()
        if not success:
            break
        results = model(frame)[0]
        annotated = results.plot()

        ret, buffer = cv2.imencode('.jpg', annotated)
        frame = buffer.tobytes()

        yield (b'--frame\r\n'
               b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n')

    cap.release()

@app.route('/video')
def video():
    return Response(generate_frames(), mimetype='multipart/x-mixed-replace; boundary=frame')

if __name__ == '__main__':
    app.run(debug=True)
