n = 10

try:
    response = n/1
    print(response)
    resp = n/0
except ZeroDivisionError:
    print("can't divide by zero")
finally:
    print('Hi from finally block')