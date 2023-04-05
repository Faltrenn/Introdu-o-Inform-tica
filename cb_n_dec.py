ALGARISMOS_ATE_HEXA = ("0", "1", "2", "3", "4", "5", "6", "7", "8", "9", "A", "B", "C", "D", "E", "F")

print("Como funciona:\n")

print("Digite o número e a base que ele está: <número> <base>\n")

print("Exemplo: 100 2\n")

print("Pressione o ENTER sem digitar nada, para sair do programa.\n")


def converter_digito(digito: str) -> int:
    return ALGARISMOS_ATE_HEXA.index(digito.upper())

def validar_numero(numero: str, base: int) -> bool:
    for digito in numero:
        if converter_digito(digito) >= base:
            return False
    return True


escolha: str = None

while escolha != "":
    escolha = input("Digite o número e a base que ele está: ")
    partes = escolha.split(" ")
    if validar_numero(partes[0], int(partes[1])):
        tamanho_do_numero = len(partes[0]) - 1
        base = int(partes[1])
        resultado = 0
        for indice, digito in enumerate(partes[0]):
            resultado += converter_digito(digito) * (base ** (tamanho_do_numero - indice))
        print(f"{partes[0]} na base {partes[1]} é {resultado} na base 10")
    else:
        print(f"{partes[0]} é inválido na base {partes[1]}")
