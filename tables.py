import sqlite3

conn = sqlite3.connect("/home/bigpenguin/code/fyp_codes/Accounts.db")

cursor = conn.cursor()

cursor.execute(""" 
CREATE TABLE account_data (phone TEXT,name TEXT,email TEXT,image BLOP,trustee BLOP)
""")
