#adding the main python file here.
print("MoodMirrorAI started") 
import cv2


def start_camera():
    cap = cv2.VideoCapture(0)

    if not cap.isOpened():
        print("Camera not accessible")
        return None

    return cap
    while True:
    ret, frame = cap.read()

    if not ret:
        break

    cv2.imshow("MoodMirrorAI", frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
