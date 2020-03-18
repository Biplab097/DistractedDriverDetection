import cv2

class ImageCapturing:
    def captureImage(self):
        vidcap = cv2.VideoCapture(0)
        count = 0
        success = True
        fps = int(vidcap.get(cv2.CAP_PROP_FPS))

        while count<700:
            success, image = vidcap.read()
            print('read a new frame:', success)
            if count % (10 * fps) == 0:
                cv2.imwrite('frame%d.jpg' % count, image)
                print('successfully written 10th frame')
            count += 1


ob = ImageCapturing()
ob.captureImage()
