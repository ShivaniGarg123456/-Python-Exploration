a = float(input("Enter first number:"))
b = float(input("Enter second number:"))
operator = input("choose an operator from given :\n 1.Addition(+)\n 2.subtraction(-)\n 3.multiplication(*)\n 4.division(/)\n")
if operator == "+":
    result = a+b
    print("Result:", round(result,2))
elif operator == "-":
    result = a-b
    print("Result:",round(result,2))
elif operator == "*":
    result = a*b
    print("Result:",round(result,2))
elif operator == "/":
    if b != 0:
        result = a/b
        print("Result:",round(result,2))
    else :
        print("Division not possible,Try again!!!")
else :
    print("invalid operator!!! please use any of given (+,-,*,/)")
