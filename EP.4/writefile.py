
def writedata(text):
    with open('data.txt','w',encoding='utf-8') as file:    # w เป็นการ replace ไฟล์เก่า
        file.write(text)


def adddata(text):
    with open('add-data.txt','a',encoding='utf-8') as file:    # a เป็นการ เพิ้มค่าจากไฟล์เก่า
        file.writelines(text + '\n')


def readdata():
    with open('add-data.txt',encoding='utf-8') as file:
        data = file.readlines()
        return data

# writedata('boss')
# adddata('pek')
# adddata('pu')
# adddata('pig')
# data = readdata()
# for i in data:
#     print(i)

