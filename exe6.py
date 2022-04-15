num = 56
chutes = 0

while True:
	chute = int(input("Digite o número que irá chutar: "))
	chutes +=1

	if chute < num:
		print("Você deve chutar mais alto!")
		print("Seu chute: ",chute)


	elif chute > num:
		print("Você deve chutar mais baixo!")
		print("Seu chute: ",chute)


	else:
		print("Parabéns você acertou!")
		print("Você chutou", chutes, "vezes")
		break
