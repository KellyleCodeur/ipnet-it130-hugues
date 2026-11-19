u=-3
n=int( input("Donner n="))
for k in range(n):
    print("u(",k,")=", u)
    u = (3 + u) / 2

from math import *
# Definition de la suite (Un)
# Terme U_n = 1/0! + 1/1! + ... + 1/n!
def u(n):
    return sum(1/factorial(k) for k in range(n+1) )

# Definition de la suite (Vn)
# Terme V_n = U_n + 1/(n!n)
def v(n):
    return u(n)+1/(factorial(n)*n)




