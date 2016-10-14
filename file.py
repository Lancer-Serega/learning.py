filename = 'none.txt'

file = open(filename, 'r', -1, 'utf-8')
newFileName = '_backup_' + file.name
newFile = open(newFileName, 'w', -1, 'utf-8')

print(newFile.write(file.read()))

file.close()
newFile.close()
