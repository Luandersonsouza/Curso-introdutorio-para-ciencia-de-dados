m = int(input("Digite o valor de m: "))
for n in range ( 1, m+1):
    soma, inicio = 0,1
    while soma != n*n*n:
        soma = 0
        for i in range(n):
            soma = soma + inicio + 2*i
        inicio += 2

    inicio = inicio - 2
    print("%d*%d*%d = " % (n,n,n))
    for i in range(n):
        print("+", inicio+2*i)
    print("n")