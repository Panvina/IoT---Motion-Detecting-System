import cv2
import serial
import time
import MySQLdb
from datetime import datetime
from Email import EmailProcessor
from Camera import CameraProcessor

#set up the serial line to recieve data from Arduino
ser = serial.Serial('/dev/ttyACM0',9600)

#initialise email object and variables
sendEmail = EmailProcessor()
email = 'tpanvina@gmail.com'
subject = "Motion Detected!"
content = "Motion has been detected at: "

#initialise camera object
capImage = CameraProcessor()

#initialise the num of photo
photoNum = 0

while (True):   # Read and record the data
    line = ser.readline().decode('utf-8')    #read each line from the serial port and decode it
    print(line)     #print the data
    if line.startswith('1'):    #if the serial data contains a high value
        #Capture the intruder and passed in the location and the title of the photo
        img = '/home/pi/Documents/IoT/DetectedPhotos/'+str(photoNum)+'.jpg'
        capImage.capture(img)       #call a function from camera class     
        photoNum+= 1
        currentT = datetime.now().ctime()   #assign the current time       
        sendEmail.sendmail(email,subject,content+currentT,img)   #Send email when the motion is detected  
        #connecting to the database 
        dbConn = MySQLdb.connect("localhost","vina","","detection_db") or  die ("Could not connect to database")
        with dbConn:
            cursor = dbConn.cursor()            
            cursor.execute("INSERT INTO motionLog (timeDetected) VALUES('"+currentT+"')")
            dbConn.commit()
            cursor.close()
    time.sleep(0.1) 
ser.close()


