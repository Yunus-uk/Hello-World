def check_leap_year(year):
  is_leap_year = False
  if year % 4 == 0:
    print(is_leap_year)


try:
  check_leap_year(2018)
  print(is_leap_year)
  # The variable is_leap_year is declared inside the function
except:
  print('Your code raised an error!')