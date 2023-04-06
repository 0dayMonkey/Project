import cv2


# imagePath = "appolo.jpg"
cascadeClassifierPath = "haarcascade_frontalface_alt.xml"

cascadeClassifier = cv2.CascadeClassifier(cascadeClassifierPath)
"""
image = cv2.imread(imagePath)

grayImage = cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)

detectedFaces = cascadeClassifier.detectMultiScale(grayImage)

for(x,y,width,height) in detectedFaces:
    cv2.rectangle(image, (x,y), (x+width, y+height), (0,255,0), 5)

    cv2.imwrite("resultat.jpg", image)
"""

cap = cv2.VideoCapture("video.mp4")
fourcc = cv2.VideoWriter_fourcc(*'mp4v')
out = cv2.VideoWriter('resultat.mp4', fourcc, 30.0, (int(cap.get(3)), int(cap.get(4))))

while(cap.isOpened()):
    ret, frame = cap.read()

    if ret == True:
        grayImage = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

        detectedFaces = cascadeClassifier.detectMultiScale(grayImage, scaleFactor = 1.1, minNeighbors = 5, minSize=(20,20))

        for (x,y,width, height) in detectedFaces:
            cv2.rectangle(frame, (x,y), (x+width, y+height), (0,255,0), 1)

        out.write(frame)

        cv2.imshow("resultat",frame)
        if cv2.waitKey(1) == ord('q'):
            break
    else:
        break

cap.release()
out.release()
cv2.destroyAllWindows