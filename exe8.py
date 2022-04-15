notes = []


while True:
	note = int(input("Digite aqui suas notas: "))
	notes.append(note)
	if note == -1: break
print("Foram lidos %i valores." % len(notes))


print("Valores informados: ")
for note in notes:
	print(note)


print("Valores informados de maneira reversa: ")
notes.reverse()
for note in notes:
	print(note)


soma = 0
for note in notes:
	soma += note
print("Valores somados: ", soma)


soma /= len(notes)
print("A média dos valores é: ", soma)


up = 0
for note in notes:
	if note > soma:
		up+=1
print("A quantidade de números acima da média é: ", up)


down = 0
for note in notes:
	if note < 7:
		down+=1
print("A quantidade de números abaixo da média 7 é: ", down)