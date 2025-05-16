lista_alfabeto = ["0", "1", "2", "3", "4", "5", "6", "7",
                "8", "9", "A", "a", "B", "b", "C", "c",
                "D", "d", "E", "e", "F", "f", "G", "g",
                "H", "h", "I", "i", "J", "j", "K", "k",
                "L", "l", "M", "m", "N", "n", "O", "o",
                "P", "p", "Q", "q", "R", "r", "S", "s",
                "T", "t", "U", "u", "V", "v", "W", "w",
                "X", "x", "Y", "y", "Z", "z", "!", "?"]

texto_original = input("Insira uma mensagem para ser criptografada: ")
lista_texto_original_separado = texto_original.split()
texto_criptografado = ""

valor_chave = int(input("Insira um valor inteiro para servir de chave criptográfica: "))

for palavra in lista_texto_original_separado:
    letras_palavra = list(palavra)
    for letra in letras_palavra:
        if letra in lista_alfabeto:
            posicao_original = lista_alfabeto.index(letra)
            posicao_criptografia = (posicao_original + valor_chave) % len(lista_alfabeto)
            letras_palavra[letras_palavra.index(letra)] = lista_alfabeto[posicao_criptografia]
            palavra_criptografada = "".join(letras_palavra)
    texto_criptografado+= palavra_criptografada + " "
texto_criptografado.strip()

print("Texto criptografado: ", texto_criptografado)

