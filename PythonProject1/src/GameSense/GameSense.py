import cv2
import numpy as np
from ultralytics import YOLO  # YOLOv8 model for object detection
from tkinter import filedialog

# Load YOLOv8 model (pretrained)
model = YOLO("yolov8l.pt")  # Uses a lightweight YOLO model

# Open video file
video_path = filedialog.askopenfilename(title="Select gameplay clip", filetypes=[("MP4 files", "*.mp4")])
cap = cv2.VideoCapture(video_path)

# Get video properties
frame_width = int(cap.get(3))
frame_height = int(cap.get(4))
fps = int(cap.get(5))

# Define background subtractor for motion detection
bg_subtractor = cv2.createBackgroundSubtractorMOG2(history=500, varThreshold=50)


while cap.isOpened():
    ret, frame = cap.read()
    print(f"Frame {ret} read.")
    if not ret:
        break  # Exit loop when video ends

    # Grayscale
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    # Motion detection
    motion_mask = bg_subtractor.apply(gray)

    # Object Detection using YOLOv8
    results = model(frame)

    # Draw detected objects
    for result in results:
        for box in result.boxes:
            x1, y1, x2, y2 = map(int, box.xyxy[0])  # Bounding box coordinates
            confidence = box.conf[0].item()  # Confidence score
            label = result.names[int(box.cls[0])]  # Object class name

            if confidence > 0.5:  # Filter weak detections
                cv2.rectangle(frame, (x1, y1), (x2, y2), (0, 255, 0), 2)
                cv2.putText(frame, f"{label} {confidence:.2f}",
                            (x1, y1 - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 255, 0), 2)

    # Overlay motion mask
    motion_overlay = cv2.addWeighted(frame, 0.7, cv2.cvtColor(motion_mask, cv2.COLOR_GRAY2BGR), 0.3, 0)

    # Display frame
    cv2.imshow("Game Footage Analysis", motion_overlay)

    # Press 'q' to exit
    if cv2.waitKey(5) & 0xFF == ord('q'):
        break

# Cleanup
cap.release()
cv2.destroyAllWindows()
