import cv2
import numpy as np
import os

for i in range(20,80):

    # Playing video from file:
    cap = cv2.VideoCapture('video%d.mp4' % i)

    try:
        if not os.path.exists('data%d' % i):
            os.makedirs('data%d' % i)
    except OSError:
        print ('Error: Creating directory of data' + str(i))

    currentFrame = 0

    # Capture frame-by-frame
    ret, frame = cap.read()

    while(ret):
        # Saves image of the current frame in jpg file
        if currentFrame % 30 == 0 and ret:
            name = ('./data%d/frame' % i) + str(currentFrame) + '.jpg'
            print ('Creating...' + name)
            test = frame
            cv2.imwrite(name, frame)

        # To stop duplicate images
        currentFrame += 1

        ret, frame = cap.read()


    # When everything done, release the capture
    cap.release()
    cv2.destroyAllWindows()