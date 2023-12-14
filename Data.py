class Data:
    def __init__(self, dia, mes, ano):
        self.dia = dia
        self.mes = mes
        self.ano = ano

    def setData(self, dia, mes, ano):
        if self.data_valida(dia, mes, ano):
            self.dia = dia
            self.mes = mes
            self.ano = ano
        else:
            print("Data inválidao.")

    def ano_bissexto(self, ano):
        return ano % 4 == 0 and (ano % 100 != 0 or ano % 400 == 0)

    def dias_no_mes(self, mes, ano):
        dias_no_mes = [0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

        if self.ano_bissexto(ano) and mes == 2:
            return 29
        else:
            return dias_no_mes[mes]

    def __str__(self):
        if self.dia is not None and self.mes is not None and self.ano is not None:
            return f"{self.dia}/{self.mes}/{self.ano}"
        else:
            return "Data inválida."

    def dataValida(self, dia, mes, ano):
        try:
            dia, mes, ano = int(dia), int(mes), int(ano)
        except ValueError:
            return False
        if 1 <= mes <= 12:
            dias_no_mes = self.dias_no_mes(mes, ano)
            if 1 <= dia <= dias_no_mes:
                if mes == 2 and dia == 29 and not self.ano_bissexto(ano):
                    return False
                if dia == 31 and mes in [4, 6, 9, 11]:
                    return False
                return True
        return False

