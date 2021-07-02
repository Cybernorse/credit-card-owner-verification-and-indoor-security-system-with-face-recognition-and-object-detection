import socket
import cv2
import time
from imutils.video import VideoStream
from imutils.video import FPS
import sqlite3
import face_recognition

import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

def get_cust(pn):
    conn = sqlite3.connect("/home/bigpenguin/code/fyp_codes/Accounts.db")

    cursor = conn.cursor()

    vals=cursor.execute("""SELECT * FROM account_data""")

    for i in vals.fetchall():
        if pn.decode('UTF-8') == i[0]:  
            with open('/home/bigpenguin/code/fyp_codes/photos/customer_server.png','wb') as img:
                img.write(i[3])

def capture_photo():
    
    vs = VideoStream(src=0,resolution=(512,512),framerate=50).start()
    time.sleep(4.0)
    fps = FPS().start()

    while True:
        frame = vs.read()
        showPic = cv2.imwrite("/home/bigpenguin/code/fyp_codes/photos/customer_atm.png",frame)
        break

    fps.stop()
    print("[INFO] elapsed time: {:.2f}".format(fps.elapsed()))
    print("[INFO] approx. FPS: {:.2f}".format(fps.fps()))

    cv2.destroyAllWindows()
    vs.stop()

def compare_images():
    known_image = face_recognition.load_image_file("/home/bigpenguin/code/fyp_codes/photos/customer_server.png")
    unknown_image = face_recognition.load_image_file("/home/bigpenguin/code/fyp_codes/photos/customer_atm.png")

    biden_encoding = face_recognition.face_encodings(known_image)[0]
    unknown_encoding = face_recognition.face_encodings(unknown_image)[0]

    results = face_recognition.compare_faces([biden_encoding], unknown_encoding)
    
    print(results)

    return results

def trustee_compare():
    conn = sqlite3.connect("/home/bigpenguin/code/fyp_codes/Accounts.db")

    cursor = conn.cursor()

    vals=cursor.execute("""SELECT * FROM account_data""")
    
    for i in vals.fetchall():
        if pn.decode('UTF-8') == i[0]:  
            with open('/home/bigpenguin/code/fyp_codes/photos/customer_server.png','wb') as img:
                img.write(i[4])

def mailer():

    conn = sqlite3.connect("/home/bigpenguin/code/fyp_codes/Accounts.db")

    cursor = conn.cursor()

    vals=cursor.execute("""SELECT * FROM account_data""")
    
    for i in vals.fetchall():
        if pn.decode('UTF-8') == i[0]:  
                reciever=i[2]

    import smtplib
    from email import encoders
    from email.mime.multipart import MIMEMultipart
    from email.mime.text import MIMEText
    from email.mime.base import MIMEBase
    from email.mime.image import MIMEImage

    strFrom = 'bigpenguincave@gmail.com'
    strTo = reciever

    # Create the root message 

    msgRoot = MIMEMultipart('alternative')
    msgRoot['Subject'] = 'CRITICAL BANK ACCOUNT ALERT'
    msgRoot['From'] = strFrom
    msgRoot['To'] = strTo
    # msgRoot['Cc'] =cc
    msgRoot.preamble = 'Multi-part message in MIME format.'

    msgAlternative = MIMEMultipart('alternative')
    msgRoot.attach(msgAlternative)

    msgText = MIMEText('Alternative plain text message.')
    msgAlternative.attach(msgText)

    msgText = MIMEText('<b>This personal has tried to access your bank account with your card</b><br><img src="cid:image1" width="400" height="450"><br>', 'html')
    msgAlternative.attach(msgText)

    #Attach Image 
    fp = open('/home/bigpenguin/code/fyp_codes/photos/customer_atm.png', 'rb') #Read image 
    msgImage = MIMEImage(fp.read())
    fp.close()



    # Define the image's ID as referenced above
    msgImage.add_header('Content-ID', '<image1>')
    msgRoot.attach(msgImage)

    # import smtplib
    smtp = smtplib.SMTP('smtp.gmail.com', 587)
    smtp.ehlo()

    smtp.starttls()
    # smtp.connect('smtp.gmail.com',587) 
    smtp.login('bigpenguincave@gmail.com', 'eminuses-eyeslash') #Username and Password of Account
    smtp.sendmail(strFrom, strTo, msgRoot.as_string())
    smtp.quit()


binded_ip='0.0.0.0'
binded_port=5555
binded_client=socket.socket(socket.AF_INET,socket.SOCK_STREAM)

print("INFO:root: Server is Active...")
print("INFO:root: Listening For Connections...")

binded_client.bind((binded_ip,binded_port))

binded_client.listen(5)
conn,addr=binded_client.accept()

pn=conn.recv(4065)

print("INFO:root: Key recieved -->",pn)
print('INFO:root: [*]<-- Fetching Target Data from the Database -->[*]')

get_cust(pn)

clients_data="INFO:root: [*] Initializing Camera..."

conn.send(clients_data.encode('UTF-8'))

init_cam=conn.recv(4065)

if init_cam.decode('UTF-8')=='0':
    capture_photo()

photo_comp="INFO:root: Photo Taken Successfully, Please Wait while we verify your authenticity..."

conn.send(photo_comp.encode('UTF-8'))

results=compare_images()

if results[0]==True:
    result_atm="INFO:root: OK, Successfull Match! \
    Allowing trasaction"
    conn.send(result_atm.encode('UTF-8'))

if results[0]==False:
    result_atm="CRITICAL:root: Your Photo did not match our database \
    Scanning Your Trustees..."
    conn.send(result_atm.encode('UTF-8'))
    trustee_compare()
    results2=compare_images()

    if results2[0]==True:
        ts="INFO:root: Trustee Scan Successfull! \
        Allowing Trasaction"
        conn.send(ts.encode('UTF-8'))
    if results2[0]==False:
        ts="AlERT:root: Trustee Scan Failed\
        Canceling Transaction "
        conn.send(ts.encode('UTF-8'))

        print("HIGH ALERT:root: Sending ALERT report to the bank ....")
        print("HIGH ALERT:root: Sending Signal to ATM to capture card ....")
        print("HIGH ALERT:root: Sending Email to the Card Owner ....")

        mailer()

conn.close()
