# Test Create and close Text File

fo = open('mydata.txt', mode='w')
print('Open text file : mydata.txt')
fo.close()
print('Now closed file.')