while True:
    sym = input("Enter a symbol (+, -, *, /) or 'q' to quit: ")
    if sym.lower() == 'q':
        print("Exiting calculator...")
        break

    num1 = int(input("Enter number 1: "))
    num2 = int(input("Enter number 2: "))

    if sym == "+":
        print("Result:", num1 + num2)
    elif sym == "-":
        print("Result:", num1 - num2)
    elif sym == "*":
        print("Result:", num1 * num2)
    elif sym == "/":
        if num2 != 0:
            print("Result:", num1 / num2)
        else:
            print("Error: division by zero!")
    else:
        print("Invalid symbol! Use +, -, *, /")
