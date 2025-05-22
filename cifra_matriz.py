lista_alfabeto = ["0", "1", "2", "3", "4", "5", "6", "7",
                 "8", "9", "A", "a", "B", "b", "C", "c",
                 "D", "d", "E", "e", "F", "f", "G", "g",
                 "H", "h", "I", "i", "J", "j", "K", "k",
                 "L", "l", "M", "m", "N", "n", "O", "o",
                 "P", "p", "Q", "q", "R", "r", "S", "s",
                 "T", "t", "U", "u", "V", "v", "W", "w",
                 "X", "x", "Y", "y", "Z", "z", "!", "?", " "]

def multiplicar_matrizes(matriz1, matriz2):
    print("\n=== Multiplicação de Matrizes ===")
    print(f"Matriz 1: {matriz1}")
    print(f"Matriz 2: {matriz2}")
    
    resultado = [[0, 0], [0, 0]] # Inicializa a matriz resultado com zeros
    
    # Realiza a multiplicação de matrizes
    for i in range(2):  # Para cada linha da primeira matriz
        for j in range(2):  # Para cada coluna da segunda matriz
            for k in range(2):  # Para cada elemento na multiplicação
                resultado[i][j] += matriz1[i][k] * matriz2[k][j]  # Soma o produto dos elementos correspondentes
                print(f"Passo {i},{j},{k}: {matriz1[i][k]} * {matriz2[k][j]} = {matriz1[i][k] * matriz2[k][j]}")
    
    print(f"Resultado da multiplicação: {resultado}")
    return resultado

def calcular_determinante(matriz):
    print("\n=== Cálculo do Determinante ===")
    print(f"Matriz: {matriz}")
    # Fórmula do determinante para matriz 2x2: det = a*d - b*c
    det = matriz[0][0] * matriz[1][1] - matriz[0][1] * matriz[1][0]
    print(f"Determinante = {matriz[0][0]} * {matriz[1][1]} - {matriz[0][1]} * {matriz[1][0]} = {det}")
    return det

def calcular_inverso_multiplicativo(numero, modulo):
    print(f"\n=== Cálculo do Inverso Multiplicativo de {numero} módulo {modulo} ===")
    # Procura um número que multiplicado pelo número original resulte em 1 módulo 65, já que a matriz identidade é 1
    for i in range(modulo): # Verifica todos os números de 0 a 64
        print(f"Testando {i}: {numero} * {i} % {modulo} = {(numero * i) % modulo}")
        if (numero * i) % modulo == 1: # Se o produto do número e i módulo 65 for igual a 1, então i é o inverso multiplicativo
            print(f"Inverso multiplicativo encontrado: {i}")
            return i
    print("Nenhum inverso multiplicativo encontrado")
    return None

def calcular_matriz_inversa(matriz):
    print("\n=== Cálculo da Matriz Inversa ===")
    print(f"Matriz original: {matriz}")
    
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
    print(f"Matriz adjunta: {adj}")
    
    # Calcula a matriz inversa multiplicando a adjunta pelo inverso do determinante
    inversa = [[0, 0], [0, 0]]  # Inicializa a matriz inversa
    for i in range(2):
        for j in range(2):
            inversa[i][j] = det_inv * adj[i][j]
            print(f"Elemento [{i},{j}] da inversa: {det_inv} * {adj[i][j]} = {inversa[i][j]}")
    
    print(f"Matriz inversa final: {inversa}")
    return inversa

def texto_para_matrizes(texto):
    print("\n=== Conversão de Texto para Matrizes ===")
    print(f"Texto original: {texto}")
    
    # Remove espaços extras
    texto = texto.strip()
    
    # Converte a string em uma lista de caracteres
    caracteres = list(texto)
    print(f"Lista de caracteres: {caracteres}")
    
    # Calcula quantos caracteres faltam para ser múltiplo de 4 (4 pois estamos usando matrizes 2x2)
    # Se o comprimento do texto não for múltiplo de 4, preenche com espaços
    faltam = (4 - len(caracteres)) % 4
    print(f"Caracteres faltando para completar o último bloco: {faltam}")
    
    # Preenche com espaços se necessário
    caracteres += [' '] * faltam
    print(f"Lista de caracteres após preenchimento: {caracteres}")
    
    # Divide em matrizes 2x2
    matrizes = []
    for i in range(0, len(caracteres), 4):
        bloco = caracteres[i:i+4]  # Pega 4 caracteres
        linha1 = bloco[:2]         # Primeira linha da matriz 2x2
        linha2 = bloco[2:4]        # Segunda linha da matriz 2x2
        matriz = [linha1, linha2]  # Monta a matriz
        matrizes.append(matriz)    # Adiciona à lista de matrizes
        print(f"\nBloco {i//4 + 1}:")
        print(f"Caracteres: {bloco}")
        print(f"Matriz: {matriz}")
    
    # Substitui os caracteres pelos seus índices na lista_alfabeto
    print("\nSubstituindo caracteres por índices:")
    for i in range(len(matrizes)):
        for j in range(len(matrizes[i])):
            for k in range(len(matrizes[i][j])):
                char = matrizes[i][j][k]
                idx = lista_alfabeto.index(char)
                matrizes[i][j][k] = idx
                print(f"Caractere '{char}' -> índice {idx}")
    
    print(f"\nMatrizes finais com índices: {matrizes}")
    return matrizes

