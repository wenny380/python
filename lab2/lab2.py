import math


def Operation():
    print("Enter the x value: ")
    x = int(input())
    print("Enter the n value: ")
    n = int(input())
    while n <= 0:
        print("n cannot be negative or 0\n Enter it again")
        n = int(input())

    print("Enter the y value: ")
    y = int(input())

    result = (math.sin(math.pow(x, n) + y ** (1 / n)) + ((math.exp(x ** 4) / math.cos(y)) ** (1 / 3))) ** (1 / 5)
    return result


print("Le resultat est: ", Operation())

