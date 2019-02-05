#!/usr/bin/python3

"""Función que muestra por la salida estándar las tablas de multiplicar"""

def tablasdemultiplicar():
    for numero1 in range(1,11):
        print ("\nTabla del " + str(numero1))
        print ("-----------")
        for numero2 in range(1,11):
            multiplicacion = numero1 * numero2
            print (str(numero1) + " por " + str(numero2) + " es " + str(multiplicacion))

tablasdemultiplicar()
