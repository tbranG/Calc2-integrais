"""
    Arquivo para armazenamento dos métodos de integração
"""

import sympy

def undef_integral(exp: sympy.Expr) -> sympy.Expr | None:
    """
        Sumário:
            Calcula a integral indefinida da expressão se for possível
    """
    result = None
    try:
        result = sympy.integrate(exp)
    except ValueError as err:
        print(err)

    return result