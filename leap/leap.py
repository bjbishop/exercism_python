def is_leap_year(y):
    if y % 100 == 0 and not y % 400 == 0:
        return False
    if y % 4 == 0 or y % 400 == 0:
        return True
