import sqlite3

conn = sqlite3.connect("/home/bigpenguin/code/fyp_codes/Accounts.db")

cursor = conn.cursor()

vals=cursor.execute("""SELECT * FROM account_data""")

for i in vals:
    image_encode=i

print(image_encode[0])


