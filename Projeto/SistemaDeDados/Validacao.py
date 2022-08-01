# 0 FALSE
# 1 TRUE
import datetime


class Vali:
    @staticmethod
    def validacao_int(valor):
        try:
            if type(int(valor)) == int:
                pass
        except:
            return 0
        else:
            return 1

    @staticmethod
    def validacao_float(valor):
        try:
            if type(float(valor.replace(',', '.'))) == float:
                pass
        except:
            return 0
        else:
            return 1

    @staticmethod
    def validacao_str(valor):
        try:
            if type(float(valor.replace(',', '.'))) != str:
                pass
        except:
            return 1
        else:
            return 0

    @staticmethod
    def data_atual():
        arq = open("Nome.txt")
        linhas = arq.readlines()

        data_atual = datetime.date.today()
        data_anterior = data_atual - datetime.timedelta(1)

        data_atual_br = f"{data_atual.day}/{data_atual.month}/{data_atual.year}"
        data_anterior_br = f"{data_anterior.day}/{data_anterior.month}/{data_anterior.year}"

        hora_atual = datetime.datetime.today().hour

        if hora_atual >= int(linhas[1]):
            return data_atual_br
        else:
            return data_anterior_br
