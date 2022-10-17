while True:

    try:
        num1 = float(input("Введите первое число: "))
        num2 = float(input("Введите второе число: "))

    except ValueError:
        print("Вы ввели не число!")

    operation = input("Введите операцию(+, -, *, /, **): ")
    result = None

    if operation == "+":
        result = num1 + num2
    elif operation == "-":
        result = num1 - num2
    elif operation == "*":
        result = num1 * num2
    elif operation == "**":
        result = num1 ** num2
    else:
        print("Вы не ввели операцию!")

    try:
        if operation == "/":
            result = num1 / num2

    except ZeroDivisionError:
        print("На ноль делить нельзя!")

    print(result)
