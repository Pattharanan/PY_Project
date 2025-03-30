fin = open('mydata.txt', 'r')  
content1 = fin.read(10)  # อ่านขึ้นมา 10 ตัวอักษร  
content = fin.read()  # อ่านจนหมดไฟล์  
fin.close()  

print(content1)  
print(content)