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
    print("Initializing YOLO model...")
    model = YOLO('yolov8n.pt')
    
    # Use CSI camera via V4L2 driver
    cap = cv2.VideoCapture(0, cv2.CAP_V4L2)

    if not cap.isOpened():
        print("Failed to open camera.")
        return
    else:
        print("Camera initialized successfully.")

    cv2.namedWindow("Laptop Camera Feed", cv2.WINDOW_NORMAL)

    frame_count = 0
    last_seen = {}
    

    try:
        while True:
            ret, frame = cap.read()
            if not ret:
                print("Failed to read frame from camera.")
                break

            frame_width = frame.shape[1]
            print("Processing frame...")
            results = model(frame, verbose=False)[0]

            if results.boxes:
                print(f"Detected {len(results.boxes)} objects.")
                for box in results.boxes:
                    cls_id = int(box.cls[0])
                    class_name = results.names[cls_id]
                    x1, y1, x2, y2 = map(int, box.xyxy[0])
                    distance_category = estimate_distance((x1, y1, x2, y2), frame_width)
                    real_distance = get_distance()
                    desc = f"{class_name}, {distance_category}, {real_distance} cm"

                    if last_seen.get(class_name) != distance_category:
                        speak_async(desc)
                    
                    last_seen[class_name] = distance_category

                    # Draw bounding box and text on the frame
                    cv2.rectangle(frame, (x1, y1), (x2, y2), (0, 255, 0), 2)
                    cv2.putText(frame, desc, (x1, y1 - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255, 0, 0), 2)

            # Show the camera feed
            cv2.imshow("Raspberry Pi Camera Feed", frame)

            # Exit on 'q' key press
            if cv2.waitKey(1) & 0xFF == ord('q'):
                break

            frame_count += 1

    finally:
        cap.release()
        cv2.destroyAllWindows()
        cleanup_gpio()

if __name__ == "__main__":
    main()
