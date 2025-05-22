lista_alfabeto = ["0", "1", "2", "3", "4", "5", "6", "7",
                "8", "9", "A", "a", "B", "b", "C", "c",
                "D", "d", "E", "e", "F", "f", "G", "g",
                "H", "h", "I", "i", "J", "j", "K", "k",
                "L", "l", "M", "m", "N", "n", "O", "o",
                "P", "p", "Q", "q", "R", "r", "S", "s",
                "T", "t", "U", "u", "V", "v", "W", "w",
                "X", "x", "Y", "y", "Z", "z", "!", "?"]

print("\n=== Criptografia de César ===")
print("Alfabeto disponível:", "".join(lista_alfabeto))
print("\nPor favor, insira os dados solicitados:")

texto_original = input("Insira uma mensagem para ser criptografada: ")
lista_texto_original_separado = texto_original.split()
texto_criptografado = ""

valor_chave = int(input("Insira um valor inteiro para servir de chave criptográfica: "))
print(f"\nChave de criptografia: {valor_chave}")

print("\n=== Processo de Criptografia ===")
for palavra in lista_texto_original_separado:
    print(f"\nProcessando palavra: {palavra}")
    letras_palavra = list(palavra)
    letras_criptografadas = []
    for letra in letras_palavra:
        if letra in lista_alfabeto:
            posicao_original = lista_alfabeto.index(letra)
            posicao_criptografia = (posicao_original + valor_chave) % len(lista_alfabeto)
            letra_criptografada = lista_alfabeto[posicao_criptografia]
            letras_criptografadas.append(letra_criptografada)
            print(f"Letra '{letra}' (posição {posicao_original}) -> '{letra_criptografada}' (posição {posicao_criptografia})")
        else:
            letras_criptografadas.append(letra)
    palavra_criptografada = "".join(letras_criptografadas)
    texto_criptografado += palavra_criptografada + " "
texto_criptografado = texto_criptografado.strip()

print("\n=== Resultado Final ===")
print(f"Texto original: {texto_original}")
print(f"Texto criptografado: {texto_criptografado}")