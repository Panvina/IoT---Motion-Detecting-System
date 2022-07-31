import cv2

class CameraProcessor:
    def capture(self, imgLocation):
        cam = cv2.VideoCapture(-1)   #initialise the camera
        while (cam.isOpened()):   #if the camera is opened
            while (True):
                ret, image = cam.read()   #read the frames
                cv2.imwrite(imgLocation,image)   #save it
                break;
            cam.release()   #close the camera
        #cv2.destroyAllWindows()