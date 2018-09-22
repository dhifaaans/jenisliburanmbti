#EXPERT SYSTEM
#Jenis Liburan MBTI By Nadhifa Sofia

import csv
import random

questionCounting = 0

def __questions__(filePath, _random=False) :
    global questionCounting
    avg = 0.0
    counter = 0
    try :
        file = open(filePath)
        questions = csv.reader(file)
        for question in questions :
            questionCounting += 1
            print('%d. Jawablah sesuai dengan keadaan dirimu!' % questionCounting)
            print('\t1.%s\n\t2.%s' % (question[0], question[1]))
            counter += 1
#            if _random :
#                ans = random.randint(1, 2)
#                print('Choose your option (1/2)? %d' % ans) 
#            else :
                ans = int(input('Choose your option (1/2)? '))
            avg += 1 if ans == 1 else 0
    finally :
        file.close()
    return avg / counter

def __IE__(point) :
    return 'I' if point > .5 else 'E'

def __SN__(point) :
    return 'S' if point > .5 else 'N'

def __TF__(point) :
    return 'T' if point > .5 else 'F'

def __JP__(point) :
    return 'J' if point > .5 else 'P'

def __personality__() :
    print('Jawablah sesuai dengan keadaan dirimu!')

    IE = __IE__(__questions__('question/IvsE.csv', _random=True))
    SN = __SN__(__questions__('question/SvsN.csv', _random=True))
    TF = __TF__(__questions__('question/TvsF.csv', _random=True))
    JP = __JP__(__questions__('question/JvsP.csv', _random=True))

    return IE + SN + TF + JP

def __holiday__(personality, budget) :
    holiday = ''
    try :
        file = open('question/rules.csv')
        destinations = csv.reader(file)
        for destination in destinations :
            if personality == destination[0] and budget == destination[1] :
                holiday = destination[2]
    finally :
        file.close()
    return holiday

def __budget__(cost) :
    return 'High' if cost == 1 else 'Low'

def __main__() :
    personality = __personality__()
    budget = __budget__(int(input('\nBudget?\n\t1.High\n\t2.Low\nChoose your option (1/2)? ')))
    print('Kepribadian Anda adalah %s Anda lebih cocok untuk berlibur ke %s' % (personality, __holiday__(personality, budget)))
    return 0

__main__()
