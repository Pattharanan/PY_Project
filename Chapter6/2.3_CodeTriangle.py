# รับจำนวนชั้นของสามเหลี่ยมจากผู้ใช้
rows = int(input("ป้อนจำนวนชั้นของสามเหลี่ยม: "))

# วนลูปสร้างสามเหลี่ยม
for i in range(1, rows + 1):
    print("*" * i)