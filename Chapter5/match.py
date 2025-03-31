violation = input("คุณทำผิดกรณีใด? (ขับเร็ว/ฝ่าไฟแดง/ย้อนศร): ")

match violation:
    case "ขับเร็ว":
        fine_amount = 500
        print("คุณโดนปรับ " + str(fine_amount) + " บาท - ขับรถเร็วเกินกำหนด")
    case "ฝ่าไฟแดง":
        fine_amount = 1000
        print("คุณโดนปรับ " + str(fine_amount) + " บาท - ฝ่าสัญญาณไฟแดง")
    case "ย้อนศร":
        fine_amount = 2000
        print("คุณโดนปรับ " + str(fine_amount) + " บาท - ขับรถย้อนศร")
    case _:
        print("ประเภทการกระทำผิดไม่ถูกต้อง กรุณาลองใหม่!")