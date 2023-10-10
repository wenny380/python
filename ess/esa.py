from tkinter import *
from tkinter import filedialog
import csv

def saveAs():
    file_name=filedialog.asksaveasfile(title='Save File', filetypes=(("CSV files", "*.csv"),("All Files","*.*")))
    file_name=file_name.name
    if file_name:
        if file_name.endswith(".csv"):
            pass
        else:
            file_name=f'{file_name}.csv'
    print(file_name)
    myFile= open(file_name, "w+", newline="")
    writeIn=csv.writer(myFile, delimiter=';')
    writeIn.writerows(medList)
    myFile.close()



window = Tk()

window.geometry('1000x700')
selected = BooleanVar()
selected.set(False)
medList = [["Tom",28],["Alice",23], ["Bob",34]]
my_f=open('file.csv',"w+", newline="")
print("The file is open")
w=csv.writer(my_f, delimiter=';')
w.writerows(medList)
print("The data are save")
my_f.close()
menu= Menu(window)
newFunc= Menu(menu)
newFunc.add_command(label='New')
newFunc.add_separator()
newFunc.add_command(label='Open')
newFunc.add_separator()
newFunc.add_command(label='Save')
newFunc.add_separator()
newFunc.add_command(label='Save as', command=saveAs)

menu.add_cascade(label='FILE', menu=newFunc)

newFunc1= Menu(menu)
newFunc1.add_command(label='About')
menu.add_cascade(label='About the program', menu=newFunc1)
window.config(menu=menu)

output_file = open(file_name, "r")
readIn = csv.reader(output_file)
for item in readIn:
    for i in item:
        cod = i[0].split(";")
        n=i[1]
        print("Name= ",n)
        nom = i[1].split(";")
        price =i[2].split(";")
        rec = i[3].split(";")
        descr = i[4]
        med1 = Medicament(cod, nom, price, rec, descr)
        print(item)
        med1.show()
        medList.append(i)



window.mainloop()