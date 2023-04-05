ALGARISMOS_ATE_HEXA = ("0", "1", "2", "3", "4", "5", "6", "7", "8", "9", "A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z")


def converter_digito(digito: str) -> int:
    return ALGARISMOS_ATE_HEXA.index(digito.upper())

def validar_numero(numero: str, base: int) -> bool:
    for digito in numero:
        if converter_digito(digito) >= base:
            return False
    return True

def converter_numero(numero: str, base: int) -> int:
    tamanho_do_numero = len(numero) - 1
    resultado = 0

    resolucao = "\n"
    for indice, digito in enumerate(numero):
        resultado += converter_digito(digito) * (base ** (tamanho_do_numero - indice))
        resolucao += f"{digito} * {base}^{tamanho_do_numero - indice} {'+ ' if indice != tamanho_do_numero else ''}"

    print(f"{resolucao}= {resultado}\n")

    print(f"{numero} na base {base} é {resultado} na base 10\n")


def boas_vindas():
    print("Como funciona:\n")

    print("Digite o número e a base que ele está: <número> <base>\n")

    print("Exemplo:\n")

    print("Digite o número e a base que ele está: 200 4")

    converter_numero("200", 4)

    print(f"A maior base de conversão possível é {len(ALGARISMOS_ATE_HEXA)}\n")

    print("Pressione o ENTER sem digitar nada, para sair do programa.\n")


boas_vindas()

escolha: str = None

while escolha != "":
    escolha = input("Digite o número e a base que ele está: ")
    partes = escolha.split(" ")
    
    if len(partes) != 2:
        print("\nDigite o número e a base que ele está: <número> <base>\n")
        continue

    numero = partes[0]
    base = int(partes[1])
    
    if not base.isnumeric() or base > 36:
        print(f"A base {base} não é válida\n")
        continue

    if validar_numero(numero, base):
        converter_numero(numero, base)
    else:
        print(f"{numero} é inválido na base {base}\n")
