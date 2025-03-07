# ชื่อไฟล์_Modules.py
def sum_number(start=1, end=10):
    sum = 0  # กำหนดค่าเริ่มต้นของผลรวมเป็น 0
    for n in range(start, end+1):  # วนลูปตั้งแต่ start ถึง end
        sum += n  # บวกค่า n เข้าไปในผลรวม
    return sum  # ส่งค่าผลรวมกลับ

def factorial(num):
    if num > 1:
        return num * factorial(num - 1)  # เรียกฟังก์ชันตัวเองโดยลดค่า num ทีละ 1
    else:
        return 1  # กรณี num = 1 หรือ 0, คืนค่า 1

def draw_triangle(ch, num):
    for n in range(1, num + 1):  # วนลูปตั้งแต่ 1 ถึง num
        print(ch * n)  # พิมพ์ ch ซ้ำกัน n ครั้ง