import cv2
import pyttsx3
import threading
from ultralytics import YOLO
from utils import get_distance, cleanup_gpio

# Text-to-speech init
engine = pyttsx3.init()
engine.setProperty('rate', 150)

def speak_async(text):
    def run():
        engine.say(text)
        engine.runAndWait()
    threading.Thread(target=run, daemon=True).start()

def estimate_distance(bbox, frame_width):
    x1, _, x2, _ = bbox
    box_width = x2 - x1
    rel_size = box_width / frame_width
    if rel_size > 0.5:
        return "very close"
    elif rel_size > 0.3:
        return "close"
    else:
        return "far"

def main():
    pretrained_model = YOLO('yolov8n.pt')
    custom_model = YOLO('best.pt')

    cap = cv2.VideoCapture(0)
    if not cap.isOpened():
        print("Failed to open camera.")
        return

    cv2.namedWindow("Camera", cv2.WINDOW_NORMAL)
    frame_count = 0

    last_seen = {}  # {class_name: last_distance_category}

    try:
        while True:
            ret, frame = cap.read()
            if not ret:
                break

            frame_width = frame.shape[1]
            model = pretrained_model if frame_count % 2 == 0 else custom_model
            results = model(frame, verbose=False)[0]

            if results.boxes:
                for box in results.boxes:
                    cls_id = int(box.cls[0])
                    class_name = results.names[cls_id]
                    x1, y1, x2, y2 = map(int, box.xyxy[0])
                    distance_category = estimate_distance((x1, y1, x2, y2), frame_width)
                    real_distance = get_distance()
                    desc = f"{class_name}, {distance_category}, {real_distance} cm"

                    # Speak only if distance category has changed for same object
                    if last_seen.get(class_name) != distance_category:
                        speak_async(desc)
                        last_seen[class_name] = distance_category

                    # Draw
                    cv2.rectangle(frame, (x1, y1), (x2, y2), (0,255,0), 2)
                    cv2.putText(frame, desc, (x1, y1-10), cv2.FONT_HERSHEY_SIMPLEX, 0.6, (255,255,255), 2)
                    
            frame_count += 1
            cv2.imshow("Camera", frame)

            key = cv2.waitKey(1) & 0xFF
            if key in [ord('q'), 27]:
                print("Exiting...")
                break

    finally:
        cap.release()
        cleanup_gpio()
        cv2.destroyAllWindows()

if __name__ == "__main__":
    main()
