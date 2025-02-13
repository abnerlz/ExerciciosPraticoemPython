Nota1=float(input("Sua nota Primeira Unidade : "))
Nota2=float(input("Sua nota Segunda Unidade : "))
Nota3=float(input("Sua nota Terceira Unidade : "))
MediaDasNotas=(Nota1+Nota2+Nota3/3)
Nota4=MediaDasNotas
if Nota4 >=7:
    print("Aprovado!!")
else:
    print("Reprovado!!")
print("Média:",Nota4)