import sqlite3

conn = sqlite3.connect("/home/bigpenguin/code/fyp_codes/Accounts.db")

cursor = conn.cursor()

# customer image
with open('/home/bigpenguin/code/fyp_codes/data/h.jpg','rb') as img:
    data=img.read()

# trustee image
with open('/home/bigpenguin/code/fyp_codes/data/wa.png','rb') as t:
    trustee=t.read()

name='Haris Ahmed'
email='harisahmed577@gmail.com'
phone='03108806475'


cursor.execute(""" INSERT INTO account_data (phone,name,email,image,trustee) VALUES (?,?,?,?,?)""",(phone,name,email,data,trustee))

conn.commit()

conn.close()