area = float(input("Digite aqui o tamanho em m² da área a ser pintada: "))

litro_metro = 6

tinta_lata = 18
preco_lata = 40

tinta_galao = 4
preco_galao = 25

lata_unidade = 0
galao_unidade = 0

unidade_necessaria = area // tinta_lata 

if area % tinta_lata > 0 :
	unidade_necessaria +=1
galao = area // tinta_galao

if area % tinta_galao > 0 :
	galao +=1

print(f"Voce vai precisar comprar {int(unidade_necessaria)} unidades de lata de tinta e irá custar {int(preco_lata*unidade_necessaria)}")

print("")

print(f"Voce vai precisar comprar {int(galao)} unidades de galão de tinta e irá custar {int(preco_galao*galao)}")

print("")

while area > 0 :
	area -=tinta_galao
	galao_unidade += 1
	if galao_unidade == 4 :
		area += 16
		area -= tinta_lata
		lata_unidade += 1
		galao_unidade = 0

else:
	print(f"Se você quiser comprar os dois, a melhor combinação é {galao_unidade} galão e {lata_unidade} lata de tinta, se você fizer isso você pagará {(galao_unidade*25) + lata_unidade*80}")