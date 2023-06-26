from tkinter import *
from tkinter import ttk
###########################################################
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
    # conn.close()

# insert_topic('วันนี้ลุงใช้ตัวอย่างในการใช้ chatgpt ในการเรียน python')

def view_topic():
    cursor.execute("SELECT * FROM knowledge")
    rows = cursor.fetchall()   #เป็น list
    for row in rows:
        print(row)
    return rows

##########################################################
current_knowledge = view_topic()
count = 0
##########################################################

GUI = Tk()
GUI.title('โปรแกรมบันทึก Uncle Lab')
GUI.geometry('500x400')

FONT1 = ('Angsana New', 15)
FONT2 = ('Angsana New', 30, 'bold')

L = Label(GUI,text='กรอกความรู้ใหม่ในช่อง', font=FONT2, fg='green')
L.pack(pady=10)

v_topic = StringVar()   #ตัวแปรพิเศษที่เก็บจากช่องกรอก

E1 = ttk.Entry(GUI,font='FONT1', textvariable=v_topic, width=60)     #นำช่องกรอกไปใส่ไว้ในโปรแกรมหลัก
E1.pack(pady=20)   #นำช่องกรอกไปแปะติดกับโปรแกรมหลัก #เพิ่มระยะห่างแกน y

def SaveTopic():
    topic = v_topic.get()    # .get เพื่อ return ผลลัพธ์จากช่องกรอก
    insert_topic(topic)     #บันทึกข้อมูล
    v_topic.set('')         #เคลียข้อมูลเก่าออกหลัง save
    E1.focus()              #นำ cursor ไปช่องกรอกเพื่อพิมพ์คำต่อไปได้ทันที
    global current_knowledge       #ทำให้บันทึกนอก function ได้
    current_knowledge = view_topic()

B1 = ttk.Button(GUI,text='บันทึก', command=SaveTopic)
B1.pack(ipadx=30,ipady=15)    #เพิ่มขนาดปุ่ม

v_result = StringVar()
v_result.set(str(current_knowledge[0][0]) +'-'+ current_knowledge[0][1])

L = Label(GUI,textvariable=v_result, font=FONT1, fg='blue')
L.pack(pady=10)

def previous():
    global count
    index = count-1
    count = index
    if count <= 0:
        index = 0
        count = 0
    print(current_knowledge[index])
    v_result.set(str(current_knowledge[index][0]) +'-'+ current_knowledge[index][1])

B2 = ttk.Button(GUI,text='<', width=5, command=previous)
B2.place(x=20,y=250)  #place วางระบุตำแหน่ง

def next():
    global count
    index = count+1
    count = index
    dataLength = len(view_topic())
    if count >= dataLength:
        index = dataLength-1
        count = dataLength-1
    print(current_knowledge[index])
    v_result.set(str(current_knowledge[index][0]) +'-'+ current_knowledge[index][1])

B3 = ttk.Button(GUI,text='>', width=5, command=next)
B3.place(x=440,y=250)  #place วางระบุตำแหน่ง

GUI.mainloop()
