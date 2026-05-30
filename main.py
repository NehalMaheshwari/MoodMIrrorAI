import cv2
from fer import FER

print("MoodMirrorAI started")

# here i have Loaded emotion detector
detector = FER(mtcnn=True)

# here face detector is loaded
face_detector = cv2.CascadeClassifier(
    cv2.data.haarcascades + 'haarcascade_frontalface_default.xml'
)


def start_camera():
    cap = cv2.VideoCapture(0)

    if not cap.isOpened():
        print("Camera not accessible")
        return None

    return cap


def detect_emotion(frame):

    results = detector.detect_emotions(frame)

    for face in results:

        emotions = face["emotions"]
        emotion = max(emotions, key=emotions.get)

        x, y, w, h = face["box"]

        # Draw rectangle
        cv2.rectangle(
            frame,
            (x, y),
            (x + w, y + h),
            (0, 255, 0),
            2
        )

        # Display emotion text
        cv2.putText(
            frame,
            emotion,
            (x, y - 10),
            cv2.FONT_HERSHEY_SIMPLEX,
            1,
            (0, 255, 0),
            2
        )

    return frame


def run_emotion_detector():

    cap = start_camera()

    if cap is None:
        return

    while True:

        ret, frame = cap.read()

        if not ret:
            break

        # Detect emotions
        frame = detect_emotion(frame)

        # Display output
        cv2.imshow("MoodMirrorAI", frame)

        # Press Q to quit
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    cap.release()
    cv2.destroyAllWindows()


# Run application
run_emotion_detector()
```
