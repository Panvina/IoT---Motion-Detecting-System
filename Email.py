import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.image import MIMEImage

#Email Variables
SMTP_SERVER = 'smtp.gmail.com' #Email Server
SMTP_PORT = 587 #Server Port
GMAIL_USERNAME = 'piberrybot@gmail.com' 
GMAIL_PASSWORD = 'raspberry!@3' 
 
class EmailProcessor:
    def sendmail(self, recipient, subject, content, image):
          
        #Create Headers
        emailData = MIMEMultipart()
        emailData['Subject'] = subject
        emailData['To'] = recipient
        emailData['From'] = GMAIL_USERNAME
        
        #Attach text data
        emailData.attach(MIMEText(content))
        
        #Create image Data from the defined image
        imageData = MIMEImage(open(image, 'rb').read(), 'jpg') 
        imageData.add_header('Content-Disposition', 'attachment; filename="image.jpg"')
        emailData.attach(imageData)
  
        #Connect to Gmail Server
        session = smtplib.SMTP(SMTP_SERVER, SMTP_PORT)
        session.ehlo()
        session.starttls()
        session.ehlo()
  
        #Login to Gmail
        session.login(GMAIL_USERNAME, GMAIL_PASSWORD)
  
        #Send Email & Exit
        session.sendmail(GMAIL_USERNAME, recipient, emailData.as_string())
        session.quit