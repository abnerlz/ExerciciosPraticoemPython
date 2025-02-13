nome = input("Digite o seu nome: ")
print("\nEscolha uma opção:")
print("1. Tudo em maiúsculo")
print("2. Tudo em minúsculo")
print("3. Inverter o nome")
print("4. Apenas as iniciais em maiúsculo")
print("5. Contar o número de caracteres(Sem contar com os espaços inseridos no nome)")
opcao = input("Digite o número da opção desejada: ")
if opcao == "1":
    resultado = nome.upper()
elif opcao == "2":
    resultado = nome.lower()
elif opcao == "3":
    resultado = nome[::-1]
elif opcao == "4":
    resultado = nome.title()
elif opcao == "5":
    resultado = str(len(nome.replace(" ", "")))
else:
    resultado = "Erro tente novamente"
print("\nResultado:", resultado)
