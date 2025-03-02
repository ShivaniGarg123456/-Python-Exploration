a = float(input("Enter first number:"))
b = float(input("Enter second number:"))
operator =input(("Choose an operator:(+,-,*,/):"))
if operator == "+":
    result = a+b
elif operator == "-":
    result = a-b
elif operator == "*":
    result = a*b
elif operator == "/":
    if b !=0:
        result = a/b
    else:
        result = "division not possible!"
else:
    print("invalid operator!!!")
print("Result:",result)    
