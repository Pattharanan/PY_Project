import sys  # นำเข้าไลบรารี sys

# สร้างตัวแปรประเภท int และ float
num_int = 100
num_float = 100.50

# ตรวจสอบขนาดของตัวแปรแต่ละตัว
size_int = sys.getsizeof(num_int)
size_float = sys.getsizeof(num_float)

# แสดงผลลัพธ์
print("ขนาดของตัวแปร num_int คือ", size_int, "ไบต์")
print("ขนาดของตัวแปร num_float คือ", size_float, "ไบต์")