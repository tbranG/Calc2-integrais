"""
    lista com os métodos disponíveis para execução
"""
import sympy, os

# importa os métodos de integração
from integ import *

# tenta exibir as expressões de uma maneira mais bonita
# o funcionamento vai depender do ambiente de execução
sympy.init_printing()

# definindo símbolo padrão como x
# x = sympy.Symbol("x")


# header do menu
def info_display() -> None: print("""
    ----Calculadora de integrais----
1- integral indefinida
2- integral definida
3- integral por partes
4- sair
""")


def call_undef_integral() -> None:
    """
        Sumário:
            Camada de Front-End: Exibe o resultado de uma integração indefinida
    """
    expr_str = input("digite a expressao para integrar\n: ")
    expr: sympy.Expr = sympy.parse_expr(expr_str)

    print("\t----Resultado----\n")
    expr2 = undef_integral(expr) + sympy.symbols("c")
    sympy.printing.pprint(expr2)
    print("\t-----------------")


def call_def_integral() -> None:
    """
        Sumário:
            Camada de Front-End: Exibe o resultado de uma integração definida
    """
    expr_str = input("digite a expressao para integrar\n: ")
    expr: sympy.Expr = sympy.parse_expr(expr_str)

    floor = input("digite o limite inferior\n: ")
    ceil = input("digite o limite superior\n: ")

    undf, res = def_integral(expr, floor, ceil)
    
    print("\t----Resultado----\n")
    print("primitiva:", end="\n")
    sympy.printing.pprint(undf)
    
    print("teorema:\n", end="\n")
    subsExpr: sympy.Expr = sympy.Subs(undf, undf.free_symbols.pop(), ceil) - sympy.Subs(undf, undf.free_symbols.pop(), floor)
    sympy.printing.pprint(subsExpr)
    print("\n")
    print("resultado:", end="\n")
    print(f"{res}\n")
    print("\t-----------------")


def call_by_parts_integral() -> None:
    """
        Sumário:
            Camada de Front-End: Exibe o resultado da integral e os elementos du e v
    """
    expr_str = input("digite a expressao para integrar\n: ")
    expr: sympy.Expr = sympy.parse_expr(expr_str)

    u_expr_str = input("digite qual eh o termo u:\n")
    u_expr: sympy.Expr = sympy.parse_expr(u_expr_str)

    dv_expr_str = input("digite qual eh o termo dv:\n")
    dv_expr: sympy.Expr = sympy.parse_expr(dv_expr_str)

    res_expr, du, v = by_parts_integral(expr, u_expr, dv_expr)

    os.system("cls")
    print("--termos--")
    print("du:")
    sympy.printing.pprint(du)
    print("\nv:")
    sympy.printing.pprint(v)
    print("--reescrita--")
    part_expr: sympy.Expr = u_expr*v - sympy.Integral(v*du)
    sympy.printing.pprint(part_expr) 
    print("--resultado:")
    sympy.printing.pprint(res_expr + sympy.Symbol("c"))

# encerra a aplicação retornando um código de status 0
def exit_app() -> int: return 0

# mapeia cada um dos métodos de integração 
menu = [
    call_undef_integral,
    call_def_integral,
    call_by_parts_integral,
    exit_app
]