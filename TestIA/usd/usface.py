import numpy as пр
import cv2
import pickle

face_cascade = cv2.CascadeClassifier("usd/cascades/data/haarcascade_frontalface_alt2.xml")
# eye_cascade = cv2.CascadeClassifier("usd/cascades/data/haarcascade_eye.xml")
face_cascade_profil = cv2.CascadeClassifier("usd/cascades/data/haarcascade_profileface.xml")
face_cascade_def = cv2.CascadeClassifier("usd/cascades/data/haarcascade_frontalface_default.xml")

recognizer = cv2.face.LBPHFaceRecognizer_create()
recognizer.read("trainner.yml")

labels = {}
with open("labels.pickle", "rb") as f:
    og_labels = pickle.load(f)
    labels = {v:k for k,v in og_labels.items()}

cap = cv2.VideoCapture(0)
while(True):
    # Enregistre chaque frame
    ret, frame = cap. read()

    gray = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(gray, scaleFactor=10, minNeighbors=5)
    for (x,y,w,h) in faces:
        print(x,y,w,h)
        roi_gray = gray[y:y+h, x:x+w]
        roi_color = frame[y:y+h, x:x+w]

        id_, conf = recognizer.predict(roi_gray)
        if conf>=45: # and conf <=85:
            print(id_)
            print(labels[id_])
            font = cv2.FONT_HERSHEY_SIMPLEX
            name = labels[id_]
            color = (255,255,255)
            stroke =  2
            cv2.putText(frame,name, (x,y-20), font, 1, color, stroke, cv2.LINE_AA)
        img_item = "my-image.png"
        cv2.imwrite(img_item,roi_gray)
 
        color = (255,180,120)
        stroke = 2
        end_cordx = x+w
        end_cordy = y+h
        cv2.rectangle(frame, (x,y), (end_cordx, end_cordy), color )
        faces_profile = face_cascade_profil.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=5)
        faces_def = face_cascade_def.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=5)
        for (px, py, pw, ph) in faces_profile:
            cv2.rectangle(roi_color, (px, py), (px+pw, py+ph), (0, 0, 255), 2)

        for (dx, dy, dw, dh) in faces_def:
            cv2.rectangle(roi_color, (dx, dy), (dx+dw, dy+dh), (255, 0, 0), 2)
        """
        eyes = eye_cascade.detectMultiScale(roi_gray)
        for (ex,ey,ew,eh) in eyes:
            cv2.rectangle(roi_color, (ex,ey), (ex+ew,ey+eh), (0,255,0), 2)
        """
    
    # Montre la nouvelle frame
    cv2. imshow("frame" ,frame)
    if cv2.waitKey (20) & 0xFF == ord('q'):
        break

# Quand tout est bon, on peux release la capture et fermer les fenetes
cap.release()
cv2.destroyAllWindows ()