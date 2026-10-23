a =float(input("Enter a number value of A: "))

operator = input("enter an a operator (+,-,*,/) : ")

b = float(input("Enter a number value of B: "))


if operator == "+":
    print("result is",a+b)
elif operator == "-":
    print("result is", a-b)
elif operator == "*":
    print("result is",a*b)
elif operator == "/":
    if b != 0:
     print("result is", a/b)
    else:
     print("division is not valid!")