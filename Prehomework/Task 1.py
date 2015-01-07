pupil_1 = input("Please enter the name of the first student: ")
pupil_2 = input("Please enter the name of the second student: ")
pupil_3 = input("Please enter the name of the third student: ")
pupil_4 = input("Please enter the name of the fourth student: ")
pupil_5 = input("Please enter the name of the fifth student: ")
pupil_6 = input("Please enter the name of the six student: ")
pupil_7 = input("Please enter the name of the seventh student: ")
pupil_8 = input("Please enter the name of the eight student: ")
print()
test = False

print("1. {0}".format(pupil_1))
print("2. {0}".format(pupil_2))
print("3. {0}".format(pupil_3))
print("4. {0}".format(pupil_4))
print("5. {0}".format(pupil_5))
print("6. {0}".format(pupil_6))
print("7. {0}".format(pupil_7))
print("8. {0}".format(pupil_8))
print("0. Exit Program")
print()

while test == False:
    edit = int(input("Please select a student to edit: "))
    if edit == 1:
        pupil_1 = input("Please select a student to edit: ")
        test = True
    elif edit == 2:
        pupil_2 = input("Please select a student to edit: ")
        test = True
    elif edit == 3:
        pupil_3 = input("Please select a student to edit: ")
        test = True
    elif edit == 4:
        pupil_4 = input("Please select a student to edit: ")
        test = True
    elif edit == 5:
        pupil_5 = input("Please select a student to edit: ")
        test = True
    elif edit == 6:
        pupil_6 = input("Please select a student to edit: ")
        test = True
    elif edit == 7:
        pupil_7 = input("Please select a student to edit: ")
        test = True
    elif edit == 8:
        pupil_8 = input("Please select a student to edit: ")
        test = True
    else:
        print("You have entered an invalid number, please try again")
