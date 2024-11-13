class Error(Exception):
    pass

class DOBException(Error):
    pass

year = int(input("Enter the date of birth: "))

age = 2024-year

try:
    if 30 >= age >= 20: # same as using "and"
        print("The age appears to be valid. You may apply for the exam.")
    else:
        raise DOBException
except DOBException:
    print("The age appears to be invalid. You may not apply for the exam.")
