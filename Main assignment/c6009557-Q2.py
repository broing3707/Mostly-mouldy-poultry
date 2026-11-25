from sympy import *
x = Symbol('x')
nr = exp(x) - 5*(x**3) + 6*(x**2) - 4 - sin(x**2 + 3)
x0 = 0
n = 15
for i in range(n):
    x0 = (x0 - nr.subs(x, x0) / diff(nr, x).subs(x, x0)).evalf()
    print(x0)
