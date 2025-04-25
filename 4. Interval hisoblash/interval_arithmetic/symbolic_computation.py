# interval_arithmetic/symbolic_computation.py

import sympy as sp

# Symbolic hisoblashlar va ifodalarni soddalashtirish
def symbolic_computation(expression):
    x = sp.symbols('x')
    expr = sp.sympify(expression)
    simplified_expr = sp.simplify(expr)
    derivative = sp.diff(expr, x)
    integral = sp.integrate(expr, x)

    return {
        "simplified": simplified_expr,
        "derivative": derivative,
        "integral": integral
    }
