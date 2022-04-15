#perf = int(input("Digite um número para verificarmos se ele é perfeito: "))


#n = int(input("Enter any number: "))
#um1 = 0
#for i in range(1, n):
#    if(n % i == 0):
#        sum1 = sum1 + i
#if (sum1 == n):
#    print("The number is a Perfect number!")
#else:
#    print("The number is not a Perfect number!")

num = int(input('Enter any positive integer: '))
sum1 = 0
i = 1

if num <= 0:
    print('Invalid Number.')
else:
    while(i < num):
        if num % i == 0:
            sum1 = sum1 + i
        i = i + 1
    
    if sum1 == num:
        print(num, "is a perfect number")
    else:
        print(num, "is not a perfect number")