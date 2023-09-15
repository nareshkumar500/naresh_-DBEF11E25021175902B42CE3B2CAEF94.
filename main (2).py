# leap year

def isLeapYear(year):
  if(year % 4==0 and year % 100 !=0): 
    return True
  else:
    return False
year = 2015
if isLeapYear(year):
  print('{} is a leap year.'.format(year))
else:
  print('{} is not a leap year.'.format(year))