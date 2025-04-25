import sympy as sp

# Symbolic ifoda yaratish
x = sp.symbols('x')
expression = sp.sin(x) + sp.cos(x)

# Ifodaning x ga nisbatan hosilasini hisoblash
derivative = sp.diff(expression, x)
simplified = sp.simplify(derivative)

print("Ifoda:", expression)
print("Hosila:", derivative)
print("Sodda shakl:", simplified)
