import os
import cv2
import shutil
import sys

imagePath = "pdatabase/img4.jpg"

image = cv2.imread(imagePath)
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

faceCascade = cv2.CascadeClassifier(cv2.data.haarcascades + "haarcascade_frontalface_default.xml")
faces = faceCascade.detectMultiScale(
    gray,
    scaleFactor=1.3,
    minNeighbors=3,
    minSize=(30, 30)
)

print("Found {0} Faces.".format(len(faces)))


# creating cropped folder
if len(faces)>1:
    if os.path.exists("cropped"):
        shutil.rmtree("cropped")
    os.mkdir("cropped")
    for (x, y, w, h) in faces:
        cv2.rectangle(image, (x, y), (x + w, y + h), (0, 255, 0), 2)
        temp = image[y:y + h, x:x + w]
        print("Saving")
        cropped_file_name = str(w) + str(h)+ ".jpg"
        cropped_file_path = "cropped" + "/" + cropped_file_name 
        cv2.imwrite(cropped_file_path, temp)
else:
    for (x, y, w, h) in faces:
        cv2.rectangle(image, (x, y), (x + w, y + h), (0, 255, 0), 2)
        temp = image[y:y + h, x:x + w]
        print("Saving")
        cv2.imwrite(str(w) + str(h)+ ".jpg", temp)


