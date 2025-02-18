import cv2
alg = "haarcascade_frontalface_default.xml"
haar_cascade = cv2.CascadeClassifier(alg)
detect = cv2.VideoCapture(0)
while True:
    _, img = detect.read()
    grayscale = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    faces = haar_cascade.detectMultiScale(grayscale,1.3,4)
    for (x,w,y,h) in faces:
        cv2.rectangle(img, (x,y), (x+w,y+h), (200, 150, 0), 2)
    cv2.imshow("Face detection and tracking",img)
    key = cv2.waitKey(10)
    if key == ord("q"):
        break
detect.release()
cv2.destroyAllWindows()
        
