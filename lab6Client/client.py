import socket
from tkinter import *
from tkinter import messagebox


def OctToDec(value):
    try:
        return int(value, 8)
    except ValueError:
        messagebox.showerror('Error input', 'Enter only octal number')


def click():
    number1 = OctToDec(num1.get())
    print(number1, 'first number')
    number2 = OctToDec(num2.get())
    print(number2, 'second number')
    number3 = OctToDec(num3.get())
    print(number3, 'third number')
    number4 = OctToDec(num4.get())
    print(number4, 'fourth number')
    # somme= number1+number2-number3+number4
    # print(somme)
    if number1 and number2 and number3 and number4:
        numList = [number1,'+', number2,'-', number3,'+', number4]
        str_d=','.join([str(item) for item in numList])
        s.send(bytes(str_d, 'utf-8'))
        str_result=s.recv(1024)
        sum_rec=(int(str(str_result.decode('utf-8'))))
        print('The result in 10 system: ', sum_rec)
        sum_oct=oct(sum_rec)
        res= sum_oct[2:]
        print('The result in octal: ', sum_oct[2:])
        lb7 = Label(window, text=res, font=('Times New Roman', 19))
        lb7.grid(column=1, row=4)
    else:
        messagebox.showerror('Error input', 'Enter the numbers')




window = Tk()
window.geometry('700x500')

lb1 = Label(window, text='Client part', font=('Times New Roman Bold', 18))
lb1.grid(column=1, row=0)
lb2 = Label(window, text='Enter the numbers', font=('Times New Roman', 14))
lb2.grid(column=0, row=1)
num1 = Entry(window, width=10, bd=3, justify=LEFT)
num2 = Entry(window, width=10, bd=3, justify=LEFT)
num3 = Entry(window, width=10, bd=3, justify=LEFT)
num4 = Entry(window, width=10, bd=3, justify=LEFT)
num1.grid(column=0, row=2)
num2.grid(column=2, row=2)
num3.grid(column=4, row=2)
num4.grid(column=6, row=2)
lb3 = Label(window, text='+', font=('Times New Roman', 14))
lb4 = Label(window, text='-', font=('Times New Roman', 14))
lb5 = Label(window, text='+', font=('Times New Roman', 14))
lb6 = Label(window, text='THE RESULT IS: ', font=('Times New Roman', 16))
lb3.grid(column=1, row=2)
lb4.grid(column=3, row=2)
lb5.grid(column=5, row=2)
lb6.grid(column=0, row=4)

btn = Button(window, text='Send to the server', command=click)
btn.grid(column=1, row=3)

s=socket.socket()
s.connect(('localhost', 3333))
# Main code


window.mainloop()