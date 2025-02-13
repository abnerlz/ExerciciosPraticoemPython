gastos_x= [189, 981, 402, 550, 638, 740]
gastos_y= [300, 170, 860, 921, 701, 103]
gastoMensal_x= sum(gastos_x)
gastoMensal_y= sum(gastos_y)
print("__"*20)
if gastoMensal_x > gastoMensal_y:
    print("O gastos da pessoa X foram maiores do que a de Y")
    print("X ficou com o valor de:", gastoMensal_x)
elif gastoMensal_y > gastoMensal_x:
    print("O gastos de Y foram maiores do que a de X")
    print("Y ficou com o valor de:", gastoMensal_y)
else:
    print("Ficaram com valores iguais")