# สร้างดิกชันนารี A และ B
A = {'apple': 10, 'banana': 5, 'cherry': 8}
B = {'banana': 5, 'cherry': 8, 'apple': 10}

# ใช้โอเปอเรเตอร์ in และ not in
print('apple' in A)   # True  ('apple' เป็น key ใน A)
print('grape' not in A) # True  ('grape' ไม่มีใน A)

# ใช้โอเปอเรเตอร์เปรียบเทียบ
print(A == B)  # True  (ค่าของ A และ B เท่ากัน)
print(A != B)  # False (A และ B ไม่แตกต่างกัน)

# ใช้ฟังก์ชัน Built-in
print(len(A))  # 3 (A มี 3 key)
print(max(A))  # 'cherry' (เรียง key ตามลำดับตัวอักษร)
print(min(A))  # 'apple' (เรียง key ตามลำดับตัวอักษร)
print(sum(A.values()))  # 23 (ผลรวมของค่าทั้งหมดใน A)