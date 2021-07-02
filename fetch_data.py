# import sqlite3

# conn = sqlite3.connect("/home/bigpenguin/code/fyp_codes/Accounts.db")

# cursor = conn.cursor()

# vals=cursor.execute("""SELECT * FROM account_data""")

# image_encode=[]
# num='03007998847'
# for i in vals.fetchall():
#     print(i[0])
#     # if num == i[0]:
#     #     print(i[3])
# # for i in vals:
# #     image_encode.append(i)

import smtplib
from email import encoders
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email.mime.image import MIMEImage

strFrom = 'bigpenguincave@gmail.com'
strTo = 'waqarsher66@gmail.com'

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
fp = open('/home/bigpenguin/code/fyp_codes/data/wa.png', 'rb') #Read image 
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