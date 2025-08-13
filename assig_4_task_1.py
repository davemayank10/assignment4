
try:
    file = open('file.txt','r')
    print('Reading file content:')
    read_file = file.read()
    print(read_file)
except FileNotFoundError:
    print("Error: The file 'file.txt' was not found")