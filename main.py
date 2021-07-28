import cv2
import serial

middle = (320, 240)
ser = serial.Serial('/dev/ttyACM0', 115200, timeout=.1)

first = ""
second = ""

cascPath = "haarcascade.xml"
faceCascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')

cap = cv2.VideoCapture(0)


def write(pixels):
    ser.write(bytes(pixels, 'utf-8'))


if not cap.isOpened():
    print("Cannot open camera")
    exit()
while True:

    ret, frame = cap.read()

    if not ret:
        print("Can't receive frame (stream end?). Exiting ...")
        break

    frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    frame = cv2.flip(frame, 1)

    faces = faceCascade.detectMultiScale(
        frame,
        scaleFactor=1.1,
        minNeighbors=5,
        minSize=(30, 30),
        flags=cv2.CASCADE_SCALE_IMAGE
    )
    for(x, y, w, h) in faces:

        a = int(x + (w / 2))
        b = int(y + (h / 2))

        cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)
        cv2.line(frame, middle, (a, b), (255, 0, 0), 2)
        cv2.rectangle(frame, middle, (a, b), (0, 0, 255), 2)

        if (320 - a) <= -5:
            first = "-"
        elif (320 - a) >= 5:
            first = "+"
        elif -5 < (320 - a) < 5:
            first = "0"

        if (240 - b) <= -5:
            second = "-"
        elif (240 - b) >= 5:
            second = "+"
        elif -5 < (240 - b) < 5:
            second = "0"

        write(first+second)

        print(first+second)

    cv2.imshow('frame', frame)

    if cv2.waitKey(1) == ord('q'):
        break

ser.close()
