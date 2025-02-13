# | DEF |  Definir uma função
def somar(a, b):
    return a + b

def subtracao(a, b):
    return a - b

def multiplicacao(a, b):
    return a * b

def dividir(a, b):
    if b == 0:
        return "Divisão por zero não é permitida. tente novamente"
    else:
        return a / b

print("O valor da soma foi >>>>>>",somar(50, 20),"\n")
print("O valor da subtração foi >>>>>",subtracao(20,10),"\n")
print("O valor da multiplicação foi >>>>>>",multiplicacao(10,5),"\n")
print("O valor da divisão foi >>>>>> ",dividir(20,0),"\n")
print("O valor da divisão foi >>>>>>",dividir(100, 4),"\n")