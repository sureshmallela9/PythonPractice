def findMax(num1, num2, num3):
    return max(num1, num2, num3)

print(findMax(2, 5, 2))

def manualWays(num1, num2, num3):
    if num1 > num2 and num1 > num3:
        return num1
    elif num2 > num3:
        return num2
    else:
        return num3

print(manualWays(2, 5, 2))

