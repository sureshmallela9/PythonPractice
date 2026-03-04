def func(x):
    x = x * 2
    print("x : {}", format(x))
    return x

def func2(b):
    b.append("D")
    return b
x = 6
value1 = func(x)
k = ["S"]
value2 = func2(k)

print(x) #Immutable objects (like integers, strings, tuples) cannot be altered in place. Reassigning them inside the function only changes the local reference, not the original object.
print(value1)

print(k) #Mutable objects (like lists, dictionaries, sets) can be changed inside the function, and those changes will be visible outside.
print(value2)