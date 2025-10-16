def equilateral(sides):
    a = sides[0]
    b = sides[1]
    c = sides[2]
    all_sides_same_length = a == b == c
    return is_triange(sides) and all_sides_same_length


def isosceles(sides):
    a = sides[0]
    b = sides[1]
    c = sides[2]
    at_least_two_sides_same_length = a == b or a == c or b == c
    return is_triange(sides) and at_least_two_sides_same_length


def scalene(sides):
    a = sides[0]
    b = sides[1]
    c = sides[2]
    different_lengths = a != b and b != c and a != c
    return is_triange(sides) and different_lengths

def is_triange(sides):
    a = sides[0]
    b = sides[1]
    c = sides[2]
    if (a == 0 and b == 0 and c == 0):
      return False
    
    return (a + b >= c) and (b + c >= a) and (a + c >= b)
