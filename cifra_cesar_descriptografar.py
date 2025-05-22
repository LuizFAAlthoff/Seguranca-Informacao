lista_alfabeto = ["0", "1", "2", "3", "4", "5", "6", "7",
                "8", "9", "A", "a", "B", "b", "C", "c",
                "D", "d", "E", "e", "F", "f", "G", "g",
                "H", "h", "I", "i", "J", "j", "K", "k",
                "L", "l", "M", "m", "N", "n", "O", "o",
                "P", "p", "Q", "q", "R", "r", "S", "s",
                "T", "t", "U", "u", "V", "v", "W", "w",
                "X", "x", "Y", "y", "Z", "z", "!", "?"]

print("\n=== Descriptografia de César ===")
print("Alfabeto disponível:", "".join(lista_alfabeto))
print("\nPor favor, insira os dados solicitados:")

texto_criptografado = input("Insira a mensagem criptografada para ser descriptografada: ")
lista_texto_criptografado_separado = texto_criptografado.split()
texto_descriptografado = ""

valor_chave = int(input("Insira o valor inteiro da chave criptográfica usada: "))
print(f"\nChave de descriptografia: {valor_chave}")

print("\n=== Processo de Descriptografia ===")
for palavra in lista_texto_criptografado_separado:
    print(f"\nProcessando palavra: {palavra}")
    letras_palavra = list(palavra)
    letras_descriptografadas = []
    for letra in letras_palavra:
        if letra in lista_alfabeto:
            posicao_criptografada = lista_alfabeto.index(letra)
            posicao_original = (posicao_criptografada - valor_chave) % len(lista_alfabeto)
            letra_descriptografada = lista_alfabeto[posicao_original]
            letras_descriptografadas.append(letra_descriptografada)
            print(f"Letra '{letra}' (posição {posicao_criptografada}) -> '{letra_descriptografada}' (posição {posicao_original})")
        else:
            letras_descriptografadas.append(letra)
    palavra_descriptografada = "".join(letras_descriptografadas)
    texto_descriptografado += palavra_descriptografada + " "
texto_descriptografado = texto_descriptografado.strip()

print("\n=== Resultado Final ===")
print(f"Texto criptografado: {texto_criptografado}")
print(f"Texto descriptografado: {texto_descriptografado}")