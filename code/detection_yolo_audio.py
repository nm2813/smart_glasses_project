import cv2
import pyttsx3
from ultralytics import YOLO
from utils import get_distance, cleanup_gpio

# Initialize TTS engine
engine = pyttsx3.init()
engine.setProperty('rate', 150)  # Speech speed

# Speak text
def speak(text):
    engine.say(text)
    engine.runAndWait()

# Estimate distance based on box size (simplified)
def estimate_distance(bbox, frame_width):
    x1, y1, x2, y2 = bbox
    box_width = x2 - x1
    rel_size = box_width / frame_width

    if rel_size > 0.5:
        return "very close"
    elif rel_size > 0.3:
        return "close"
    else:
        return "far"

def main():
    model = YOLO('yolov8n.pt')
    cap = cv2.VideoCapture(0)

    if not cap.isOpened():
        print("Error: Could not open webcam.")
        return

    last_spoken = ""

    try:
        while True:
            ret, frame = cap.read()
            if not ret:
                break

            results = model(frame, verbose=False)[0]
            annotated_frame = results.plot()
            frame_width = frame.shape[1]

            if results.boxes:
                for box in results.boxes:
                    cls_id = int(box.cls[0])
                    class_name = results.names[cls_id]
                    x1, y1, x2, y2 = map(int, box.xyxy[0])
                    distance = estimate_distance((x1, y1, x2, y2), frame_width)
                    dist_feedback = get_distance()

                    # Say object + distance estimate + actual ultrasonic distance
                    description = f"{class_name} {distance}, {dist_feedback} cm"

                    if description != last_spoken:
                        speak(description)
                        last_spoken = description
                        break

            cv2.imshow("YOLOv8 Detection", annotated_frame)

            key = cv2.waitKey(1)
            if key == ord('q') or key == 27:
                break
    finally:
        cap.release()
        cv2.destroyAllWindows()
        cleanup_gpio()

if __name__ == '__main__':
    main()