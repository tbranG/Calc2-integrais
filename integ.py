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
            Calcula a integral indefinda por meio da integração por partes
        
        Retorna:
            A integral indefinida, o termo du e o termo v
    """
    result = None

    try:
        # checa se u e dv existem na expressão
        # caso não existam, a definição das partes está incorreta
        if (str(u) not in str(exp)) or (str(dv) not in str(exp)):
            raise ValueError("ERRO: Definição inválida de u e dv")

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


def subs_integral(exp: sympy.Expr, u: sympy.Expr) -> tuple | None:
    """
        Sumário:
            Calcula a integral indefinida por meio da integração por substituição

        Retorna:
            A integral indefinida com o termo u, o resultado com o termo u e o resultado final 
    """
    result = None

    try:
        # checa se o termo u existe na expressão
        # caso não exista, a definição do termo de substituição está incorreta
        if(str(u) not in str(exp)):
            raise ValueError("ERRO: Termo u inválido")

        du: sympy.Expr = 1/sympy.diff(u)
        subs_expr = exp.subs(u, sympy.symbols('u'))*du

        integ_u = sympy.integrate(subs_expr)
        integ_fin = integ_u.subs(sympy.symbols('u'), u)

        result = (subs_expr, integ_u, integ_fin)
    except ValueError as err:
        print(err)
    
    return result