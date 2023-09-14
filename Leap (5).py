￼def isLeapYearyear):
if (year ℅ 4 == 0 and year ℅ 100 !=0) or year ℅ 400 == 0:
  return True 
year = 2013
if isLeapYear(year):
  print('{} is a leap year.'.format(year))
else:
  print('{} is not a leap year.'.format(year)) 