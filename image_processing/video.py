import cv2 
path = r'WhatsApp Video 2022-12-27 at 6.06.13 PM.mp4'
video = cv2.VideoCapture(path)

while True:
    status, img = video.read()
    if not status:
        break
    cv2.imshow('video',img)
    if cv2.waitKey(1)==27:
        break
video.release()
cv2.destroyAllWindows()
