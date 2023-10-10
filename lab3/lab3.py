
class medicament:
    code = 1
    name = 'paracetamol'
    cost = 1000
    receipt = True
    description = 'braise, amoxiciline'

    def __init__(self, code1, name1, cost1, receipt1, description1):
        self.code = code1
        self.name = name1
        self.cost = cost1
        self.receipt = receipt1
        self.description = description1

    def show(self):
        print(self.code, self.name, self.cost, self.receipt, self.description)

    def Get_code(self):
        return self.code

    def Get_receipt(self):
        return self.receipt

medList = []
print("1.Add information in the list\n"
      "2.Delete information \n"
      "3.Show information about all the medicine\n"
      "4.Search for all the medicine that can be sell without receipt\n"
      "Enter your choice")
c = int(input())

while c != 0:
    if c == 1:
        print("Enter the code")
        cod = int(input())
        for i in range(len(medList)):
            if cod == medList[i].Get_code():
                print("This code already exist! Choose another one")
                cod = int(input())

        print("Enter the name")
        nom = input()
        print("Enter the cost")
        prix = int(input())
        print("Enter T if the medicine can be sell without receipt and F if not ")
        verif = False
        rec = input()
        while not verif:
            if rec == 'T' or rec == 't':
                presc = True
                verif = True
            elif rec == 'F' or rec == 'f':
                presc = False
                verif = True
            else:
                print("Wrong input. Enter T or F")
                rec = input()
        print("Enter the description")
        descr = input()
        med = medicament(cod, nom, prix, presc, descr)
        medList.append(med)

    elif c == 2:
        print("Enter the code of the medicine you want to delete")
        askDel = int(input())
        for i in range(len(medList)):
            if askDel == medList[i].Get_code():
                del medList[i]
                break
            else:
                print("This object doesn't exist")

    elif c == 3:
        for i in range(len(medList)):
            medList[i].show()
            print(medList[i].code)
        print("")
    elif c == 4:
        print("The list of medicine that can be sell without receipt")
        for i in range(len(medList)):
            if not medList[i].Get_receipt():
                medList[i].show()
        print("")

    print("1.Add information in the list\n"
          "2.Delete information \n"
          "3.Show information about all the medicine\n"
          "4.Search for all the medicine that can be sell without receipt\n"
          "Enter your choice")
    c = int(input())
