__author__ = 'Leila Spini & Ignacio Pieve'
__version__ = 0.2

from sympy import *
import modulos.mensajes as msg
import modulos.tipoA as A
import modulos.tipoB as B
import modulos.tipoC as C
import os


def menu():
    opc = msg.opciones_principales()
    os.system('cls')

    if opc == 1:
        opc2 = msg.opciones_tipo_a()
        if opc2 == 1:
            retorno = A.euler()
            for a in retorno:
                print(a)
        elif opc2 == 2:
            retorno = A.euler_mejorado()
            for a in retorno:
                print(a)
        else:
            retorno = A.runge_kutta()
            for a in retorno:
                print(a)

    elif opc == 2:
        opc2 = msg.opciones_tipo_b()
        if opc2 == 1:
            retorno = B.euler()
            for a in retorno:
                print(a)
        elif opc2 == 2:
            retorno = B.euler_mejorado()
            for a in retorno:
                print(a)
        else:
            retorno = B.runge_kutta()
            for a in retorno:
                print(a)

    elif opc == 3:
        opc2 = msg.opciones_tipo_c()
        if opc2 == 1:
            retorno = C.euler()
            for a in retorno:
                print(a)
        elif opc2 == 2:
            retorno = C.euler_mejorado()
            for a in retorno:
                print(a)
        else:
            retorno = C.runge_kutta()
            for a in retorno:
                print(a)


if __name__ == '__main__':
    menu()
