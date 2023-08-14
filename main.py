#Matheus José de Lima Costa rm551157

listaAI = []  # Usar uma lista em vez de um conjunto
listaSom = 0

print("Digite 'real' para adicionar números reais e 'inteiro' para inteiros:")
resp = input()

while resp != 'real' and resp != 'inteiro':
    print("Opção inválida. Digite 'real' ou 'inteiro':")
    resp = input().lower()

if resp == 'real' or 'reais':
    num_set = set()
    num_set.add(0.0)
elif resp == 'inteiro' or 'inteiros':
    num_set = set()
    num_set.add(0)

print("Conjunto de números:", num_set)

while listaSom < 10:
    print("Digite um número:")
    num = input()

    try:
        if resp == 'real':
            num = float(num)
        elif resp == 'inteiro':
            num = int(num)

        listaAI.append(num)  # Adicionar o número à lista
        listaSom = sum(listaAI)

        if listaSom >= 10:
            break
    except ValueError:
        print("Entrada inválida. Digite um número válido.")

maior = max(listaAI)

if resp == "real":
    respn = "reais"
elif resp == "inteiro":
    respn = "inteiros"

print(f"você escolheu o conjunto dos números {respn}")

print(f"O maior número é {maior:.1f}" if isinstance(maior, float) else f"O maior número é {int(maior)}")

print("Aqui estão os valores digitados:")
for valor in listaAI:
    print(int(valor))

print("Soma dos valores:", listaSom)
