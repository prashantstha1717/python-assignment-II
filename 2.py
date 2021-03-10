# 2. Write an if statement to determine whether a variable holding a year is a leap year

def leap_year(year):
    if year % 400 == 0:
        return f'{year} is a leap year.'
    if year % 100 == 0:
        return f'{year} is a not leap year.'
    if year % 4 == 0:
        return f'{year} is a leap year.'
    else:
        return f'{year} is a not leap year.'


check = int(input('Input the year: '))
print(leap_year(check))
