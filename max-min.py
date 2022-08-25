# FIND MAX and MIN  NUMBER IN 5 INTEGER
num = []
num.insert(0,input("Enter a number:"))
num.insert(1,input("Enter a number:"))
num.insert(2,input("Enter a number:"))
num.insert(3,input("Enter a number:"))
num.insert(4,input("Enter a number:"))

max = num[0]
min = num[0]

for i in num:
    if i > max:
        max = i
    if i < min:
        min = i

print("max value is : " + max)
print("min value is : " + min)
