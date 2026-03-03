def add_func(a, b):
    return a + b

def apply_func(func, a, b):
    return func(a, b)

print(apply_func(add_func, 1, 2))