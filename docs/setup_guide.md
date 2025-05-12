# Smart Glasses Project Setup Guide 

This guide will help you set up the Smart Glasses Project on your local machine. The project involves integrating object detection using YOLOv8 and providing audio feedback to visually impaired individuals.

## Prerequisites
Before you start, ensure you have the following:

1. Python 3.7+ (Recommended version: 3.8 or higher)

2. Git (for version control)

## Virtual Environment (Optional but recommended)

### Step 1: Clone the Repository
First, clone the project repository to your local machine:

git clone https://github.com/nm2813/smart_glasses_project.git
cd smart_glasses_project
 
### Step 2: Set Up a Virtual Environment
It is recommended to use a virtual environment to avoid dependency conflicts. Follow these steps to create and activate the environment:

#### Windows:
1. Create the virtual environment:
python -m venv venv

2. Activate the virtual environment:
venv\Scripts\activate

#### macOS/Linux:
1. Create the virtual environment:
python3 -m venv venv

2. Activate the virtual environment:
source venv/bin/activate

### Step 3: Install Dependencies
Once the virtual environment is activated, install the necessary dependencies:

manually install the dependencies:
pip install ultralytics opencv-python pyttsx3 numpy

### Step 4: Set Up Camera
Ensure you have the Raspberry Pi Camera Module properly connected and configured. If you're using a USB webcam or an external camera, ensure it's working with OpenCV.

#### For Raspberry Pi:
1. Enable the camera interface:
Open the Raspberry Pi configuration tool:
sudo raspi-config

Select Interfacing Options > Camera, then enable the camera.

2. Reboot the Raspberry Pi:
sudo reboot

### Step 5: Download the YOLOv8 Model
The project uses YOLOv8 for object detection. Download the YOLOv8 model file from the following location:

#### YOLOv8 Pretrained Model

Once downloaded, place the yolov8n.pt model file into the models folder of the project.

### Step 6: Running the Code
Run Object Detection with Audio Feedback
You can run the object detection with audio feedback using the following command:
python code/detection_yolo_audio.py

This script will:
Capture frames from the camera.
Run object detection using YOLOv8.
Provide audio feedback based on detected objects and their distance.

Run Camera Setup (If needed)
If you need to test or configure the camera setup, you can run:
python code/camera_setup.py

### Step 7: Additional Configuration
If needed, you can configure the project further by modifying the following files:
code/utils.py: For additional utility functions like image processing.
audio_feedback/sounds/: To customize audio feedback files.

### Step 8: Testing
After everything is set up, you can run tests by using the following command:
python -m unittest discover tests/
This will run any unit tests present in the tests folder.

## Troubleshooting
If you encounter any issues, check the camera connection and permissions.
Make sure all dependencies are installed by running pip install -r requirements.txt.

## Conclusion
You should now have the Smart Glasses Project set up and running locally. Feel free to reach out for any assistance or clarification.

