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


# def def_integral(exp: sympy.Expr, floor: int, ceil: int) -> tuple | None:
#     """
#         Sumário:
#             Calcula a integral definida da expressão se for possível
        
#         Retorna:
#             A integral indefinda e o resultado do teorema fundamental
#     """
#     result = None
#     try:
#         undef = sympy.integrate(exp)

#         return (undef, 0.0)
#     except ValueError as err:
#         print(err)