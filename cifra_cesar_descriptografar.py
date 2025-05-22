lista_alfabeto = ["0", "1", "2", "3", "4", "5", "6", "7",
                "8", "9", "A", "a", "B", "b", "C", "c",
                "D", "d", "E", "e", "F", "f", "G", "g",
                "H", "h", "I", "i", "J", "j", "K", "k",
                "L", "l", "M", "m", "N", "n", "O", "o",
                "P", "p", "Q", "q", "R", "r", "S", "s",
                "T", "t", "U", "u", "V", "v", "W", "w",
                "X", "x", "Y", "y", "Z", "z", "!", "?"]

texto_criptografado = input("Insira a mensagem criptografada para ser descriptografada: ")
lista_texto_criptografado_separado = texto_criptografado.split()
texto_descriptografado = ""

valor_chave = int(input("Insira o valor inteiro da chave criptográfica usada: "))

for palavra in lista_texto_criptografado_separado:
    letras_palavra = list(palavra)
    for letra in letras_palavra:
        if letra in lista_alfabeto:
            posicao_criptografada = lista_alfabeto.index(letra)
            posicao_original = (posicao_criptografada - valor_chave) % len(lista_alfabeto)
            letras_palavra[letras_palavra.index(letra)] = lista_alfabeto[posicao_original]
            palavra_descriptografada = "".join(letras_palavra)
    texto_descriptografado += palavra_descriptografada + " "
texto_descriptografado = texto_descriptografado.strip()

print("Texto descriptografado: ", texto_descriptografado)