def countOvels(a):
 list = [1 for char in a if char.lower() in 'aeiou']
 return sum(list)

print(countOvels("suresh mallela"))

