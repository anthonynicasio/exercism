def is_armstrong_number(number):
    digits = []
    digits = get_digits(number)
    armstrong = 0
    for i in digits:
        armstrong += i ** len(digits)

    if (armstrong == number):
        return True
    else:
        return False
        
        

def get_digits(number):
    digits = []
    while number > 0:
        digits.append(number % 10)
        number //= 10
    digits.reverse()
    return digits