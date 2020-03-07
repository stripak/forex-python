from forex_python.converter import CurrencyRates
from datetime import datetime

def question():
    print('Если желаете провести конвертацию повторно, то нажмите 1.')
    print('Если желаете посмотреть историю операций, то нажмите 2.')
    print('Если желаете закончить, то нажмите 3.')
    ans = None
    fail = True
    while fail:
        ans = input()
        if ans >= '1' and ans <= '3':
            fail = False
        else:
            print('Некорректный ввод')
    return ans

def change_money(val1, val2, money, tup, history):
    c = CurrencyRates()
    if tup == ():
        a = c.convert(val1, val2, money)
        s = 'Конвертировал ' + str(money) + ' ' + val1 + ' в ' + val2
        s += ' по курсу ' + str(c.get_rate(val1, val2)) + ' и получил '
        s += str(a) + ' ' + val2
        history.append(s)
        return a
    else:
        a = c.convert(val1, val2, money, tup)
        s = 'Конвертировал ' + str(money) + ' ' + val1 + ' в ' + val2
        s += ' по курсу ' + str(c.get_rate(val1, val2, tup)) + ' и получил '
        s += str(a) + ' ' + val2
        history.append(s)
        return a

def write_data():
    year = month = day = None
    try:
        year, month, day = map(int, input().split())
    except:
        print('Данные введены неверно повторите ввод.')
        return write_data()
    if year > 2020:
        print('Данные введены неверно, повторите ввод.')
        return write_data()
    elif month < 1 or month > 12:
        print('Данные введены неверно, повторите ввод.')
        return write_data()
    elif day < 1 or day > 31:
        print('Данные введены неверно, повторите ввод.')
        return write_data()
    
    ans = str(year) + '-'
    if month < 10:
        ans += '0'
    ans += str(month) + '-'
    if day < 10:
        ans += '0'
    ans += str(day)
    return ans

def convert(history):
    c = CurrencyRates()
    print('Введите трехбуквенную аббревиатуру вылюты, которую хотите конвертировать.')
    val1 = None
    fail = True
    while fail:
        val1 = input()
        if val1 == 'exit':
            return
        try:
            c.get_rates(val1)
            fail = False
        except:
            print('Данные введены неверно повторите ввод.')

    print('Введите трехбуквенную аббревиатуру вылюты, в которую хотите перевести деньги.')

    val2 = None
    fail = True
    while fail:
        val2 = input()
        if val2 == 'exit':
            return
        try:
            c.get_rates(val1)
            fail = False
        except:
            print('Данные введены неверно повторите ввод.')

    print('Введите количество денег, которые хотите поменять.')
    money = None
    fail = True
    while fail:
        money = input()
        if money == 'exit':
            return
        try:
            money = float(money)
            fail = False
        except:
            print('Данные введены неверно повторите ввод.')

    print('Хотите ли вы обменять валюту в какую-то конкретную дату? Ответьте: yes / no.')
    answer = None
    fail = True
    while fail:
        answer = input()
        if answer == 'exit':
            return
        if answer == 'yes':
            fail = False
        elif answer == 'no':
            fail = False
        else:
            print('Не понял ваш ответ, пожалуйста, ответьте повторно.')

    if answer == 'no':
        got = change_money(val1, val2, money, (), history)
        print('В результате конвертации вы получили', got, val2)
    else:
        print('Введите: год, месяц, день.')
        data = write_data()
        date = datetime.strptime(data,"%Y-%m-%d")
        got = change_money(val1, val2, money, date, history)
        print('В результате конвертации вы получили', got, val2)


print('Здравствуйте!')
print('Сейчас вы будете направлены в режим конвертации валюты.')
print()
history = []
convert(history)
while True:
    print()
    a = question()
    if a == '1':
        print()
        convert(history)
    elif a == '2':
        print()
        for el in history:
            print(el)
    else:
        break
    
