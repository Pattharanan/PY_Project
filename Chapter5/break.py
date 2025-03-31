# กำหนดปริมาณพลังงานที่ต้องการกินในแต่ละวัน (cal)
target_calories = int(input("กรุณากำหนดปริมาณแคลอรี่ที่ต้องการกินในวันนี้ (cal): "))
total_calories = 0  # เก็บแคลอรี่ที่กินไปแล้ว

while True:
    calories = int(input("กรุณากรอกจำนวนแคลอรี่ที่คุณกินไปในแต่ละมื้อ: "))
    total_calories += calories  # เพิ่มแคลอรี่ที่กินไปแล้ว

    remaining_calories = target_calories - total_calories  # คำนวณแคลอรี่ที่เหลือ
    print("คุณกินไปแล้ว " + str(total_calories) + " cal")
    
    if total_calories < target_calories:
        print("เหลืออีก " + str(remaining_calories) + " cal จะครบพลังงานที่ต้องการต่อวัน")
    
    # หยุดการทำงานเมื่อถึงหรือเกินเป้าหมาย
    if total_calories >= target_calories:
        print("ปริมาณแคลอรี่ที่ต้องการของวันนี้ครบแล้ว!")
        break  # หยุดการทำงานเมื่อถึงเป้าหมาย

print("สิ้นสุดการกินแคลอรี่ของวันนี้!")