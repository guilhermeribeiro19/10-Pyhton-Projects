print("Welcome to a simple Calculator\n")


def Add(n1, n2):
    result = round((n1 + n2), 2)
    print("\nThe result is: ",result) 

def Sub(n1, n2):
    result = round((n1 - n2), 2)
    print("\nThe result is: ",result) 

def Mult(n1, n2):
    result = round((n1 * n2), 2)
    print("\nThe result is: ",result) 

def Div(n1, n2):
    result = round((n1 / n2), 2)
    print("\nThe result is: ",result) 

while True:
    print("\n\nChoose an Operation:-")
    print("1. Addition")
    print("2. Subtraction")
    print("3  Multiplication")
    print("4. Division")
    print("5. Exit")

    choice = int(input("Enter your choice: "))

    if choice == 1:
        number1 = float(input("Enter the first number: "))
        number2 = float(input("Enter the second number: "))
        value = Add(number1, number2)

    elif choice == 2:
        number1 = float(input("Enter the first number: "))
        number2 = float(input("Enter the second number: "))
        value = Sub(number1, number2)

    elif choice == 3:
        number1 = float(input("Enter the first number: "))
        number2 = float(input("Enter the second number: "))
        value = Mult(number1, number2)

    elif choice == 4:
        number1 = float(input("Enter the first number: "))
        number2 = float(input("Enter the second number: "))
        value = Div(number1, number2)

    elif choice == 5:
        print("Exiting...")
        break