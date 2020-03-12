#!/usr/bin/python
#-*- coding: utf-8 -*-

import socket, os, pickle, hashlib, d_funciones
from des import DesKey

ip = ""
port = 9895

key = DesKey(b"some key")

dataConecction = (ip,port)
connectionsMax = 5

s_socket = socket.socket(socket.AF_INET,socket.SOCK_STREAM)

try:
    s_socket.bind(dataConecction)
except socket.error as ex:
    print(ex)

s_socket.listen(connectionsMax)

print("Esperando conexión ...")

s_cliente, direccion = s_socket.accept()

print("Conexión establecida ...")
print("%s : %s"%(direccion[0],direccion[1]))

establecido = True

while establecido:
    try:

        data = s_cliente.recv(82224)
        #print(data)

        d_data = key.decrypt(b'%b'%data,initial=0,padding=True)

        print("\n"+"\n")
        #print(d_data)

        print("Make file ...")
        
        makeFile = "x"
        with open(makeFile,"wb") as file:
            file.write(d_data)
            file.close()

        sizeFile = os.stat(makeFile).st_size
        
        print("Creando has ...")
        _hash = d_funciones.haser(makeFile, sizeFile)
        print(_hash)
        f = open(makeFile,"rb")
        print(hashlib.md5(f.read()).hexdigest())

        establecido = False
        s_socket.close()
    
    except socket.error:
        print("Error ...")
        establecido = False
        s_socket.close()

print("Desconectado ....")
s_socket.close()