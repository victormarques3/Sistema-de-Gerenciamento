import sqlite3


from MinhaGUI import Ui_MainWindow
from Validacao import Vali
from PySide6.QtWidgets import QMessageBox


class BancoDeDados(Ui_MainWindow):

    def __init__(self, name='BancoDeDados.db') -> None:
        self.name = name
        self.connection = sqlite3.connect(self.name)
        self.validacao = Vali

    def connect(self):
        self.connection = sqlite3.connect(self.name)

    def close_connection(self):
        try:
            self.connection.close()
        except:
            pass

    ###########################################################################
    # TABELA   tb_estoque
    def criar_tabela_estoque(self):
        cursor = self.connection.cursor()
        cursor.execute("""CREATE TABLE IF NOT EXISTS tb_estoque (
        PRODUTO TEXT,
        QUANTIDADE TEXT,
        VALORCOMPRA TEXT,
        VALORVENDA TEXT,
        LUCROPORUNIDADE TEXT)
        """)

    def registrar_estoque(self, lista):
        lucroporunidade = lista[3] - lista[2]
        lista.append(str(lucroporunidade))
        cursor = self.connection.cursor()
        valor = float(lista[2]) * float(lista[1])
        self.adicionar_investimento(valor)

        try:
            cursor.execute("""INSERT INTO tb_estoque (
            PRODUTO, QUANTIDADE, VALORCOMPRA, VALORVENDA, LUCROPORUNIDADE)
            VALUES(?,?,?,?,?)""", lista)
            self.connection.commit()
            return "OK"
        except:
            return "ERRO"

    def ler_dados_repetidos_estoque(self, produto):
        cursor = self.connection.cursor()
        cursor.execute("""SELECT PRODUTO FROM tb_estoque""")
        resultado = 0
        for linha in cursor.fetchall():
            if linha[0] == produto:
                resultado += 1
        return resultado

    def ler_tabela_estoque(self):
        try:
            cursor = self.connection.cursor()
            cursor.execute("SELECT * FROM tb_estoque")
            produtos = cursor.fetchall()
            return produtos
        except:
            pass

    def deletar_estoque(self, nome):
        try:
            cursor = self.connection.cursor()
            cursor.execute(f"DELETE FROM tb_estoque WHERE PRODUTO = '{nome}'")
            self.connection.commit()
            return "Produto deletado com sucesso!!!"
        except:
            return "Erro ao excluir item!!!"

    def editar_estoque(self, dados):
        int1 = self.validacao.validacao_int(dados[1])
        float1 = self.validacao.validacao_float(dados[2])
        float2 = self.validacao.validacao_float(dados[3])
        cursor = self.connection.cursor()
        valido = ""
        if int1 == 0:
            valido += 'Digite uma quantidade inteira...'
        if float1 == 0 or float2 == 0:
            valido += '\nDigite apenas numeros nos valores...'
        if len(valido) > 0:
            dialog = QMessageBox()
            dialog.setIcon(QMessageBox.Warning)
            dialog.setWindowTitle("Erro")
            dialog.setText(valido)
            dialog.exec()
            return 1
        else:
            lucro = float(dados[3]) - float(dados[2])
            cursor.execute(f"""UPDATE tb_estoque set 
                PRODUTO = '{dados[0]}', 
                QUANTIDADE = '{dados[1]}', 
                VALORCOMPRA = '{float(dados[2]):.2f}', 
                VALORVENDA = '{float(dados[3]):.2f}', 
                LUCROPORUNIDADE = '{float(lucro):.2f}' 
            
                WHERE PRODUTO = '{dados[0]}'""")
            for item in self.ler_tabela_estoque():
                if item[1] == '0':
                    self.deletar_estoque(item[0])
            self.connection.commit()
            return 0

    def dados_item(self, produto):
        for linha in self.ler_tabela_estoque():
            if linha[0] == produto:
                return linha

    def lucro_por_item(self, produto):
        for linha in self.ler_tabela_estoque():
            if linha[0] == produto:
                return linha[4]

    ###########################################################################
    # TABELA   tb_clientes
    def criar_tabela_clientes(self):
        cursor = self.connection.cursor()
        cursor.execute("""CREATE TABLE IF NOT EXISTS tb_clientes(
        DATA TEXT,
        CLIENTE TEXT,
        QUANTIDADE TEXT,
        PRODUTO TEXT,
        VALORTOTAL TEXT)
        """)

    def ler_tabela_cliente(self):
        try:
            cursor = self.connection.cursor()
            cursor.execute("SELECT * FROM tb_clientes ORDER BY CLIENTE")
            produtos = cursor.fetchall()
            return produtos
        except:
            pass

    def adicionar_cliente(self, lista):
        cursor = self.connection.cursor()
        cursor.execute("""INSERT INTO tb_clientes (DATA, CLIENTE, QUANTIDADE, PRODUTO, VALORTOTAL)
            VALUES(?,?,?,?,?)""", lista)
        self.connection.commit()

    def apagar_tabela_clientes_dia(self):
        for linha in self.ler_tabela_cliente():
            if str(linha[0]) != str(Vali.data_atual()):
                cursor = self.connection.cursor()
                cursor.execute(f"DELETE FROM tb_clientes WHERE DATA = '{str(linha[0])}'")
                self.connection.commit()

    ###########################################################################
    # TABELA   tb_dividas
    def criar_tabela_dividas(self):
        cursor = self.connection.cursor()
        cursor.execute("""CREATE TABLE IF NOT EXISTS tb_dividas(
        DATA TEXT,
        CLIENTE TEXT,
        DIVIDA TEXT,
        LUCRO TEXT)
        """)

    def ler_tabela_divida(self):
        try:
            cursor = self.connection.cursor()
            cursor.execute("SELECT * FROM tb_dividas ORDER BY CLIENTE")
            produtos = cursor.fetchall()
            return produtos
        except:
            pass

    def ler_tabela_divida_cliente(self, cliente):
        cursor = self.connection.cursor()
        cursor.execute(f"SELECT * FROM tb_dividas WHERE CLIENTE = '{cliente}' ORDER BY CLIENTE")
        produtos = cursor.fetchall()
        return produtos

    def adicionar_divida(self, lista):
        contador = 0
        for linha in self.ler_tabela_divida():
            if str(linha[1]) == str(lista[1]) and str(linha[0]) == str(lista[0]):
                contador += 1
                cursor = self.connection.cursor()
                cursor.execute(f"""UPDATE tb_dividas set
                DATA = '{lista[0]}',
                CLIENTE = '{lista[1]}',
                DIVIDA = '{float(linha[2]) + float(lista[2])}',
                LUCRO = '{float(linha[3]) + float(lista[3])}'

                WHERE CLIENTE = '{lista[1]}'""")
                self.connection.commit()
        if contador == 0:
            cursor = self.connection.cursor()
            cursor.execute("""INSERT INTO tb_dividas (DATA, CLIENTE, DIVIDA, LUCRO)
                VALUES(?,?,?,?)""", lista)
            self.connection.commit()

    def deletar_divida(self, nome):
        cursor = self.connection.cursor()
        cursor.execute(f"DELETE FROM tb_dividas WHERE CLIENTE = '{str(nome)}'")
        self.connection.commit()

    ###########################################################################
    # TABELA   tb_cliente_venda
    def criar_tabela_cliente_venda(self):
        cursor = self.connection.cursor()
        cursor.execute("""CREATE TABLE IF NOT EXISTS tb_cliente_venda(
        PRODUTO TEXT,
        QUANTIDADE TEXT,
        TOTAL TEXT)
        """)

    def ler_tabela_cliente_venda(self):
        cursor = self.connection.cursor()
        cursor.execute("SELECT * FROM tb_cliente_venda")
        produtos = cursor.fetchall()
        return produtos

    def dados_valor_cliente(self):
        valor = 0
        for linha in self.ler_tabela_cliente_venda():
            for coluna in linha:
                if linha[2] == coluna:
                    valor += float(coluna)
        return valor

    def adicionar_clientevenda(self, lista):
        cursor = self.connection.cursor()
        cursor.execute("""INSERT INTO tb_cliente_venda (PRODUTO, QUANTIDADE, TOTAL)
            VALUES(?,?,?)""", lista)
        self.connection.commit()

    def apagar_tabela_clientes(self):
        cursor = self.connection.cursor()
        cursor.execute("DELETE FROM tb_cliente_venda")
        self.connection.commit()

    ###########################################################################
    # TABELA   tb_lucro_investimento
    def criar_tabela_lucro_investimento(self):
        cursor = self.connection.cursor()
        cursor.execute("""CREATE TABLE IF NOT EXISTS tb_lucro_investimento(
        DATA TEXT,
        LUCRO TEXT,
        INVESTIMENTO TEXT)
        """)

    def ler_tabela_lucro_investimento(self):
        cursor = self.connection.cursor()
        cursor.execute("SELECT * FROM tb_lucro_investimento")
        produtos = cursor.fetchall()
        return produtos

    def adicionar_investimento(self, valor):
        cursor = self.connection.cursor()
        if len(self.ler_tabela_lucro_investimento()) == 0:
            cursor.execute(f"""INSERT INTO tb_lucro_investimento (DATA, LUCRO, INVESTIMENTO)
                VALUES ('{Vali.data_atual()}', '0', '{float(valor)}')""")
            self.connection.commit()
        else:
            nao = 0
            for linha in self.ler_tabela_lucro_investimento():
                if str(linha[0]) == str(Vali.data_atual()):
                    cursor.execute(f"""UPDATE tb_lucro_investimento set
                        DATA = '{linha[0]}', 
                        LUCRO = '{linha[1]}', 
                        INVESTIMENTO = '{float(linha[2]) + float(valor)}'""")
                    self.connection.commit()
                    nao += 1
            if nao == 0:
                cursor.execute(f"""INSERT INTO tb_lucro_investimento (DATA, LUCRO, INVESTIMENTO)
                    VALUES ('{Vali.data_atual()}', '0', '{float(valor)}')""")
                self.connection.commit()

    def ler_tabela_lucro_investimento_data(self, data):
        cursor = self.connection.cursor()
        cursor.execute(f"SELECT * FROM tb_lucro_investimento WHERE DATA = '{data}'")
        produtos = cursor.fetchall()
        return produtos

    def apagar_tabela_lucro_investimento(self):
        cursor = self.connection.cursor()
        cursor.execute("DELETE FROM tb_lucro_investimento")
        self.connection.commit()

    def lucro_total(self):
        cursor = self.connection.cursor()
        lucro = 0
        for linha in cursor.execute("SELECT * FROM tb_lucro_investimento"):
            lucro += float(linha[1])
        return str(lucro)

    def lucro_total_data(self, data):
        cursor = self.connection.cursor()
        lucro = 0
        for linha in cursor.execute(f"SELECT * FROM tb_lucro_investimento WHERE DATA = '{data}'"):
            lucro += float(linha[1])
        return str(lucro)

    def adicionar_lucro(self, valor):
        cursor = self.connection.cursor()
        if len(self.ler_tabela_lucro_investimento()) == 0:
            cursor.execute(f"""INSERT INTO tb_lucro_investimento (DATA, LUCRO, INVESTIMENTO)
                VALUES ('{Vali.data_atual()}', '{float(valor)}', '0')""")
            self.connection.commit()
        else:
            nao = 0
            for linha in self.ler_tabela_lucro_investimento():
                if str(linha[0]) == str(Vali.data_atual()):
                    cursor.execute(f"""UPDATE tb_lucro_investimento set
                        DATA = '{linha[0]}', 
                        LUCRO = '{float(linha[1]) + float(valor)}', 
                        INVESTIMENTO = '{linha[2]}'""")
                    self.connection.commit()
                    nao += 1
            if nao == 0:
                cursor.execute(f"""INSERT INTO tb_lucro_investimento (DATA, LUCRO, INVESTIMENTO)
                    VALUES ('{Vali.data_atual()}', '{float(valor)}', '0')""")
                self.connection.commit()

    def investimento_total(self):
        cursor = self.connection.cursor()
        investimento = 0
        for linha in cursor.execute("SELECT * FROM tb_lucro_investimento"):
            investimento += float(linha[2])
        return str(investimento)

    def investimento_total_data(self, data):
        cursor = self.connection.cursor()
        investimento = 0
        for linha in cursor.execute(f"SELECT * FROM tb_lucro_investimento WHERE DATA = '{data}'"):
            investimento += float(linha[2])
        return str(investimento)
