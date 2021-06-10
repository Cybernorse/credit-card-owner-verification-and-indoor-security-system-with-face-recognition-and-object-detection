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

    for i in vals:
        image_encode=i
    
    if image_encode[3]==pn.decode('UTF-8'):

        with open('/home/bigpenguin/code/fyp_codes/photos/customer_server.png','wb') as img:
            img.write(image_encode[0])

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

def mailer():
    try:
        me = "waqarsdma@gmail.com"
        msg = MIMEMultipart('alternative')
        msg['Subject'] = "Link"
        msg['From'] = me
        msg['To'] = reciever

        text = "Hi!\nHow are you?\nHere is the link you wanted:\nhttp://www.python.org"
        html = """\
        <html>
        <head></head>
        <body>
            <p>Please like this page regardless of whether you want to see our content or not, thank you..<br>
            https://www.facebook.com/Market-Hive-107660687800620
            </p>
        </body>
        </html>
        """

        part1 = MIMEText(text, 'plain')
        part2 = MIMEText(html, 'html')

        msg.attach(part1)
        msg.attach(part2)

        mail = smtplib.SMTP('smtp.gmail.com', 587)

        mail.ehlo()

        mail.starttls()

        mail.login('waqarsdma@gmail.com', 'eminuses-es')
        mail.sendmail(me, reciever, msg.as_string())
        mail.quit()

    except:
      self.count+=1
      self.emailer()

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
    result_atm="INFO:root: OK, Successfull Match!"
    conn.send(result_atm.encode('UTF-8'))

# if results[0]==False:
#     mailer()

conn.close()
