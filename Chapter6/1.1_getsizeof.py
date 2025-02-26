import sys  # นำเข้าไลบรารี sys

text = "Hello, Python!"  # กำหนดตัวแปร text ให้เก็บข้อความ
size = sys.getsizeof(text)  # ใช้ฟังก์ชัน getsizeof() เพื่อตรวจสอบขนาดของตัวแปร text

print("ขนาดของตัวแปร text คือ", size, "ไบต์")  # แสดงผลขนาดของตัวแปร