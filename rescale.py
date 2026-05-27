
import cv2 as cv

#Read a photo and display it rescaled

img = cv.imread('C:/Users/HP/Pictures/1779721082301.jfif')

def rescaleFrame(frame, scale=0.75):
    width = int(frame.shape[1] * scale)
    height = int(frame.shape[0] * scale)
    dimensions = (width, height)

    return cv.resize(frame, dimensions, interpolation=cv.INTER_AREA)

rescaled_image = rescaleFrame(img)
cv.imshow('Original Image', img)
cv.imshow('Rescaled Image', rescaled_image)
cv.waitKey(0)

#Read a video and display it rescaled

capture = cv.VideoCapture('C:\\Users\\HP\\Pictures\\today\\WhatsApp Video 2025-05-27 at 01.51.53_be039ebc.mp4')
while True: 
    ret, frame = capture.read()
    if not ret:
        print("Can't receive frame (stream end?). Exiting ...")
        break
    rescaled_frame = rescaleFrame(frame, scale=0.2)

    cv.imshow('Original Frame', frame)
    cv.imshow('Rescaled Frame', rescaled_frame)
    if cv.waitKey(1) == ord('q'):
        break
capture.release()
cv.destroyAllWindows()
