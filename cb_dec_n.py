ALGARISMOS_ATE_HEXA = ("0", "1", "2", "3", "4", "5", "6", "7", "8", "9", "A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z")


def converter_numero(numero: int, base: int):
    resultado = ""
    while numero > 0:
        resultado = ALGARISMOS_ATE_HEXA[numero % base] + resultado
        numero //= base
    return resultado

def boas_vindas():
    print("Como funciona:\n")

    print("Digite o número e a base que ele está: <número> <base>\n")

    print("Exemplo:\n")

    print("Digite o número e a base que ele está: 200 4")

    converter_numero("200", 4)

    print(f"A maior base de conversão possível é {len(ALGARISMOS_ATE_HEXA)}\n")

    print("Pressione o ENTER sem digitar nada, para sair do programa.\n")

print(converter_numero(200, 16))
