import cv2 as cv

centx = 320
centy = 240

cap = cv.VideoCapture(0)

while True:
    cx = 0
    cy = 0
    ret, frame = cap.read()

    gray = cv.cvtColor(frame, cv.COLOR_BGR2GRAY)

    haar_cascade = cv.CascadeClassifier('haar_face.xml') # haar cascades are free for download publicly online
    faces_rect = haar_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=20)

    for(x, y, w, h) in faces_rect:
        cv.rectangle(frame, (x, y), (x+w, y+h), (0, 0, 255), 2)

        cx = int(x + (w/2))
        cy = int(y + (h/2))

        cv.circle(frame, (cx, cy), 4, (0, 0, 255), -1)
        cv.circle(frame, (centx, centy), 4, (0, 255, 0), -1)
        # (320, 240) center
    # if cx == 0 & cy == 0:
    #     print('no target')
    # elif cx > centx:
    #     print("move left")
    #     if cy > centy:
    #         print('move down')
    #     elif cy < centy:
    #         print('move up')
    # elif cx < centx:
    #     print("move right")
    #     if cy > centy:
    #         print('move down')
    #     elif cy < centy:
    #         print('move up')
    # if ((cx < centx + 10) | (cx > centx - 10)) & ((cy < centy + 10) | (cy > centy - 10)):
    #     print('lock')

    cv.imshow('Watchmen', frame)
    key = cv.waitKey(30)
    if key == 27: #escape key
        break

cap.release()
cv.destroyAllWindows()
