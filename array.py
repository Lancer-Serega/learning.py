phoneBook = dict(
    franc="- \"franc\"",
    anna="- \"anna\"",
    andrey="- \"andrey\"",
    kostik="- \"kostik\"",
    masha="- \"masha\"",
    lisa="- \"lisa\"",
    dima="- \"dima\"",
    ira="- \"ira\"",
)

post = str(input("Кого ищем? : "))

# result = phoneBook.get(post, 'Контакт "' + post + '" не найден!')
# print(result)

if post in phoneBook:
    print('Контакт "' + post + '" найден! ')
    print(phoneBook[post])
else:
    print('Контакт к "' + post + '" сожалению не найден!')
    print('Попробуйте изменить параметры поиска')
