import sympy
import math

# importação dos métodos
from menu import menu, info_display

while(True):
    info_display()
    
    try:
        sel = int(input(": "))
        
        if sel < 0 or sel > len(menu):
            print("\nERRO: entrada invalida\n")
            continue

        if menu[sel-1]() is not None:
            break

        input("pressione qualquer tecla...")
    except ValueError as err:
        print(err)
        break