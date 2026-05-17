a ={'a', 'b', 'c'}
b = {1, 2, 3}

# dict comprehension

d = {k:v for k,v in zip(a,b)}
print(d)