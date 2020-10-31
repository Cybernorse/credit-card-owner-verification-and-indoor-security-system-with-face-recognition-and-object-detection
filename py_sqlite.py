import sqlite3
import face_recognition

conn = sqlite3.connect("Accounts.db")

cursor = conn.cursor()

''' creating table '''
# cursor.execute(""" 
# CREATE TABLE account_data (name TEXT,image BLOP)
# """)

''' insert values into the data '''
# with open('/home/bigpenguin/Downloads/circle-cropped.png','rb') as img:
#     data=img.read()
# name='waqar ahmad'
# cursor.execute(""" INSERT INTO account_data (name,image) VALUES (?,?)""",(name,data))

vals=cursor.execute("""SELECT * FROM account_data""")
for i in vals:
    image_encode=i[1]

with open('/home/bigpenguin/Downloads/waqar.png','wb') as img:
    img.write(image_encode)

conn.commit()
cursor.close
conn.close()

known_image = face_recognition.load_image_file("/home/bigpenguin/Downloads/circle-cropped.png")
unknown_image = face_recognition.load_image_file("/home/bigpenguin/Downloads/waqar.png")

biden_encoding = face_recognition.face_encodings(known_image)[0]
unknown_encoding = face_recognition.face_encodings(unknown_image)[0]

results = face_recognition.compare_faces([biden_encoding], unknown_encoding)
print(results)