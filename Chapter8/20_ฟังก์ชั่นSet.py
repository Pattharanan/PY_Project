# สร้างเซตตัวอย่าง
my_set = {1, 2, 3}

# add(item) - เพิ่มสมาชิก 4
my_set.add(4)
print(my_set)  
# Output: {1, 2, 3, 4}

# remove(item) - ลบสมาชิก 2
my_set.remove(2)
print(my_set)  
# Output: {1, 3, 4}

# union() - รวมเซตกับเซตอื่น
set2 = {3, 4, 5}
union_result = my_set.union(set2)
print(union_result)  
# Output: {1, 3, 4, 5}

# intersection() - หาสมาชิกที่เหมือนกัน
intersection_result = my_set.intersection(set2)
print(intersection_result)  
# Output: {3, 4}