import math

def is_prime(n):
    for num in range(2, int(math.sqrt(n)) + 1):
        if n % num == 0:
            return False
    return True

def prime_factors(n):
    result = ""
    number = n
    if n == 1:
        return "(1)"
    for num in range(2, n):
        count = 0
        while number % num == 0:
            count += 1
            number = int(number / num)
        if count > 0:
            result += ("({}**{})".format(num, count) if count > 1 else "({})".format(num))
        if number == 1:
            return result
        if is_prime(number):
            result += ("({})".format(number))
            return result
    return result if result else "({})".format(n)

print(prime_factors(1245))