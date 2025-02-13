#REFAZER TALVEZ

num = int(input("Insira um número: \n"))
fator = 1
for i in range(1, num + 1):
    fator = fator * i
print(f"O fatorial de", num, "é", fator)