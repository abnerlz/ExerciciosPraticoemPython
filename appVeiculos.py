'''valor=int(input("digite um número \n"))

match valor:
    case 1: 
        print("O NUMERO 1 FOI DIGITADO")
    case 2:
        print("O NUMERO 2 FOI DIGITADO")
    case _:
        print("OUTRO VALOR")'''

numeroDeRodas=int(input("DIGITE A QUANTIDADE DE RODAS \n"))
match numeroDeRodas:
    case 0:
        print("VEICULOS AQUATICOS ou UM OVNI")
    case 1:
        print("MONOCICLO")
    case 2:
        print("MOTO ou BICICLETA")
    case 4:
        print("CARRO, KOMBI, SKATE ou BICICLETA COM RODINHAS")
    case 6:
        print("CAMINHÃO PEQUENO")
    case 8 | 10 | 12:
        print("CAMINHÃO GRANDE")
    case _:
        print("DESCONHECIDO")