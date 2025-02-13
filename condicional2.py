#E = AND  
#OU = OR 
#NAO = NOT
age=int(input("Qual a sua idade \n "))
habilitchoose=int(input("Digite 1 para habilitado e 2 não habilidado \n "))
habilit=habilitchoose
habilit=None

if habilitchoose==1:
    habilit=True
elif habilitchoose==2:
    habilit=False
else:
    print("valor invalido")
if age>=18 and habilit==True:
    print("Você está dentro da lei")
    print("Tem a idade correta e esta habilitado")
elif age<18:
    print("Você é menor e não pode dirigir")
elif habilit==False:
    print("Você não é habilitado")
elif habilit==True and age<18:
    print("Você é habilitado porem não tem idade suficiente")
elif habilit==False and age>=18:
    print("Você tem idade porém não está habilitada.")
#
