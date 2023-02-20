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
