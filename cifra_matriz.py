lista_alfabeto = ["0", "1", "2", "3", "4", "5", "6", "7",
                "8", "9", "A", "a", "B", "b", "C", "c",
                "D", "d", "E", "e", "F", "f", "G", "g",
                "H", "h", "I", "i", "J", "j", "K", "k",
                "L", "l", "M", "m", "N", "n", "O", "o",
                "P", "p", "Q", "q", "R", "r", "S", "s",
                "T", "t", "U", "u", "V", "v", "W", "w",
                "X", "x", "Y", "y", "Z", "z", "!", "?", " "]

texto = input("Insira uma mensagem para ser criptografada: ")

# Converte a string em uma lista de caracteres (ex: ['H', 'e', 'l', 'l', 'o'])
caracteres = list(texto)

# Calcula quantos caracteres faltam para ser múltiplo de 4 (pois usaremos matrizes 2x2)
faltam = (4 - len(caracteres)) % 4

# Preenche com espaços se necessário (ex: ['H', 'e', 'l', 'l', 'o', ' ', ' ', ' '])
caracteres += [' '] * faltam

# Divide em matrizes 2x2 (ex: [ [['H', 'e'], ['l', 'l']],
#                               [['o', ' '], [' ', ' ']]])
matrizes = []
for i in range(0, len(caracteres), 4):
    bloco = caracteres[i:i+4]  # Pega 4 caracteres
    linha1 = bloco[:2]         # Primeira linha da matriz 2x2
    linha2 = bloco[2:4]        # Segunda linha da matriz 2x2
    matriz = [linha1, linha2]  # Monta a matriz
    matrizes.append(matriz)    # Adiciona à lista de matrizes

# substitui os caracteres por seus índices na lista do alfabeto
# Exemplo: 'H' -> 33, 'e' -> 34, 'l' -> 37, 'o' -> 40
# [['H', 'e'], ['l', 'l']] -> [[33, 34], [37, 37]]
# [['o', ' '], [' ', ' ']] -> [[40, 64], [64, 64]]
# Substitui os caracteres pelos seus índices na lista_alfabeto

for i in range(len(matrizes)):            # Para cada matriz
    for j in range(len(matrizes[i])):     # Para cada vetor (linha) na matriz
        for k in range(len(matrizes[i][j])):  # Para cada caractere no vetor
            matrizes[i][j][k] = lista_alfabeto.index(matrizes[i][j][k]) # Substitui o caractere pelo índice
            
# Exibe as matrizes
print("Matrizes:")
for matriz in matrizes:
    print(matriz)

