#adding the main python file here.
print("MoodMirrorAI started") 
import cv2
from fer import FER

detector = FER(mtcnn=True)

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
results = detector.detect_emotions(frame)

for face in results:
    emotions = face["emotions"]
    emotion = max(emotions, key=emotions.get)

    cv2.putText(frame, emotion, (20, 40),
                cv2.FONT_HERSHEY_SIMPLEX,
                1, (0, 255, 0), 2)
