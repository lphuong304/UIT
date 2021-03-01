from decimal import *
F=float(input())
C=float(( F - 32.0 ) *(5.0/9.0))
K= 273.15 + ((F - 32.0) * (5.0/9.0))
getcontext().prec=6
print(Decimal(C).normalize(),Decimal(K).normalize())