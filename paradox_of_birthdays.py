import random, datetime

def getBirthday(numBDays):
    birthdays = []
    for i in range( numBDays):
        stateOfDate = datetime.date(2000, 1, 1)
        randomNumOfDays = datetime.timedelta(random.randint(0, 364))
        birthday = stateOfDate + randomNumOfDays
        birthdays.append(birthday)
    return birthdays


def getMatch(birthdays):
    if len(birthdays) == len(set(birthdays)):
        return None
    for a, birthdayA in enumerate(birthdays):
        for birthdayB in birthdays[a + 1:]:
            if birthdayA == birthdayB:
                return birthdayA

print('''Парадокс дня рождения показывает нам, что в группе из N человек вероятность того, что у двоих из них совпадут дни рождения, на удивление велика. 
Эта программа выполняет моделирование методом Монте-Карло (то есть повторяющиеся случайные симуляции), чтобы изучить эту концепцию.
(На самом деле это не парадокс, это просто удивительный результат.)''')

MONTHS = ('Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec')

while True:
    print('Как много дней рождений я должен сгенерировать? (Максимально: 100)')
    response = input('> ')
    if response.isdecimal() and (0 < int(response) <= 100):
        numBDays = int(response)
        break
print()

print(f'Здесь {numBDays} дней рождений')
birthdays = getBirthday(numBDays)
for i, birthday in enumerate(birthdays):
    if i != 0:
        print(', ', end='')
    monthOfBirthday = MONTHS[birthday.month - 1]
    dayOfBirthday = birthday.day
    print(f'{monthOfBirthday} {dayOfBirthday}', end='')

print()
print()

match = getMatch(birthdays)
print('В этой симуляции, ', end='')
if match != None:
    monthOfBirthday = MONTHS[match.month - 1]
    dateText = f'{monthOfBirthday} {match.day}'
    print('У нескольких человек день рождения', dateText)
else:
    print('У всех людей разные дни рождения')
print()

print(f'Сейчас мы сгенерируем группы по {numBDays} человек 100_000 раз')
input('Нажмите Enter, чтобы начать моделирование')

simMatch = 0
for i in range(100_000):
    if i % 10_000 == 0:
        print('Симуляция идёт...')
    birthdays = getBirthday(numBDays)
    match = getMatch(birthdays)
    if match != simMatch:
        simMatch += 1
print('Успешно прошло 100_000 симуляций')

probability = round(simMatch / 100_000 * 100, 2)

print(f'''В 100_000 симуляций из {numBDays} человек в каждой группе день рождение совпал в {simMatch} группах.
Это означает, что в группе из {numBDays} человек шанс того, что хотя бы у двух людей день рождения в один день равен {probability}%
Скорее всего, вы думали, что % будет намного меньше)))''')