##1. Write a program that stores the names of ten countries in column1
# and their capitals in column2. 
#The program should then pick a random country and ask the user for the capital.

#Display an appropriate message to the user to show whether
#they are right or wrong.
import random
print('Capital Quiz: Europe Edition')
print()
def gettingTheThing():
    countryAndCapital = []
    print('The program tests you on the capital cities of Europe .')
    n= int(input('Enter the number of countries to be quizzed on: '))
    return n

def chooser(n):
    countryAndCapital = [['England', 'Austria', 'Norway', 'Czech Republic', 'Portugal',  'Denmark', 'Russia',  'Germany', 'Turkey', 'Belgium'] ,
                         ['London', 'Vienna', 'Oslo', 'Prague', 'Lisbon', 'Copenhagen', 'Moscow', 'Berlin', 'Ankara', 'Brussels']
                         ]
    print(countryAndCapital[0:3])

    for count in range(n):
        random = random.randint[0,10]
        userAnswer = input('{0}. What is the Capital of {1}? '.format(count+1,countryAndCapital[0][random]))
        userAnswer = capitalise(userAnswer)
        if userAnswer == countryAndCapital[random]:
                           print('Correct, The Capital of {0} is {1}.'.format(countryAndCapital[0][random], countryAndCapital[1][random]))
        else:
            print('The Capital of {0} is {1}.'.format(countryAndCapital[0]))
    
	
chooser()
