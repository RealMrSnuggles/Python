# A Narcissistic Number (or Armstrong Number) 
# is a positive number which is the sum of its own digits, 
# each raised to the power of the number of digits in a given base.

def narcissistic(value):
    nar = value
    count = 0
    digits = []
    while nar >= 1:
        digits.append(nar % 10)
        nar = nar // 10
        count += 1
    digits.reverse()
    test = 0
    for digit in digits:
        test = test + digit**count
    if test == value:
        return True
    else:
        return False

print(narcissistic(153))
print(narcissistic(15))