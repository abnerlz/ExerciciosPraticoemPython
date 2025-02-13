def fibonacci_ate(limite):
    a, b = 0, 1
    while a <= limite:
        print(a, end=' ')
        a, b = b, a + b

limite = int(input("Digite o número limite para a sequência de Fibonacci: "))
fibonacci_ate(limite)
