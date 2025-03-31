total = 0.0  
num_scores = 5  # กำหนดจำนวนรอบที่ต้องการรับค่า

for n in range(1, num_scores + 1):  
    score = float(input(f"Enter Score #{n} : "))  
    total += score  

print("\nTotal score value :", total)  
print("Average score :", total / num_scores)