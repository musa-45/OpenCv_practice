import cv2 as cv

#Read a photo and display it

img = cv.imread('C:/Users/HP/Pictures/1779721082301.jfif')
cv.imshow('image', img)
cv.waitKey(0)


#Read a video and display it
capture = cv.VideoCapture('C:\\Users\\HP\\Pictures\\today\\WhatsApp Video 2025-05-27 at 01.51.53_be039ebc.mp4')
while True:
    ret, frame = capture.read()
    if not ret:
        print("Can't receive frame (stream end?). Exiting ...")
        break
    cv.imshow('frame', frame)
    if cv.waitKey(1) == ord('q'):
        break
capture.release()
cv.destroyAllWindows()


