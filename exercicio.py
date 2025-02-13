def message(X):
    print("Aula sobre", X)
X="funções em Python"
message(X)
print("__"*50)

def calcularArea(altura,largura):
    return altura*largura
print(calcularArea(8,5))
print("___"*50)

def maioral(num1,num2):
    if num1>num2:
        print("Numero primario maior que o secundario")
    elif num1<num2:
        print("Numero secundario maior que o primario")
    else:
        print("Valores iguais") 
    return num1 and num2
maioral(8,4)
maioral(4,4)
maioral(4,8)
print("___"*50)

def ValorIMC(peso,alt):
    ValorIMC=float(peso/(alt*alt))
    if ValorIMC<=18.5:
        print("Classificação: MAGREZA | Obesidade: 0")
    elif ValorIMC>=18.5 and ValorIMC<24.9:
        print("Classificação: NORMAL | Obesidade: 0")
    elif ValorIMC>=25 and ValorIMC<29.9:
        print("Classificação: SOBREPESO | Obesidade: 1")
    elif ValorIMC>=30 and ValorIMC<39.9:
        print("Classificação: OBESIDADE | Obesidade: 2")
    else:
        print("Classificação: OBESIDADE GRAVE | Obesidade: 3")
ValorIMC(51.0,1.68)
ValorIMC(64,1.75)