def surface(option):

    if option == 'R' or option== 'r':
        print("Enter the value of a: ")
        a = int(input())
        print("Enter the value of b: ")
        b = int(input())
        print("The surface is triangle is: ", (a * b) / 2)
    elif option == 'T' or option== 't':
        print("Entrer la grande base: ")
        b = int(input())
        print("Entrer la petite base: ")
        b1 = int(input())
        print("Entrer la hauteur: ")
        h = int(input())
        print("la surface du trapeze: ", ((b + b1) * h) / 2)
    elif option == 'S' or option == 's':
        print("Entrer le cote du carre")
        c = int(input())
        print("La surface du carre: ", c * c)
    elif option == 'E' or option == 'e':

        return
    else:
        print("There is no action for this command")


print("Choose the options\n R pour triangle rectangle\n T pour trapeze\n S pour carre\n E quitter")
GivenList = input().split()
resultat = list(map(surface, GivenList))



