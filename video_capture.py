import cv2, time


 
# video = cv2.VideoCapture(1)
# video.set(3, 1920)
# video.set(4, 1080)
# video.set(15, 0.1)


#face_cascade = cv2.CascadeClassifier(r"C:\Users\Alice\Documents\Udemy\Python10Apps\app6\Files\haarcascade_frontalface_default.xml")



video = cv2.VideoCapture(0)
video.set(3, 1920)
video.set(4, 1080)
video.set(15, 0.1)
#video.open(0)
#if video.isOpened():
    #time.sleep(2)

while True:
    check, frame = video.read()

    #time.sleep(2)
    # print(check)
    # print(frame)
    # cv2.imwrite(".\\my_foto2.jpg", frame)

    #time.sleep(3)
    #img = cv2.imread(r"C:\Users\Alice\Documents\Udemy\Python10Apps\app6\my_foto.jpg")
    # gray_img = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    # faces = face_cascade.detectMultiScale(gray_img, scaleFactor=1.05, minNeighbors=5)

    # for x, y, w, h in faces:
    #     frame = cv2.rectangle(frame, (x,y), (x+w,y+h), (0,255,0), 3)


    cv2.imshow("Capturing", frame)
    key = cv2.waitKey(1)
    if key == ord('q'):
        break

video.release()
cv2.destroyAllWindows()
