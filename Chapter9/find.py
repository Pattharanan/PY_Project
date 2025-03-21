try:
    # รับชื่อไฟล์จากผู้ใช้
    filename = input('Enter file name : ')  
    # พยายามเปิดไฟล์ในโหมดอ่าน (อ่านเป็นข้อความด้วย encoding utf-8)
    fin = open(filename, encoding='utf-8')  
    # อ่านข้อมูลทั้งหมดจากไฟล์
    data = fin.read()  
    # แสดงข้อมูลที่อ่านได้
    print(data)  
    # ปิดไฟล์หลังจากอ่านเสร็จ
    fin.close()  

# กรณีที่ไฟล์ไม่พบ จะเกิดข้อผิดพลาด FileNotFoundError
except FileNotFoundError:  
    print(f'File "{filename}" not open, this file not found.')

# ถ้าไม่มีข้อผิดพลาดใด ๆ ในบล็อก try จะทำคำสั่งในบล็อก else
else:  
    print('Work Complete.')

# คำสั่งในบล็อก finally จะทำงานเสมอ ไม่ว่าโค้ดจะเกิดข้อผิดพลาดหรือไม่
finally:  
    print('End Program.')