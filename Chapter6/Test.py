name = input('Enter your name: ')
num = len(name)

print("\nShow Triangle name")
for i in range(num, 0, -1):  # ใช้ลูปเริ่มจากจำนวนอักขระทั้งหมด แล้วลดลงทีละตัว
    print(name[:i])  # แสดงผลชื่อที่ตัดตัวอักษรตามลำดับ