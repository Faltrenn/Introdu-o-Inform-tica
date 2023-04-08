import os

os.system("color") #Necessário para que os códigos de cores funcionem no Windows

ALGARISMOS = ("0", "1", "2", "3", "4", "5", "6", "7", "8", "9", "A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z")


class Cores:
    VERDE = "\033[1;32m"
    AZUL = "\033[1;34m"
    MAGENTA = "\033[1;35m"
    CIANO = "\033[1;36m"
    VERMELHO = "\033[1;31m"
    AMARELO = "\033[1;33m"
    RESET = "\033[0;0m"


def colorir(texto: any, cor: str) -> str:
    return f"{cor}{texto}{Cores.RESET}"


def converter_numero(numero: int, base: int):
    resultado = ""
    resolucao = "\n"
    numero_auxiliar = numero
    passos = [[], []]
    while numero_auxiliar > 0:
        resto = numero_auxiliar % base
        resultado = ALGARISMOS[resto] + resultado
        passos[0].append(numero_auxiliar)
        passos[1].append(resto)
        numero_auxiliar = numero_auxiliar // base
    
    tamanho_do_maior_numero = len(str(sorted(passos[0])[-1]))
    tamanho_do_maior_resto = len(str(sorted(passos[1])[-1]))
    for numero_a, resto in zip(passos[0], passos[1]):
        resolucao += f"{numero_a:>{tamanho_do_maior_numero}}/{base} | resto: {resto:>{tamanho_do_maior_resto}} {colorir(ALGARISMOS[resto], Cores.AZUL) if resto > 9 else ''}\n"
    
    print(resolucao)
    print(f"{colorir(numero, Cores.VERDE)} em decimal é {colorir(resultado, Cores.CIANO)} na base {colorir(base, Cores.MAGENTA)}.")


def validar_partes(partes: list) -> bool:
    if len(partes) != 2:
        print(colorir("\nDigite o número e a base que deseja convertê-lo: <número> <base>\n", Cores.AMARELO))
        return False
    numero = partes[0]
    base = partes[1]
    if not numero.isnumeric():
        print(colorir("\nDigite um número válido\n", Cores.VERMELHO))
        return False
    if not base.isnumeric() or int(base) < 2:
        print(colorir("\nDigite uma base válida\n", Cores.VERMELHO))
        return False
    if int(base) > 36:
        print(colorir("\nA maior base de conversão é 36\n", Cores.AMARELO))
        return False
    return True


print("Como funciona:\n")

print("Digite o número e a base que deseja convertê-lo: <número> <base>\n")

print("Exemplo:\n")

print("Digite o número e a base que deseja convertê-lo: 200 4")

converter_numero(200, 4)

print(f"A maior base de conversão possível é {len(ALGARISMOS)}\n")

print("Pressione o ENTER sem digitar nada, para sair do programa.\n")


while True:
    escolha = input("Digite o número e a base que deseja convertê-lo: ")
    
    if escolha == "":
        break
    
    partes = escolha.split(" ")
    
    if not validar_partes(partes):
        continue
    
    numero = int(partes[0])
    base = int(partes[1])

    converter_numero(numero, base)
