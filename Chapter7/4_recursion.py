def factorial(n):
    # base case : ถ้า n คือ 0 หรือ 1 ผลลัพธ์คือ 1
    if n == 0 or n == 1:
        return 1
    #  recursive: ถ้า n มากกว่า 1 เรียกฟังก์ชั่นตัวเอง
    else:
        return n * factorial(n - 1)

print(factorial(5))  # ผลลัพธ์คือ 120