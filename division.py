def division(a, b):
    try:
        return a / b
    except ZeroDivisionError:
        raise ZeroDivisionError("Vous ne pouvez pas diviser par 0.")
