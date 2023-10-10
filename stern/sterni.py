import math


def calcul(listdonnees):

    if listdonnees == "c":
        print("Введите радиус")
        val1 = float(input())
        print("Площадь окружности с радиусом ",val1, "равна: " , math.pi * (val1 ** 2))

    elif listdonnees == "t":
        print("Введите основание А")
        val2 = float(input())
        print("Введите основание B")
        val3 = float(input())
        print("Введите основание Bысота")
        val4 = float(input())

        val5 = ((val2 + val3) / 2) * val4
        print("Площадь трапеции = ", val5)

    elif listdonnees == "r":
        print("Введите длину")
        val6 = float(input())
        print("Введите ширину")
        val7 = float(input())

        val8 = val6 * val7
        print("Площадь прямоугольника = ", val8)

    elif listdonnees == "e":
        return



print("Enter the elements")
myList = input().split()

result = list(map(calcul,myList))
print(result)
















































