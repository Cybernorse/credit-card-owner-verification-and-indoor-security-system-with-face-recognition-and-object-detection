import sqlite3

conn = sqlite3.connect("/home/bigpenguin/code/fyp_codes/Accounts.db")

cursor = conn.cursor()

cursor.execute(""" 
CREATE TABLE account_data (image BLOP,name TEXT,email TEXT,phone TEXT)
""")
