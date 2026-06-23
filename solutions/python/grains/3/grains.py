def square(number):
  #  how would you figure this out? square 1 is always 1, square 2 is 2, square 3 is 4, square 4 is 8,
 #   square 5 is 16, square 6 is 32, square 7 is 64

  #  so the first square is always 1. square 1 is 2^0, square 2 is  is 2^1 and so on
    if (number < 1 or number > 64):
        raise ValueError("square must be between 1 and 64")
    total = 2 ** (number-1)
    return total

def total():
    total = 0
    for i in range(1, 65):
        total += square(i)
    return total