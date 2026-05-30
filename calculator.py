print("===== SIMPLE CALCULATOR =====")

num1 = float(input("Enter First Number: "))
num2 = float(input("Enter Second Number: "))

print("1. Addition")
print("2. Subtraction")
print("3. Multiplication")
print("4. Division")

choice = input("Enter Choice: ")

if choice == "1":
    print("Result =", num1 + num2)
elif choice == "2":
    print("Result =", num1 - num2)
elif choice == "3":
    print("Result =", num1 * num2)
elif choice == "4":
    if num2 == 0:
        print("Cannot divide by zero")
    else:
        print("Result =", num1 / num2)
else:
    print("Invalid Choice")
