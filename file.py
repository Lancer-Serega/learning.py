filename = input('Введите имя файла который хотите забэкапить: ')

file = open(filename, 'rb')
newFileName = '_backup_' + file.name
newFile = open(newFileName, 'wb')

print('файл "' + filename + '"' + ' успешно скопирован!')
print('новое имя файла - ' + newFileName)
print(str(newFile.write(file.read())) + ' байт скопировано')

file.close()
newFile.close()
