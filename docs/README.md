# 👓 Smart Glasses for Visually Impaired

An object detection-based smart glasses system that provides **audio feedback** using a **YOLOv8 model** and a **Raspberry Pi camera**, helping visually impaired users detect objects and their relative distances (e.g., *"person – very close"*).

---

## 🗂️ Project Structure
smart_glasses_project/ 
├── code/ # Main Python scripts 
│ ├── detection_yolo_audio.py 
│ ├── camera_setup.py 
│ └── utils.py 
├── models/ # YOLOv8 model weights 
│ └── yolov8n.pt 
├── hardware_integration/ # Wiring diagrams & Pi config 
│ ├── wiring_diagrams/ 
│ └── raspberry_pi_config/
├── docs/ # Documentation 
│ ├── README.md 
│ └── setup_guide.md 
└── tests/ # Test results 
    └── test_results.md

    
---

## Features

- Real-time object detection with YOLOv8
- Audio feedback for object and distance (e.g., *"chair – far"*)
- Raspberry Pi + camera-based live feed
- Modular folder structure for easy hardware/software separation

---

## Getting Started

### 1. Clone the Repo
```bash
git clone https://github.com/nm2813/smart_glasses_project.git
cd smart_glasses_project

### 2. Setup Python Environment
python -m venv venv
venv\Scripts\activate    # Windows
# OR
source venv/bin/activate # macOS/Linux

pip install -r requirements.txt

### Run Camera Test
python code/camera_setup.py

### Start Detection
python code/detection_yolo_audio.py
#You will see bounding boxes and hear audio feedback.

##Harrdware Setup
hardware_integration/
├── wiring_diagrams/
└── raspberry_pi_config/

##Contribution Guide
Pull latest code: git pull origin main
Add changes: git add .
Commit: git commit -m "Message"
Push: git push origin main
