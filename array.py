phoneBook = dict(
    franc="Contact \"franc\"",
    anna="Contact \"anna\"",
    andrey="Contact \"andrey\"",
    kostik="Contact \"kostik\"",
    masha="Contact \"masha\"",
    lisa="Contact \"lisa\"",
    dima="Contact \"dima\"",
    ira="Contact \"ira\"",
)

post = str(input("Кого ищем? : "))

if post in phoneBook:
    print("Контакт найден! ")
    print(phoneBook[post])
else:
    print("Контакт к сожалению не найден!")
    print("Попробуйте изменить параметры поиска")
