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


def def_integral(exp: sympy.Expr, floor: int | str, ceil: int | str) -> tuple | None:
    """
        Sumário:
            Calcula a integral definida da expressão se for possível
        
        Retorna:
            A integral indefinda e o resultado do teorema fundamental
    """
    result = None
    try:
        # tratando a entrada caso o usuário digite alguma constante. ex: pi e euler
        if type(floor) is str:
            floor = sympy.parse_expr(floor)

        if type(ceil) is str:
            ceil = sympy.parse_expr(ceil)
        # ----------------------------------------------------------------------
    
        undef = sympy.integrate(exp)
        symbols = undef.free_symbols    # recupera as variáveis
        
        val = sympy.integrate(exp, (symbols.pop(), floor, ceil))

        result = (undef, val)
    except ValueError as err:
        print(err)      
    
    return result


def by_parts_integral(exp: sympy.Expr, u: sympy.Expr, dv: sympy.Expr) -> tuple | None:
    """
        Sumário:
            Cálcula a integral indefinda por meio da integração por partes
        
        Retorna:
            A integral indefinida, o termo du e o termo v
    """
    result = None

    try:
        v = sympy.integrate(dv)
        du = sympy.diff(u)

        #parte1 da expressão: u*v
        uv = u*v

        #parte2 da expressão: integral v*du
        intg_vdu = v*du
        
        final_intg = uv - sympy.integrate(intg_vdu)
        result = (final_intg, du, v)
    except ValueError as err:
        print(err)

    return result