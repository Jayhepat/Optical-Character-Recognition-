import cv2
import pytesseract
from picamera.array import PiRGBArray
from picamera import PiCamera
import time

# Initialize the PiCamera
camera = PiCamera()
camera.resolution = (640, 480)
camera.framerate = 30

# Allow the camera to warm up
time.sleep(0.1)

# Prepare PiRGBArray for image capture
raw_capture = PiRGBArray(camera, size=(640, 480))

# Capture frames continuously
for frame in camera.capture_continuous(raw_capture, format="bgr", use_video_port=True):
    image = frame.array  # Get image as NumPy array

    cv2.imshow("Frame", image)  # Show image preview

    text = pytesseract.image_to_string(image)  # Run OCR
    print("Recognized Text:")
    print(text)

    raw_capture.truncate(0)  # Clear stream for next frame

    # Press 'q' to quit
    if cv2.waitKey(1) & 0xFF == ord("q"):
        break

cv2.destroyAllWindows()
