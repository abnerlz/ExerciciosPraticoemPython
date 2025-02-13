#Divisão para uma aparência mais bonita
print("="*100)    
#Imprimir o nome do aplicativo                                     
print("INVERTAPP")     
#Através da multiplicação da string
print("="*100)
#Utilização do input, para que o sistema possa receber os dados com o nome digitado no terminal                                        
nome=input("Digite seu nome completo:\n")
#Utilização do reverse, depois do nome inserido, de como sera o nome digitado invertido
nomeInvertido= "".join((reversed(nome)))
#Utilização do Upper, para deixar todos os caracteres maiusculos
print("Seu nome é:", nome.upper())
#Utilização do len, para verificar a quantidade de caracteres no nome digitado no terminal
print("Seu nome possui:",(nome.__len__()),"Caracteres")
#Mostra como seria o nome digitado de forma inversa através do comando anterior do reverse
print("Seu nome invertida seria:", nomeInvertido)