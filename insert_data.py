import sqlite3

conn = sqlite3.connect("/home/bigpenguin/code/fyp_codes/Accounts.db")

cursor = conn.cursor()


with open('/home/bigpenguin/Downloads/circle-cropped.png','rb') as img:
    data=img.read()
name='waqar ahmad'
email='waqarsher66@gmail.com'
phone='03214038977'

cursor.execute(""" INSERT INTO account_data (image,name,email,phone) VALUES (?,?,?,?)""",(data,name,email,phone))

conn.commit()

conn.close()