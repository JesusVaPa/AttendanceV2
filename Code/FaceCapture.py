import cv2
import os
import imutils
import sys

personName = sys.argv[1]
dataPath = 'D:\\LaSalle\Computer architecture\Project\Data'
personPath = os.path.join(dataPath, personName)

if not os.path.exists(personPath):
    print('Folder created:', personPath)
    os.makedirs(personPath)

cap = cv2.VideoCapture(0, cv2.CAP_DSHOW)

faceClassif = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')
count = 0

while True:
    ret, frame = cap.read()
    if ret == False:
        break
    frame = imutils.resize(frame, width=640)
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    auxFrame = frame.copy()

    faces = faceClassif.detectMultiScale(gray, 1.3, 5)

    for (x, y, w, h) in faces:
        cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)
        visage = auxFrame[y:y + h, x:x + w]
        visage = cv2.resize(visage, (150, 150), interpolation=cv2.INTER_CUBIC)
        cv2.imwrite(personPath + '/visage_{}.jpg'.format(count), visage)
        count = count + 1
    cv2.imshow('frame', frame)

    k = cv2.waitKey(1)
    if k == 27 or count >= 500:
        break

cap.release()
cv2.destroyAllWindows()
