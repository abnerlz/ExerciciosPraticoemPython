x = y = Calculadora = None
while Calculadora !=5:
    print("Selecione uma das opções a seguir: 1. SOMAR / 2. SUBTRAIR / 3. MULTIPLICAR / 4. DIVISÃO / 5. SAIR")
    Calculadora=int(input("DIGITE O NUMERO CORRESPONDEDO AS ALTERNATIVAS\n"))
    if Calculadora !=5:
        x=int(input("PRIMEIRO NUMERO : "))
        y=int(input("SEGUNDO NUMERO : "))
        match Calculadora:
            case 1:
                print(x+y)
            case 2:
                print(x-y)
            case 3:
                print(x*y)
            case 4:
                if y != 0:
                    print(x / y)
                else:
                    print("ERROO......... Divisão por zero não permitida")
    else:
        print("ERRO... TENTE NOVAMENTE")
        break