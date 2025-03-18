# สร้างดิกชันนารีว่าง
A = {}

# สร้างดิกชันนารี B ที่มี key '1' (string) และ value 'one'
B = {'1': 'one'}

# เพิ่ม key 1 (integer) ใน A และกำหนดค่าเป็น 1500.5
A[1] = 1500.5  

# เพิ่ม key 1 (integer) ใน B และกำหนดค่าเป็น 'Python'
B[1] = 'Python'  

#C['one'] = 2000  # ❌ Error: NameError: name 'C' is not defined
 
# เพิ่ม key 2 (integer) ใน A และกำหนดค่าเป็น list ['Python', 'Program']
A[2] = ['Python', 'Program']  

# เพิ่ม key 'B+' (string) ใน B และกำหนดค่าเป็น 3.5
B['B+'] = 3.5  

# แสดงค่าทั้งหมดในแต่ละดิกชันนารี
print("A:", A)  
print("B:", B)