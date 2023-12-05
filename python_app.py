def add_numbers(a, b):
    return a + b


if __name__ == "__main__":
    num1 = float(input("Gib die erste Zahl ein: "))
    num2 = float(input("Gib die zweite Zahl ein: "))
    ergebnis = add_numbers(num1, num2)
    print(f"Das Ergebnis ist: {ergebnis}")
