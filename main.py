#adding the main python file here.
print("MoodMirrorAI started") 
import cv2


def start_camera():
    cap = cv2.VideoCapture(0)

    if not cap.isOpened():
        print("Camera not accessible")
        return None

    return cap
