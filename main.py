import sympy
import math

# importação dos métodos
import os
from menu import menu, info_display

while(True):
    info_display()
    
    try:
        sel = int(input(": "))
        inval_input = False

        if sel < 0 or sel > len(menu):
            print("\nERRO: entrada invalida")
            inval_input = True

        if not inval_input:
            if menu[sel-1]() is not None:
                break

        input("pressione qualquer tecla...")
        
        # limpando console
        os.system("cls")

    except ValueError as err:
        print(err)
        break