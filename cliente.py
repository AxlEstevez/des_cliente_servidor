#!/usr/bin/python
#-*- coding: utf-8 -*-

import socket,os,hashlib,pickle, d_funciones
from des import DesKey

#ipServer = str(input("IP Server: "))
ipServer = "127.0.0.1"
port = 9895
hasher = hashlib.md5()
key = DesKey(b"some key")

dataConnection = (ipServer,port)

c_socket = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
c_socket.connect(dataConnection)

print("En conexión con el servidor ...")

establecido = True

while establecido:
    print("1 - Enviar archivo")
    print("2 - Cerrar conexión")
    opt = int(input("? "))
    if opt == 1:
        g_file = str(input("Ruta o archivo: "))
        
        sizeFile = os.stat(g_file).st_size

        with open(g_file, "rb") as c_message:
            buffer = c_message.read()
            c_message.close()
        
        print("Haciendo el hash ...")
        h_file = d_funciones.haser(g_file,sizeFile)
        print("Cifrando ...")
        c_file = d_funciones.encripta(key,buffer)
        #print(c_file)
        print(h_file)
        c_socket.sendall(c_file)

    elif opt == 2:
        establecido = False
        c_socket.close()

    