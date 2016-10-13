### Calculate
x = float(input('Press first number: '))
math = input('Press operand: ')
y = float(input('Press second number: '))
result = None

if math == '+':
    result = x + y

elif math == '-':
    result = x - y

elif math == '*':
    result = x * y

elif math == '/':
    try:
        if (math is 0):
            raise ZeroDivisionError

        result = x / y

    except ZeroDivisionError:
        print('Деление на ноль запрещено!')

else:
    print('Please to press IN(+-*/)')
if result is not None:
    print(result)
    ### End Calculate

    # print("""Я бы не хотел никогда услышать, как он говорит: '''Она сказала: "Он сказал: 'Дай мне двести рублей'"'''""")
