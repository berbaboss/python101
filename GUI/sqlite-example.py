import sqlite3

# Connect to database (creates the file if it doesn't exist)
conn = sqlite3.connect('knowledge.db')
cursor = conn.cursor()


# # Create table
cursor.execute('''CREATE TABLE IF NOT EXISTS knowledge (id INTEGER PRIMARY KEY, topic TEXT, other TEXT)''')   #ใส่ if not exists เพื่อรันครั้งหน้าจะได้ไม่ error ว่ามี table นี้อยุ่แล้ว


# # Commit changes and close connection
# conn.commit()
# conn.close()

def insert_topic(topic):
    command = "INSERT INTO knowledge (topic, other) VALUES ('{}', '-')".format(topic)
    cursor.execute(command)
    conn.commit()
    conn.close()

# insert_topic('วันนี้ลุงใช้ตัวอย่างในการใช้ chatgpt ในการเรียน python')

def view_topic():
    cursor.execute("SELECT * FROM knowledge")
    rows = cursor.fetchall()   #เป็น list
    for row in rows:
        print(row)
    conn.close()
    return rows

data = view_topic()
print(data[0])