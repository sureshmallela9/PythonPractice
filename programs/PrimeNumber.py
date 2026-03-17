# negative numbers are not considered prime in standard mathematics because the definition of a prime number
# is an integer greater than 1 with only two positive divisors (1 and itself),

def is_prime(n):
    if n < 1:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        print("i : {}".format(i))
        if n % i == 0:
            return False
    return True

print(is_prime(14))
# value1 = 16 ** 0.5
# print(value1)
# print(int(value1))
# print(int(value1) + 1)

