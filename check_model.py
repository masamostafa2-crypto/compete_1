import cv2
from ultralytics import YOLO

MODEL_PATH = "/home/masa/Downloads/best1/best.pt"   # update to the full path if it's not in the same folder
CAMERA_INDEX = 2       # 0 is usually the default/built-in webcam; try 1, 2... if wrong
CONF_THRESHOLD = 0.60
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

    # Convert to grayscale (mono), then back to 3-channel so YOLO can
    # still process it -- this matches the mono8 images the robot's
    # actual camera publishes on /mono/image.
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    mono_frame = cv2.cvtColor(gray, cv2.COLOR_GRAY2BGR)

    results = model(mono_frame, conf=CONF_THRESHOLD, verbose=False, device="cpu")

    for box in results[0].boxes:
        name = results[0].names[int(box.cls[0])]
        conf = float(box.conf[0])
        print(f"Detected: {name} ({conf:.2f})")

    annotated = results[0].plot()
    cv2.imshow("YOLO test (mono)", annotated)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()