balance = 5000  # เงินในบัญชี

while balance > 0:
    print("ยอดเงินในบัญชี:", balance, "บาท")
    withdraw_amount = int(input("กรุณาใส่จำนวนเงินที่ต้องการถอน: "))
    
    if withdraw_amount > balance:
        print("ยอดเงินในบัญชีไม่พอถอน!")
    elif withdraw_amount <= 0:
        print("กรุณาใส่จำนวนเงินที่ถูกต้อง!")
    else:
        balance -= withdraw_amount  # หักเงินออกจากบัญชี
        print("ถอนเงิน", withdraw_amount, "บาท (ยอดคงเหลือ:", balance, "บาท)")

print("เงินในบัญชีหมดแล้ว!")