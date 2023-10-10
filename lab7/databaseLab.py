import pymysql
from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from tkinter.ttk import Combobox
import numpy as np



def add():
    compo_n= ten2.get()
    nom=ten4.get()
    prix= int(ten5.get())
    recp= selected.get()

    if not compo_n or not nom or not prix:
        messagebox.showerror('Title', 'Fill all the blank space')
    else:
        addQuery= "INSERT INTO Description (`compo`) VALUES (%s) "
        values=(compo_n)
        curs.execute(addQuery, values)
        cur.commit()
        id=curs.lastrowid
        addQuery1= "INSERT INTO Medicament(`nom`,`prix`,`need_pres`,`id_descr`) VALUES (%s, %s, %s, %s)"
        values1=(nom, prix, recp, id)
        curs.execute(addQuery1, values1)
        cur.commit()
        print(id)
        if curs.rowcount>0:
            messagebox.showinfo('Success', 'Data added successfully!')
        else:
            messagebox.showinfo('Failed', 'Data not added successfully!')


def show():
    curs.execute("SELECT  Medicament.nom, Medicament.prix, Medicament.need_pres, Description.compo FROM "
                "(Medicament inner join Description on Medicament.id_descr= Description.ID_desc)")
    data=curs.fetchall()
    curs.execute("SELECT * FROM Description")
    dat=curs.fetchall()
    print(dat)
    curs.execute("SELECT * FROM Medicament")
    dat=curs.fetchall()
    print(dat)
    for item in tree.get_children():
        tree.delete(item)
    for item in data:
        medlist=np.asarray(item)
        if medlist[2]== '0':
            tree.insert(parent='', index=0, values= (medlist[0], medlist[1], "No need", medlist[3]))
        else:
            tree.insert(parent='', index=0, values= (medlist[0], medlist[1], "Need", medlist[3]))
    #print(data)

def delete():
    delname= delEntry.get()
    if not delname:
        messagebox.showerror('Title', 'Fill the blank space')
    else:
        query="DELETE FROM Medicament WHERE nom = '"+delname+"'"
        curs.execute(query)
        cur.commit()
        if curs.rowcount>0:
            messagebox.showinfo('Success', 'Data deleted successfully!')


window = Tk()
window.geometry('900x700')

cur= pymysql.connect(host='localhost', user='root', password='password', db='Pharmacie')
curs=cur.cursor()
selected = BooleanVar()
selected.set(False)

col = ('name', 'price', 'receipt', 'description')

tree = ttk.Treeview(window, columns=col, show='headings')
tree.grid(row=17, column=0, sticky='nsew')

# define headings
tree.heading('name', text='Name')
tree.heading('price', text='price')
tree.heading('receipt', text='receipt')
tree.heading('description', text='description')

tree.column("name", anchor=W, width=100)
tree.column("price", anchor=W, width=80)
tree.column("receipt", anchor=W, width=80)
tree.column("description", anchor=W, width=100)


l4 = Label(window, text="Name of the medicine ", font=('Times New Roman', 14))
l5 = Label(window, text="Price of the medicine ", font=('Times New Roman', 14), )
l6 = Label(window, text="Description  ", font=('Times New Roman', 14))
l7= Label(window, text="Need prescription", font=('Times New Roman', 14))
l8= Label(window, text="Name of the medicine to delete", font=('Times New Roman', 14))


l4.grid(column=0, row=7)
l5.grid(column=0, row=9)
l6.grid(column=0, row=11)
l7.grid(column=0, row=13)
l8.grid(column=2, row=3)


ten2 = Entry(window, width=20, bd=3, justify=LEFT)
ten4 = Entry(window, width=20, bd=3, justify=LEFT)
ten5 = Entry(window, width=20, bd=3, justify=LEFT)
delEntry = Entry(window, width=20, bd=3, justify=LEFT)

rad1 = Radiobutton(window, text='Need receipt', value=True, variable=selected)
rad2 = Radiobutton(window, text="Don't need receipt", value=False, variable=selected)


ten2.grid(column=0, row=12)
ten4.grid(column=0, row=8)
ten5.grid(column=0, row=10)
rad1.grid(column=0, row=14)
rad2.grid(column=1, row=14)

btn = Button(window, text='Add new medicine', bg='#2186C1', fg='white', command=add)
btn.grid(column=1, row=15)
btn1 = Button(window, text='Show', bg='#2186C1', fg='white', command=show)
btn1.grid(column=1, row=17)
btn2 = Button(window, text='Delete', bg='#2186C1', fg='white', command=delete)
btn2.grid(column=2, row=5)
delEntry.grid(column=2, row=4)



window.mainloop()