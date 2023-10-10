listDone = ["wen", '+', 12.5, 2, 1, '-', 16, "ok"]
print("Choose an option\n 1. exo1\n 2.exo2\n 3.exo3\n 4.exo4\n 5.exo5\n 6.exo6\n 7.exo7\n 8.exo8\n 9.quit")
option = int(input())
while option !=9:
    if option ==1:
        print("The list: ", listDone)
    elif option ==2:
        print("Add an element! \nEnter the element: ")
        newEl = input()
        listDone.append(newEl)
        print("The list: ", listDone)
    elif option ==3:
        print("Enter the value you want to delete: ")
        removeEl = input()
        listDone.remove(removeEl)
        print("The list with remove element: ", listDone)
    elif option == 4:
        cortege = (listDone[1::2])
        print("The cortege", cortege)
    elif option ==5:
     prodList = 1
     for i in range(len(listDone)):
         if type(listDone[i]) == int or type(listDone[i]) == float:
            prodList *= listDone[i]

     print("Le produit est: ", prodList)

    elif option ==6:
        stringMake = ' '.join([str(item) for item in listDone])
        print(stringMake)
        print("The number of operator in the string: ", len([i for i in stringMake if i in '+-:*=']))
    elif option ==7:
        print("Enter the set")
        M1 = set(map(int, input()))
        print(M1)
        M2= set(listDone)
        print(M2)
        M3= M1 &M2
        print("The intersection between the set: ", M3)
    elif option ==8:
        my_dict = dict(zip(range(len(listDone)), listDone))
        print("Mon dictionnaire \n", my_dict)
        for i in range(3):
         print(my_dict[i])
    else:
        print("Enter a valid command")
    print("Choose an option\n 1. exo1\n 2.exo2\n 3.exo3\n 4.exo4\n 5.exo5\n 6.exo6\n 7.exo7\n 8.exo8\n 9.quit")
    option = int(input())













