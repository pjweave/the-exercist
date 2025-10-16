def leap_year(year):
    divisible_by_four = year % 4 == 0
    divisble_by_hundred = year % 100 == 0
    divisible_by_four_hundred = year % 400 == 0
    return (divisible_by_four and (divisble_by_hundred and divisible_by_four_hundred)) or (divisible_by_four and not divisble_by_hundred)
