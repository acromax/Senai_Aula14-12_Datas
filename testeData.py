from Data import Data

# Apresentação

print("\n\t\t -- Programa para confirmar datas válidas -- ")

# Função para obter entrada do usuário
def obter_entrada_usuario():
    try:
        dia = int(input("Digite o dia: "))
        mes = int(input("Digite o mês: "))
        ano = int(input("Digite o ano: "))
        return dia, mes, ano
    except ValueError:
        print("Valor inválido. Por favor, insira apenas números inteiros.")
        return None

# Testes
entrada_usuario = obter_entrada_usuario()
if entrada_usuario[0] is not None:
    data = Data(*entrada_usuario)
    print(data)