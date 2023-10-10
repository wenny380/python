import math

# THE FIRST EXERCISE
# print("Enter the x value: ")
# x = int(input())
# print("Enter the n value: ")
# n = int(input())
# print("Enter the y value: ")
# y = int(input())
#
# result = (math.sin(math.pow(x, n)+y**(1/n)) + ((math.exp(x**4)/math.cos(y))**(1/3)))**(1/5)
# print(result)

# THE SECOND EXERCISE
# listDone = ["wen", '+', 12.5, 2, 1, '-', 16, "ok"]
# print("The list: ", listDone)
# print("Add an element! \nEnter the element: ")
# newEl = input()
# listDone.append(newEl)
# print("The list: ", listDone)
# print("Enter the value you want to delete: ")
# removeEl = input()
# listDone.remove(removeEl)
# print("The list with remove element: ", listDone)
# cortege = (listDone[1::2])
# print("The cortege", cortege)


# prodList = 1
# for i in range(len(listDone)):
#     if type(listDone[i]) == int or type(listDone[i]) == float:
#         prodList *= listDone[i]

# print("Le produit est: ", prodList)
# stringMake = ' '.join([str(item) for item in listDone])
# print(stringMake)
# print("The number of operator in the string: ", len([i for i in stringMake if i in '+-:*=']))

# print("Enter the set")
# M1 = set(map(int, input()))
# print(M1)
# M2= set(listDone)
# print(M2)
# M3= M1 &M2
# print("The intersection between the set: ", M3)

# my_dict = dict(zip(range(len(listDone)), listDone))
# print("Mon dictionnaire \n", my_dict)
# for i in range(3):
#  print(my_dict[i])

# THE THIRD EXERCISE

print("Choose an option\n R pour triangle rectangle\n T pour trapeze\n S pour carre\n E quitter")
option = input()
while option != 'E':
    if option == 'R':
        print("Enter the value of a: ")
        A = int(input())
        print("Enter the value of b: ")
        B = int(input())
        print("The surface is: ", (A * B) / 2)
    elif option == 'T':
        print("Entrer la grande base: ")
        B = int(input())
        print("Entrer la petite base: ")
        b = int(input())
        print("Entrer la hauteur: ")
        h = int(input())
        print("la surface du trapeze: ", ((B + b) * h) / 2)
    elif option == 'S':
        print("Entrer le cote du carre")
        C = int(input())
        print("La surface du carre: ", C * C)
    else:
        print("Enter a valid command")
    print("Choose an option\n R pour triangle rectangle\n T pour trapeze\n S pour carre\n E quitter")
    option = input()