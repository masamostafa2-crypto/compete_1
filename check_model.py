import cv2
from ultralytics import YOLO
MODEL_PATH = "/home/masa/Downloads/best.pt"   # update to the full path if it's not in the same folder
CAMERA_INDEX = 0          # 0 is usually the default/built-in webcam; try 1, 2... if wrong
CONF_THRESHOLD = 0.6

model = YOLO(MODEL_PATH)
print("Model classes:", model.names)

cap = cv2.VideoCapture(CAMERA_INDEX)
if not cap.isOpened():
    print(f"Could not open camera index {CAMERA_INDEX}")
    exit(1)

print("Press 'q' to quit.")

while True:
    ret, frame = cap.read()
    if not ret:
        print("Failed to grab frame.")
        break

    results = model(frame, conf=CONF_THRESHOLD, verbose=False, device="cpu")

    for box in results[0].boxes:
        name = results[0].names[int(box.cls[0])]
        conf = float(box.conf[0])
        print(f"Detected: {name} ({conf:.2f})")

    annotated = results[0].plot()
    cv2.imshow("YOLO test", annotated)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()