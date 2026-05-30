a = int(input("Enter 1st number: "))
b = float(input("Enter 2nd number: "))

choose = input("Enter operator (+, -, *, /): ")

if choose == "+":
    result = a + b
    print("The result is:", result)

elif choose == "-":
    result = a - b
    print("The result is:", result)

elif choose == "*":
    result = a * b
    print("The result is:", result)

elif choose == "/":
    if b != 0:
        result = a / b
        print("The result is:", result)
    else:
        print("Division by zero is not allowed.")

else:
    print("Invalid operator!")