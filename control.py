from os import system
from colorama import Fore, Cursor

verde = Fore.GREEN
estado = verde + Cursor.POS(10,5)+"Motor en pausa"
opcion = 'P'

while True:  
    system("cls")
    print(verde+Cursor.POS(10,0)+"Control de motor")
    print(Fore.BLUE+Cursor.POS(10,2)+"I = izquierda")
    print(Fore.RED+Cursor.POS(10,3)+"D = derecha")
    print(Fore.YELLOW+Cursor.POS(10,4)+"P = pausa")

    match opcion:
        case 'I':
            estado = verde+Cursor.POS(10,5,)+"Motor girando a la izquierda"
        case 'D':
            estado = verde+Cursor.POS(10,5)+"Motor girando a la derecha"
        case 'P':
            estado = verde+Cursor.POS(10,5)+"Motor en pausa"
        case _:
            print(Fore.LIGHTRED_EX+Cursor.POS(10,7)+"Caracter no reconocido")

    print(estado)

    opcion = input(verde+Cursor.POS(10, 6)+"Elija una opción: ")
    print(Cursor.POS(28,6)+"                       ")