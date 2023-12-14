
# Importar Classe
from Data import Data

# Função para obter entrada do usuário
def dataUsuario():
    dia = input("Digite o dia: ")
    mes = input("Digite o mês: ")
    ano = input("Digite o ano: ")

    def dataValida(valor):
        try:
            int(valor)
            return True
        except ValueError:
            return False

    if dataValida(dia) and dataValida(mes) and dataValida(ano):
        return int(dia), int(mes), int(ano)
    else:
        print("Valor inválido. Por favor, insira apenas números inteiros.")

# Saída
entrada_usuario = dataUsuario()
if entrada_usuario is not None:
    data = Data(*entrada_usuario)
    if data.dataValida(data.dia, data.mes, data.ano):
        print(data)
    else:
        print("Essa não é uma data válida.")
