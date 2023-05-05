"""
    lista com os métodos disponíveis para execução
"""
import sympy

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
2- sair
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


# encerra a aplicação retornando um código de status 0
def exit_app() -> int: return 0

# mapeia cada um dos métodos de integração 
menu = [
    call_undef_integral,
    exit_app
]