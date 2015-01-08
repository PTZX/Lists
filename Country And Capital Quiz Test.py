import random
n=3
countryAndCapital = [['England', 'Austria', 'Norway', 'Czech Republic', 'Portugal',  'Denmark', 'Russia',  'Germany', 'Turkey', 'Belgium'] ,
                         ['London', 'Vienna', 'Oslo', 'Prague', 'Lisbon', 'Copenhagen', 'Moscow', 'Berlin', 'Ankara', 'Brussels']
                         ]

for count in range(n):
        userAnswer = input('{0}. What is the Capital of {1}? '.format(count+1,countryAndCapital[0][3]))
        userAnswer = userAnswer.capitalize()
        if userAnswer == countryAndCapital[1][n-1]:
                           print('Correct, The Capital of {0} is {1}.'.format(countryAndCapital[0][n-1], countryAndCapital[1][n-1]))
        elif userAnswer != countryAndCapital[1][n-1]:
            print('The Capital of {0} is {1}.'.format(countryAndCapital[0], countryAndCapital[0]))
