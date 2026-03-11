def factorialNumber(n):
    print('n : {}'.format(n))
    if n == 0:
        return 1
    value = n * factorialNumber(n-1)
    # 5 * factorialNumber(4) 5 * 24 = 120
    #4 * factorialNumber(3) == 4 * 6 = 24
    #3 * factorialNumber(2) == 3 * 2 = 6
    #2 * factorialNumber(1) == 2*1 == 2
    #1 * factorialNumber(0) == 1*1
    print('value: {}, n: {}'.format(value, n))
    return value

factorialNumber(5)

#n!=n* (n-1)* (n-2)* .... * 3*2*1
#start with n, multiply by each number one less than it, keep going until you reach 1.




