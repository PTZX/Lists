##1. Write a program that stores the names of ten countries in column1
# and their capitals in column2. 
#The program should then pick a random country and ask the user for the capital.

#Display an appropriate message to the user to show whether
#they are right or wrong.
import random

print('The program picks a random country, enter its capital.')

def chooser():
    countryAndCapital = [
        ['England', 'Austria', 'Norway', 'Czech Republic', 'Portugal',  'Denmark', 'Russia',  'Germany', 'Turkey', 'Belgium']
        ['London', 'Vienna', 'Oslo', 'Prague', 'Lisbon', 'Copenhagen', 'Moscow', 'Berlin', 'Ankara', 'Brussels']]
    print(countryAndCapital)
    
    for count in range(3):
        random = rand.int[0,10]
        userAnswer = input('What is the Capital of {0}?'.format(countryAndCapital[0][random]))
        userAnswer = capitalise(userAnswer)
        if userAnswer == countryAndCapital[random]:
                           print('Correct, The Capital of {0} is {1}.'.format(countryAndCapital[0][random], countryAndCapital[1][random]))
    
	
chooser()
