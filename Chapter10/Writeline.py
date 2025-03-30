datas1 = ['Python', 'Program', '\n']
datas2 = ('Python', 'File', '\n')
datas3 = {'name': 'Python', 'surname': 'Program'}

fout = open('mydata.txt', 'w')

print(fout.write('Hello, text file\n'))
fout.write('Salary : ' + str(1200.5) + '\n')

fout.writelines(datas1)
fout.writelines(datas2)
fout.writelines(datas3)

fout.close()