def criptografar_matriz(matriz, chave):
    print("\n=== Criptografando Matriz ===")
    print(f"Matriz original: {matriz}")
    print(f"Chave: {chave}")
    
    # Multiplica a matriz pela chave
    resultado = multiplicar_matrizes(chave, matriz)
    
    # Aplica o módulo apenas no final para garantir índices válidos
    for i in range(2):
        for j in range(2):
            resultado[i][j] %= len(lista_alfabeto)
            print(f"Elemento [{i},{j}] após módulo: {resultado[i][j]}")
    
    print(f"Matriz criptografada: {resultado}")
    return resultado

def descriptografar_matriz(matriz, chave):
    print("\n=== Descriptografando Matriz ===")
    print(f"Matriz criptografada: {matriz}")
    print(f"Chave: {chave}")
    
    # Calcula a matriz inversa da chave
    chave_inv = calcular_matriz_inversa(chave)
    
    # Multiplica a matriz criptografada pela inversa da chave
    resultado = multiplicar_matrizes(chave_inv, matriz)
    
    # Aplica o módulo apenas no final para garantir índices válidos
    for i in range(2):
        for j in range(2):
            resultado[i][j] %= len(lista_alfabeto)
            print(f"Elemento [{i},{j}] após módulo: {resultado[i][j]}")
    
    print(f"Matriz descriptografada: {resultado}")
    return resultado

def matriz_para_texto(matrizes):
    print("\n=== Convertendo Matrizes para Texto ===")
    print(f"Matrizes: {matrizes}")
    
    texto = ""
    # Para cada matriz na lista
    for i, matriz in enumerate(matrizes):
        print(f"\nProcessando matriz {i+1}:")
        # Para cada linha na matriz
        for j, linha in enumerate(matriz):
            # Para cada número na linha
            for k, num in enumerate(linha):
                # Converte o número de volta para caractere
                char = lista_alfabeto[num]
                texto += char
                print(f"Índice {num} -> caractere '{char}'")
    
    print(f"\nTexto final: {texto}")
    return texto.strip()

def processar_primeiros_caracteres(texto):
    print("\n=== Processando Primeiros 4 Caracteres ===")
    print(f"Texto original: {texto}")
    
    # Pega apenas os 4 primeiros caracteres
    texto = texto[:4]
    print(f"Primeiros 4 caracteres: {texto}")
    
    # Preenche com espaços se necessário
    while len(texto) < 4:
        texto += " "
    print(f"Texto após preenchimento: {texto}")
    
    # Converte para matriz 2x2
    matriz = [
        [lista_alfabeto.index(texto[0]), lista_alfabeto.index(texto[1])],
        [lista_alfabeto.index(texto[2]), lista_alfabeto.index(texto[3])]
    ]
    print(f"Matriz convertida: {matriz}")
    
    # Tenta calcular a matriz inversa
    try:
        print("\nTentando calcular a matriz inversa...")
        inversa = calcular_matriz_inversa(matriz)
        print("Matriz tem inversa! Usando a matriz como chave.")
        return matriz
    except ValueError:
        print("Matriz não tem inversa. Usando chave padrão [[3,2],[1,4]]")
        return [[3, 2], [1, 4]]

# Menu principal
print("\n=== Criptografia com Matrizes ===")

# Solicita ao usuário a mensagem para criptografar
texto_original = input("Insira uma mensagem para ser criptografada: ")

# Solicita ao usuário a chave criptográfica
chave_texto = input("Insira uma chave criptográfica (serão usados os primeiros 4 caracteres): ")

# Processa a chave
chave = processar_primeiros_caracteres(chave_texto)
print("\nChave que será utilizada:", chave)

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
print("\n=== Resultados Finais ===")
print(f"Texto original: {texto_original}")
print(f"Texto criptografado: {texto_criptografado}")
print(f"Texto descriptografado: {texto_descriptografado}")