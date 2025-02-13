names1=("Abner Lucas O. de Souza")
names2=("João Paulo B. Francisco")
print(names1,"||", names2)
#Mostrar numeros de caracteres > len ou __len__
caracteres= len(names1)
print(caracteres)
#OU
print(names2.__len__())
#SOMAR A QUANTIDADE DE CARACTERES
print(names1.__len__()+(names2.__len__()))
print("-----------------------------------")
#TEXTO EXEMPLO
txt=("frase totalmente aleatorio.")
print(txt)
print(txt.__len__())

paragrafo1='abcdefghijklmnopqrstuvwxyz'
paragrafo2="aeiou"
alfabetoInvertido=sorted(paragrafo1,reverse=True)
vogaisInvertidas=sorted(paragrafo2, reverse=True)

#NONE - Um valor que está prestes a ser definido #  ::-1 Inverter string #  sorted() > criar uma lista ordenada, reverse > inverte a lista
print(paragrafo1.__len__())
print(paragrafo2.__len__())
print("--------------------------")
print(paragrafo1)
print(paragrafo1[::-1])
print("---------------------")
print(alfabetoInvertido)
print(vogaisInvertidas)
print("---------------------")