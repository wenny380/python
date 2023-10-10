import socket

sock= socket.socket()
sock.bind(('', 3333))
sock.listen(1)
conn, addr=sock.accept()

print('Connected:', addr)
while True:
    data = conn.recv(1024)
    if not data:
        break
    str_r=(str(data.decode('utf-8')))

    print('La phrase recu: ', str_r)
    num=[]
    operand=[]

    operation= str_r.split(',')
    for item in operation:
         print(item)
         if item.isdigit():
            num.append(item)
         else:
             operand.append(item)

    sum = int(num[0])
    i=1
    for item in operand:
        if item == "+":
            sum += int(num[i])

        else:
            sum -= int(num[i])

        i += 1
    print(sum)
    str_ret=str(sum)
    conn.send(bytes(str_ret,'utf-8'))
conn.close()
