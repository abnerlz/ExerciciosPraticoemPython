listaDeNumeros = [100, 80, 2, 60] 

print(listaDeNumeros) #INDEX 0 - [0, 1, 2, 3]
print(listaDeNumeros[2])
print("---------------------------------------------------------------------------------------")

#SOME OS 2 PRIMEIROS NUMEROS DA LISTA= 45
print(listaDeNumeros[0]+listaDeNumeros[1])

#SOME O PRIMEIRO E O ÚLTIMO NUMERO DA LISTA= 75
print(listaDeNumeros[0]+listaDeNumeros[3])
print("---------------------------------------------------------------------------------------")

#ADICIONANDO ITENS NA LISTA
listaDeNumeros.append(75)
listaDeNumeros.append(90)
listaDeNumeros.append(105)

print(listaDeNumeros)

#REMOVENDO ITENS DA LISTA
listaDeNumeros.remove(90)
print(listaDeNumeros)

#LIMPAR A LISTA

#listaDeNumeros.clear()
#print(listaDeNumeros)

#INVERTER A LISTA
listaDeNumeros.reverse()
print(listaDeNumeros)

#LISTA NA ORDEM CRESCENTE
listaDeNumeros.sort()
print(listaDeNumeros)

#LISTA NA ORDEM DECRESCENTE
listaDeNumeros.sort(reverse=True)
print(listaDeNumeros)

#TROCAR 1 ITEM DA POSIÇÃO

listaDeNumeros[0]=60
print(listaDeNumeros)

