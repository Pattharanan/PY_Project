filename = input('Enter file name : ')

try:
    with open(filename, encoding='utf-8') as fin:
        data = fin.read()
        print(data)
except FileNotFoundError:
    print(f'File "{filename}" not open, this file not found.')
else:
    print('Work Complete.')
finally:
    print('End Program.')