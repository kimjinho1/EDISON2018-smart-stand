import cv2

cap = cv2.VideoCapture(0)

while cap.isOpened():
    ret, frame = cap.read()
    if ret:
        cv2.imshow('camera-0', frame)
        cv2.imwrite('image.jpg', frame)
        break
    else:
        print('no camera')
        break
cap.release()
cv2.destroyAllWindows()
