my_tuple = ("apple", "banana", "cherry")

print(my_tuple[0])  # "apple"  (ตำแหน่งที่ 0)
print(my_tuple[1])  # "banana" (ตำแหน่งที่ 1)
print(my_tuple[2])  # "cherry" (ตำแหน่งที่ 2)

print(my_tuple[-1])  # "cherry"  (ตัวสุดท้าย)
print(my_tuple[-2])  # "banana" (ตัวก่อนสุดท้าย)
print(my_tuple[-3])  # "apple"  (ตัวแรก)

print("-" * 10)

#การวนลูปผ่านสมาชิกแต่ละตัวของ tuple โดยใช้ for loop
Num = (1, 3, 5, 7, 9)
for n in Num:  # วนลูปแต่ละค่าภายใน tuple
    print(n)