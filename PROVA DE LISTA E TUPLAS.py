# Solicita  o usuário que digite 10 valores

valores = []
for _ in range(10):
    valor = int(input("Digite um valor: "))
    valores.append(valor)


# Separar o números pares e ímpares
pares = []
impares = []
for num in valores:
    if num % 2 ==0:
        pares.append(num)
    else:
        impares.append(num)

print(f"Números pares: {pares}")
print(f"Números ímpares (em tupla): {tuple(impares)}")

# Qunatiicar / Contar os números pares e ímpares

quantidade_pares = len(pares)
quantidade_impares = len(impares)

print(f"Quantidade de números pares: {quantidade_pares}")
print(f"Quantidade de números ímpares: {quantidade_impares}")

# Somar os números pares e ímpares

soma_pares = sum(pares)
soma_impares = sum (impares)

print(f"Soma dos números pares: {soma_pares}")
print(f"Soma dos números ímpares: {soma_impares}")


