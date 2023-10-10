from tkinter import *
from tkinter import messagebox
from tkinter.ttk import Radiobutton
from tkinter.ttk import Combobox


class Medicament:
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

    def Get_name(self):
        return self.name

    def Get_cost(self):
        return self.cost

    def Get_description(self):
        return self.description

    def Get_receipt(self):
        return self.receipt


def click():
    prix = 0
    cod = int(comb1.get())
    for i in range(len(medList)):
        if cod == medList[i].Get_code():
            messagebox.showerror('Error input', 'This code already exist! Choose another one')
            cod = 0
    nom = ten2.get()
    try:
        prix = int(ten3.get())
    except ValueError:
        try:
            prix = float(ten3.get())
        except ValueError:
            messagebox.showerror('Error input', 'The price can be an integer or a float')

    descr = ten4.get()
    recp = selected.get()
    if not cod or not nom or not prix or not descr:
        messagebox.showerror('Title', 'Fill all the blank space')
    else:
        med = Medicament(cod, nom, prix, recp, descr)
        medList.append(med)


def DeList():
    verif.set(False)
    try:
        delCod = int(ten5.get())
    except ValueError:
        messagebox.showerror('Error input', 'The code should be an integer')
        delCod = 0
    if not delCod:
        messagebox.showerror('Error', 'Fill the blank place')
    else:
        for i in range(len(medList)):
            if delCod == medList[i].code:
                del medList[i]
                verif.set(True)
                break
    v=verif.get()
    if not v:
        messagebox.showerror('Error input', 'This code doesnt exit')
    else:
        messagebox.showinfo('Success', 'The code is successfully delete! Press Show again to see the change')


def show():
    global e1, e2, e3, e4, e5
    v = verif.get()
    r=len(medList)
    if v :
        e1.grid(row=r+14, column=0, sticky=NSEW)
        e1.delete(0, END)
        e2.grid(row=r+14, column=1, sticky=NSEW)
        e2.delete(0, END)
        e3.grid(row=r+14, column=2, sticky=NSEW)
        e3.delete(0, END)
        e4.grid(row=r+14, column=3, sticky=NSEW)
        e4.delete(0, END)
        e5.grid(row=r+14, column=4, sticky=NSEW)
        e5.delete(0, END)
        verif.set(False)
    rows, cols = (len(medList), 5)
    arr = [[0] * cols] * rows
    r = 14
    for i in range(len(medList)):
        arr[i][0] = medList[i].code
        e1 = Entry(relief=GROOVE)
        e1.grid(row=r, column=0, sticky=NSEW)
        e1.insert(END, '%s' % arr[i][0])
        arr[i][1] = medList[i].name
        e2 = Entry(relief=GROOVE)
        e2.grid(row=r, column=1, sticky=NSEW)
        e2.insert(END, '%s' % arr[i][1])
        arr[i][2] = medList[i].cost
        e3 = Entry(relief=GROOVE)
        e3.grid(row=r, column=2, sticky=NSEW)
        e3.insert(END, '%s' % arr[i][2])
        arr[i][3] = medList[i].receipt
        e4 = Entry(relief=GROOVE)
        e4.grid(row=r, column=3, sticky=NSEW)
        e4.insert(END, '%s' % arr[i][3])
        arr[i][4] = medList[i].description
        e5 = Entry(relief=GROOVE)
        e5.grid(row=r, column=4, sticky=NSEW)
        e5.insert(END, '%s' % arr[i][4])
        r += 1

def hidespec():
    r=14
    rows, cols = (len(medList), 5)
    arr = [[0] * cols] * rows
    for i in range(len(medList)):
        if not medList[i].receipt:
            arr[i][0] = medList[i].code
            e1 = Entry(relief=GROOVE)
            e1.grid(row=r, column=0, sticky=NSEW)
            e1.insert(END, '%s' % arr[i][0])
            arr[i][1] = medList[i].name
            e2 = Entry(relief=GROOVE)
            e2.grid(row=r, column=1, sticky=NSEW)
            e2.insert(END, '%s' % arr[i][1])
            arr[i][2] = medList[i].cost
            e3 = Entry(relief=GROOVE)
            e3.grid(row=r, column=2, sticky=NSEW)
            e3.insert(END, '%s' % arr[i][2])
            arr[i][3] = medList[i].receipt
            e4 = Entry(relief=GROOVE)
            e4.grid(row=r, column=3, sticky=NSEW)
            e4.insert(END, '%s' % arr[i][3])
            arr[i][4] = medList[i].description
            e5 = Entry(relief=GROOVE)
            e5.grid(row=r, column=4, sticky=NSEW)
            e5.insert(END, '%s' % arr[i][4])
        r += 1


window = Tk()

window.geometry('900x700')
selected = BooleanVar()
selected.set(False)
medList = []
verif = BooleanVar()

lb = Label(window, text="Information's card ", fg='red', font=('Times New Roman Bold', 18))
lb.grid(column=1, row=0)
l1 = Label(window, text="Code of the medicine ", font=('Times New Roman', 14))
l2 = Label(window, text="Name of the medicine ", font=('Times New Roman', 14))
l3 = Label(window, text="Price of the medicine ", font=('Times New Roman', 14), )
l4 = Label(window, text="Description  ", font=('Times New Roman', 14))
l5 = Label(window, text=" ", font=('Times New Roman', 14))
l6 = Label(window, text="Enter the code of the medicine to delete", font=('Times New Roman', 14))

l1.grid(column=0, row=1)
l2.grid(column=0, row=3)
l3.grid(column=0, row=5)
l4.grid(column=0, row=7)
l5.grid(column=0, row=9)
l6.grid(column=3, row=10)
comb1 = Combobox(window)
comb1['values'] = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20)
comb1.current(0)
ten2 = Entry(window, width=20, bd=3, justify=LEFT)
ten3 = Entry(window, width=20, bd=3, justify=LEFT)
ten4 = Entry(window, width=20, bd=3, justify=LEFT)
ten5 = Entry(window, width=20, bd=3, justify=LEFT)
rad1 = Radiobutton(window, text='Need receipt', value=True, variable=selected)
rad2 = Radiobutton(window, text="Don't need receipt", value=False, variable=selected)
comb1.grid(column=0, row=2)
ten2.grid(column=0, row=4)
ten3.grid(column=0, row=6)
ten4.grid(column=0, row=8)
ten5.grid(column=3, row=11)
rad1.grid(column=0, row=10)
rad2.grid(column=1, row=10)
btn = Button(window, text='Add new medicine', command=click)
btn1 = Button(window, text='Show list', command=show)
btn2 = Button(window, text='Delete', command=DeList)
btn3 = Button(window, text='Show medicine', command=hidespec)
btn.grid(column=0, row=11)
btn1.grid(column=1, row=12)
btn2.grid(column=4, row=11)
btn3.grid(column=2, row=12)

window.mainloop()
