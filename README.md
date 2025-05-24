# YOLOv8 Real-Time Video Object Detection with Flask

This project is a simple web application built with Flask that allows users to upload a video file and performs real-time object detection on the uploaded video using the YOLOv8 model from the Ultralytics library. The app streams the processed video with detection annotations directly on the webpage.

## Features

- Upload videos via a web interface
- Real-time object detection using YOLOv8 (YOLOv8n pre-trained model)
- Stream annotated video frames in the browser
- Simple and clean UI for uploading and viewing detection results

## Requirements

- Python 3.8+
- Flask
- OpenCV (`opencv-python`)
- Ultralytics YOLO package (`ultralytics`)

## Installation

1. Clone the repository:

   ```bash
   git clone https://github.com/Bilal-73/yolov8-flask-video-detection.git
   cd yolov8-flask-video-detection
## Project Structure

app.py: Main Flask application containing routes and video processing logic.
templates/index.html: HTML template for the upload page and video display.
uploads/: Directory where uploaded videos are stored (created automatically).

##Notes

The video streaming uses MJPEG format with multipart response to stream frames.
The model yolov8n.pt is lightweight and good for real-time demos; you can switch to larger models if needed.
Ensure your system has the necessary codecs to handle video files.
