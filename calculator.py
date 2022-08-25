# BASIC CALCULATOR

num1 = input("ENTER FIRST NUMBER:")
num2 = input("ENTER SECOND NUMBER:")
op = input("ENTER OPERATOR:")

if op == '+':
    result = int(num1) + int (num2)
    print(result)

elif op == '-':
    result = int(num1) - int(num2)
    print(result)

elif op == '*':
    result = int(num1) * int(num2)
    print(result)

elif op == '/':
    result = int(num1) / int(num2)
    print(result)

else:
    print("Invalid operator...")

