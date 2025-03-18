# สร้างดิกชันนารี Numbers ที่มี key เป็นตัวเลข และ value เป็นข้อความ
Numbers = {1: 'One', 2: 'Two', 3: 'Three'}

# เข้าถึงค่าในดิกชันนารีโดยใช้ key
print(Numbers[1])  # แสดงค่า 'One'

# วนลูปแสดง key ทั้งหมดในดิกชันนารี
for n in Numbers:
    print(n)  # แสดง key ทีละตัว

# วนลูปแสดงทั้ง key และ value
for n in Numbers:
    print(n, Numbers[n])  # แสดง key และ value ของดิกชันนารี