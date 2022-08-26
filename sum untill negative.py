# SUM INPUTTED VALUES UNTILL A NEGATİVE VALUE IS INPUTTED
sum = 0
number = input("Enter a number:")
while int (number) > 0:
    sum = sum + int(number)
    number = input("Enter a number:")

print(sum)