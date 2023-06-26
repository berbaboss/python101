import csv

def writeCsv(datalist):
    with open('data1.csv', 'a', encoding='utf-8', newline='') as file:   #ถ้าไม่ใส่ newline='' จะมีการเพิ่มบรรทัดใหม่ขึ้นมา   [['ขนม', '20', '7.00 น.'], ['ขนม', '20', '7.00 น.'], []]
        fw = csv.writer(file)     #fw = file writer
        fw.writerow(datalist)   # datalist = ['pen','pencil','eraser']


def readCsv():
    with open('data1.csv', encoding='utf-8', newline='') as file:
        fr = csv.reader(file)     #fw = file writer
        data = list(fr)
    return  data

# data1 = ['ขนม','20','7.00 น.']
# writeCsv(data1)

# data1 = readCsv()     [['ขนม', '20', '7.00 น.'], ['ขนม', '20', '7.00 น.']]
# print(data1)          


