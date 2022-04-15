high = float(input("Digite sua altura: "))
peso = float(input("Digite aqui seu peso: "))
print("No campo abaixo, informe M para o sexo Masculino e F para o sexo feminino")
sex = input()


if sex =='M':
	kg_ideal = (72.7*high) - 58

else:
	kg_ideal = (62.1*high)-44.7

if peso > kg_ideal:
	print("Você está acima do peso")

elif peso < kg_ideal:
	print("Você está abaixo do peso")

else:
	print("Você está no peso ideal")
