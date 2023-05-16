"""
    lista com os métodos disponíveis para execução
"""
import sympy, os

# importa os métodos de integração
from integ import *

# tenta exibir as expressões de uma maneira mais bonita
# o funcionamento vai depender do ambiente de execução
sympy.init_printing()


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


def call_subs_integral() -> None:
    """
        Sumário:
            Camada de Front-End: Exibe o resultado da integral final e com o elemento u
    """
    expr_str = input("digite a expressao para integrar\n: ")
    expr: sympy.Expr = sympy.parse_expr(expr_str)

    u_expr_str = input("digite qual eh o termo u:\n")
    u_expr: sympy.Expr = sympy.parse_expr(u_expr_str)

    subs_expr, integ_u, integ_fin = subs_integral(expr, u_expr)

    print("--expressao substituida--")
    sympy.printing.pprint(sympy.Integral(subs_expr))

    print("\n--integral com u--")
    sympy.printing.pprint(integ_u + sympy.symbols("c"))

    print("\n--integral final--")
    sympy.printing.pprint(integ_fin + sympy.symbols("c"))


# encerra a aplicação retornando um código de status 0
def exit_app() -> int: return 0


# mapeia cada um dos métodos de integração 
menu = {
    1 : (call_undef_integral, "integral indefinida"),
    2 : (call_def_integral, "integral definida"),
    3 : (call_by_parts_integral, "integral por partes"),
    4 : (call_subs_integral, "integral por substituicao"),
    5 : (exit_app, "sair")
}

# exibe o menu para o usuário
def info_display() -> None: 
    menuStr = "----Calculadora de integrais----\n\n"
    keysList = list(menu.keys())

    for key in keysList:
        menuStr += str(key) + "-" + " " + menu.get(key)[1] + "\n" 

    print(menuStr)