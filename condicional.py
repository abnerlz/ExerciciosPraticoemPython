#Condicional > Estrutura de decisão
# ---- IDADE -----
print("_"*50)
Idade = int(input("Digite a sua idade : "))
if Idade >=18:
    print("És qualificado para ser um maior de idade") 
else:
    print("Pequeno demais para mim filhote")
# ---- NOTAS ESCOLARES ------
nota= float(input("Qual foi a sua nota desse bimestre meu consagrado : "))
if nota>7.9:
    print("És o meu mentor, respeita os meus ensinos meu pequeno aluno")
elif nota>=7:
    print("Ta na média, OK.")
else:
    print("Ou você reprova ou você mude sua atitude repugnante")
# ---- MEDIA ANUAL ----
Nota1=float(input("Sua nota Primeira Unidade : "))
Nota2=float(input("Sua nota Segunda Unidade : "))
Nota3=float(input("Sua nota Terceira Unidade : "))
Nota4=float(input("Sua nota Quarta Unidade : "))
MediaAnual=(Nota1+Nota2+Nota3+Nota4/4)
Nota5=MediaAnual
if Nota5 >=320:
    print("Sua média foi alta demais:", Nota5, "BOM DEMAIS")
else:
    print("Ou você reprova, ou você muda de atitude estandil")
