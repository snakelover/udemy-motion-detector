import cv2

face_cascade = cv2.CascadeClassifier(r"C:\Users\Alice\Documents\Udemy\Python10Apps\app6\Files\haarcascade_frontalface_default.xml")

img = cv2.imread(r"C:\Users\Alice\Documents\Udemy\Python10Apps\app6\my_foto.jpg")
gray_img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

faces = face_cascade.detectMultiScale(gray_img, scaleFactor=1.05, minNeighbors=5)

for x, y, w, h in faces:
    img = cv2.rectangle(img, (x,y), (x+w,y+h), (0,255,0), 3)

cv2.imshow("Face", img)
cv2.waitKey(0)
cv2.destroyAllWindows()

