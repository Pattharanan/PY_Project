# เปิดไฟล์ เพื่ออ่านข้อมูล
fin = open('myscore.txt', encoding='utf-8')

# อ่านข้อมูลทีละบรรทัด
datas = []
data = fin.readline()
while data != "":
    datas.append(data)
    data = fin.readline()

# ปิดไฟล์หลังจากอ่านเสร็จ
fin.close()

# แสดงผลลัพธ์ที่อ่านได้
print(datas)