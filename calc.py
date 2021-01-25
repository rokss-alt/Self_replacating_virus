
while True:
    num1 = float(input("pirmas skaicius: "))
    op = input("zenklas: ")
    num2 = input("antras skaicius: ")
    answer = float(input("atsakymas: "))

    if num2 == "x":
        if op == '+':
            print(answer - num1)
        elif op == "-":
            print(num1 - answer)
        elif op == "*":
            print(answer / num1)
        else:
            print(num1 / answer)
