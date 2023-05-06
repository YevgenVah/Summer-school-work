from colorama import Fore, Back, Style

print(Fore.BLACK)
print(Back.CYAN)

what = input("What are we doin? (+, -, /, *): " )

print(Back.YELLOW)

from colorama import init
from colorama import Fore, Back, Style





a = float(input("print first number:"))
b = float(input("print second Number:"))


if what == "+":
    c = a + b
    print("result: " + str(c))


elif what == "-":
    c = a - b
    print("result: " + str(c))


elif what == "/":
    c = a / b
    print("result: " + str(c))


elif what == "*": 
    c = a * b
    print("result: " + str(c))   


else:
   print("chosen wrong combination!" )


input()