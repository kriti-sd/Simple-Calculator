#calculator

from allOperators import *


a = int(input("enter a:"))
b = int(input("enter b:"))
char = input("enter operator:")

if char == "+":
    print(add2(a,b))

elif char == "-":
    print(sub2(a,b))

elif char == "*":
    print(mul2(a,b))

elif char == "/":
    print(div2(a,b))

elif char == "%":
    print(mod2(a,b))

else:
    print("invalid you fool")