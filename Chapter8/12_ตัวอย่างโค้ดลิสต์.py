from random import randint

# main program
student = int(input("Enter number of student : "))
subject = int(input("Enter number of subject : "))

# create list variable
scores = []

# generate data in list
for r in range(student):
    scores.append([]) # add list
    for c in range(subject):
        scores[r].append(randint(0, 100)) # random value

# display
for score in scores:
    print(score)