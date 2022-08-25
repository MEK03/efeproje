# EXPONENT FUNCTİON

def exp_funct (base_number,power):
    result = 1
    for index in range(int(power)):
        result = result * int(base_number)
    return result

base = input("Enter Base Number:")
power = input("Enter Power Number:")

print(exp_funct(base,power))
