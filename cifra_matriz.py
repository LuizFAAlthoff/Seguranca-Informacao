lista_alfabeto = ["0", "1", "2", "3", "4", "5", "6", "7",
                 "8", "9", "A", "a", "B", "b", "C", "c",
                 "D", "d", "E", "e", "F", "f", "G", "g",
                 "H", "h", "I", "i", "J", "j", "K", "k",
                 "L", "l", "M", "m", "N", "n", "O", "o",
                 "P", "p", "Q", "q", "R", "r", "S", "s",
                 "T", "t", "U", "u", "V", "v", "W", "w",
                 "X", "x", "Y", "y", "Z", "z", "!", "?"]

def multiplicar_matrizes(matriz1, matriz2):
    resultado = [[0, 0], [0, 0]] # Inicializa a matriz resultado com zeros
    
    # Realiza a multiplicação de matrizes
    for i in range(2):  # Para cada linha da primeira matriz
        for j in range(2):  # Para cada coluna da segunda matriz
            for k in range(2):  # Para cada elemento na multiplicação
                resultado[i][j] += matriz1[i][k] * matriz2[k][j]  # Soma o produto dos elementos correspondentes
    
    return resultado

def calcular_determinante(matriz):
    # Fórmula do determinante para matriz 2x2: det = a*d - b*c
    return matriz[0][0] * matriz[1][1] - matriz[0][1] * matriz[1][0]

def calcular_inverso_multiplicativo(numero, modulo):
    # Procura um número que multiplicado pelo número original resulte em 1 módulo 65, já que a matriz identidade é 1
    for i in range(modulo): # Verifica todos os números de 0 a 64
        if (numero * i) % modulo == 1: # Se o produto do número e i módulo 65 for igual a 1, então i é o inverso multiplicativo
            return i
    return None

def calcular_matriz_inversa(matriz):
    # Calcula o determinante da matriz
    det = calcular_determinante(matriz)
    
    # Calcula o inverso multiplicativo do determinante
    det_inv = calcular_inverso_multiplicativo(det, len(lista_alfabeto))
    
    # Verifica se a matriz possui inversa
    if det_inv is None:
        raise ValueError("A matriz não possui inversa")
    
    # Calcula a matriz adjunta (transposta da matriz de cofatores)
    adj = [
        [matriz[1][1], -matriz[0][1]],  # Primeira linha da adjunta
        [-matriz[1][0], matriz[0][0]]   # Segunda linha da adjunta
    ]
    
    # Calcula a matriz inversa multiplicando a adjunta pelo inverso do determinante
    inversa = [[0, 0], [0, 0]]  # Inicializa a matriz inversa
    for i in range(2):
        for j in range(2):
            inversa[i][j] = det_inv * adj[i][j]
    
    return inversa

def texto_para_matrizes(texto):
    # Remove espaços extras
    texto = texto.strip()
    
    # Converte a string em uma lista de caracteres
    caracteres = list(texto)
    
    # Calcula quantos caracteres faltam para ser múltiplo de 4 (4 pois estamos usando matrizes 2x2)
    # Se o comprimento do texto não for múltiplo de 4, preenche com espaços
    faltam = (4 - len(caracteres)) % 4
    
    # Preenche com espaços se necessário
    caracteres += [' '] * faltam
    
    # Divide em matrizes 2x2
    matrizes = []
    for i in range(0, len(caracteres), 4):
        bloco = caracteres[i:i+4]  # Pega 4 caracteres
        linha1 = bloco[:2]         # Primeira linha da matriz 2x2
        linha2 = bloco[2:4]        # Segunda linha da matriz 2x2
        matriz = [linha1, linha2]  # Monta a matriz
        matrizes.append(matriz)    # Adiciona à lista de matrizes
        #exemplo de output: 
        # 'eu gosto de tomat' --> 
        # [

        # [
        # ['e', 'u'], 
        # [' ', 'g']
        # ], 

        # [
        # ['o', 's'], 
        # ['t', 'o']
        # ], 

        # [
        # [' ', 'd'], 
        # ['e', ' ']
        # ], 

        # [
        # ['t', 'o'], 
        # ['m', 'a']
        # ], 

        # [
        # ['t', ' '], 
        # [' ', ' ']
        # ]

        # ]
    
    # Substitui os caracteres pelos seus índices na lista_alfabeto
    for i in range(len(matrizes)):
        for j in range(len(matrizes[i])):
            for k in range(len(matrizes[i][j])):
                matrizes[i][j][k] = lista_alfabeto.index(matrizes[i][j][k])
    
    return matrizes

def criptografar_matriz(matriz, chave):
    # Multiplica a matriz pela chave
    resultado = multiplicar_matrizes(chave, matriz)
    
    # Aplica o módulo apenas no final para garantir índices válidos
    for i in range(2):
        for j in range(2):
            resultado[i][j] %= len(lista_alfabeto)
    
    return resultado

def descriptografar_matriz(matriz, chave):
    # Calcula a matriz inversa da chave
    chave_inv = calcular_matriz_inversa(chave)

    # Multiplica a matriz criptografada pela inversa da chave
    resultado = multiplicar_matrizes(chave_inv, matriz)

    # Aplica o módulo apenas no final para garantir índices válidos
    for i in range(2):
        for j in range(2):
            resultado[i][j] %= len(lista_alfabeto)
    
    return resultado

def matriz_para_texto(matrizes):
    texto = ""
    # Para cada matriz na lista
    for matriz in matrizes:
        # Para cada linha na matriz
        for linha in matriz:
            # Para cada número na linha
            for num in linha:
                # Converte o número de volta para caractere
                texto += lista_alfabeto[num]
    return texto.strip()

# Chave de criptografia (matriz 2x2)
# Esta chave foi escolhida porque tem determinante não nulo e é inversível módulo 65
chave = [[3, 2], [1, 4]]

# Solicita ao usuário a mensagem para criptografar
texto_original = input("Insira uma mensagem para ser criptografada: ")

# Processo de criptografia
# 1. Converte o texto em matrizes
matrizes = texto_para_matrizes(texto_original)
# 2. Criptografa cada matriz
matrizes_criptografadas = [criptografar_matriz(matriz, chave) for matriz in matrizes]
# 3. Converte as matrizes criptografadas em texto
texto_criptografado = matriz_para_texto(matrizes_criptografadas)

# Processo de descriptografia
# 1. Descriptografa cada matriz
matrizes_descriptografadas = [descriptografar_matriz(matriz, chave) for matriz in matrizes_criptografadas]
# 2. Converte as matrizes descriptografadas em texto
texto_descriptografado = matriz_para_texto(matrizes_descriptografadas)

# Exibe os resultados
print("\nResultados:")
print(f"Texto original: {texto_original}")
print(f"Texto criptografado: {texto_criptografado}")
print(f"Texto descriptografado: {texto_descriptografado}")
