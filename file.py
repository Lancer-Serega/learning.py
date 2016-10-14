# coding: utf-8
filename = 'none.txt'  # input('Введите имя файла который хотите забэкапить: ') + '.txt'
# method = input('Хотите посмотреть какие данные будут скопированы? (y/N): ')

file = open(filename, 'r', -1, 'utf-8')
newFileName = '_backup_' + file.name

newFile = open(newFileName, 'w', -1, 'utf-8')

if newFile:
    print('файл "' + filename + '"' + ' успешно скопирован!')
    print('новое имя файла - "' + newFileName + '"')
    # print(str(newFile.write(file.read())) + ' байт скопировано')

# if method.lower() == ('y' or 'yes' or 'да'):
# backupFile = open(newFileName)
with filename as string:
    print(string.read())


file.close()
newFile.close()
