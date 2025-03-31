correct_password = "secure123"
user_input = input("กรุณากรอกรหัสผ่าน: ")



if user_input == correct_password:
    print("เข้าสู่ระบบสำเร็จ ✅")
else:
    print("รหัสผ่านผิดพลาด ❌ กรุณาลองอีกครั้ง")