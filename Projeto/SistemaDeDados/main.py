from MinhaGUI import Ui_MainWindow, Qt, QFont
from PySide6.QtWidgets import QApplication, QMainWindow, QMessageBox, QTableWidgetItem, QAbstractItemView
from PySide6 import QtCore
import sys
from tabelas import BancoDeDados
from Validacao import *


def QdialogEspacoBranco():
    dialog = QMessageBox()
    dialog.setIcon(QMessageBox.Warning)
    dialog.setWindowTitle("Erro")
    dialog.setText("Espaço em branco!!!")
    dialog.exec()


class MainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.animação = None
        self.setupUi(self)
        self.ColocarNome()
        self.Atualizar()

        #########################################################################################
        # BOTÃO DESLIZAR ESQUERDA/DIREITA
        self.btn_menu.clicked.connect(self.MenuEsconder)

        #########################################################################################
        # BOTÕES PAGINAS DO SISTEMA
        self.Button_menu_clientes.clicked.connect(lambda: self.stackedWidget.setCurrentWidget(self.pg_clientes))
        self.Button_menu_balanco.clicked.connect(lambda: self.stackedWidget.setCurrentWidget(self.pg_balanco))
        self.Button_menu_estoque.clicked.connect(lambda: self.stackedWidget.setCurrentWidget(self.pg_estoque))
        self.Button_menu_dividas.clicked.connect(lambda: self.stackedWidget.setCurrentWidget(self.pg_dividas))
        self.Button_menu_definicoes.clicked.connect(lambda: self.stackedWidget.setCurrentWidget(self.pg_definicoes))

        #########################################################################################
        # SALVAR NOME E DATA
        self.btn_definicoes_salvar.clicked.connect(self.NomeEstabelecimento)

        #########################################################################################
        # ESTOQUE
        self.tableWidget_estoque_adicionar.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.tableWidget_estoque_remover.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.tableWidget_balanco_LI.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.tableWidget_cliente_tabela.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.tableWidget_cliente_venda.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.tableWidget_dividas.setEditTriggers(QAbstractItemView.NoEditTriggers)

        self.btn_estoque_adicionar.clicked.connect(self.AdicionarEstoque)
        self.btn_estoque_editar.clicked.connect(self.EditarProdutoEstoque)
        self.btn_estoque_remover.clicked.connect(self.DeletarProdutoEstoque)

        #########################################################################################
        # CLIENTES
        self.label_cliente_valor.setText('')
        self.btn_cliente_adicionar.clicked.connect(self.ClienteVista)
        self.btn_cliente_apagar.clicked.connect(self.ApagarTabelaClientes)
        self.btn_cliente_vender.clicked.connect(self.VenderClientes)

        #########################################################################################
        # DIVIDAS
        self.comboBox_dividas_cliente.currentTextChanged.connect(self.AtualizarTabelaDividas)
        self.btn_dividas_resetar.clicked.connect(self.Atualizar)
        self.lineEdit_dividas_valorRecebido.returnPressed.connect(self.TrocoDividas)
        self.btn_dividas_pagar.clicked.connect(self.PagarDivida)

        #########################################################################################
        # DIVIDAS
        self.btn_balanco_deletar.clicked.connect(self.DeletarTabelaLucroInvestimento)
        self.comboBox_balanco_mes.currentTextChanged.connect(self.FiltrarTabelaBalanco)
    #########################################################################################
    # FUNÇÕES
    #########################################################################################

    def MenuEsconder(self):
        largura = self.frame_esquerda.width()
        if largura == 0:
            nova_largura = 200
        else:
            nova_largura = 0

        self.animação = QtCore.QPropertyAnimation(self.frame_esquerda, b"maximumWidth")
        self.animação.setDuration(250)
        self.animação.setStartValue(largura)
        self.animação.setEndValue(nova_largura)
        self.animação.setEasingCurve(QtCore.QEasingCurve.InOutQuart)
        self.animação.start()

    def NomeEstabelecimento(self):
        if self.lineEdit_definicoes_nomelocal.text() != "":
            try:
                arq = open("Nome.txt", "w+")
                definições = [self.lineEdit_definicoes_nomelocal.text(),
                              str(self.timeEdit_definicoes_DE.text()[:2]),
                              str(self.timeEdit_definicoes_AS.text()[:2])]
                self.label_nomeEstabelecimento.setText(definições[0].upper())
                for linha in definições:
                    arq.write(linha)
                    arq.write('\n')
            except:
                pass
            else:
                dialog = QMessageBox()
                dialog.setIcon(QMessageBox.Information)
                dialog.setWindowTitle("Salvo")
                dialog.setText("Alterações Salvas!!!")
                resultado = dialog.exec()
                if resultado == QMessageBox.Ok:
                    self.stackedWidget.setCurrentWidget(self.pg_menu)
                    self.lineEdit_definicoes_nomelocal.clear()
        else:
            QdialogEspacoBranco()

    def ColocarNome(self):
        arq = open("Nome.txt")
        linhas = arq.readlines()
        self.label_nomeEstabelecimento.setText(str(linhas[0].upper()))
        self.label_nomeEstabelecimento.setAlignment(Qt.AlignCenter)
        self.label_nomeEstabelecimento.setWordWrap(True)
        self.label_nomeEstabelecimento.setFont(QFont("MS Shell Dlg 2", 12))
        self.label_nomeEstabelecimento.setStyleSheet("color: rgb(255, 255, 255)")

    ###########################################
    # ESTOQUE
    ###########################################
    def AdicionarEstoque(self):
        if self.lineEdit_estoque_produto.text() == "" or \
                self.lineEdit_estoque_quantidade.text() == "" or \
                self.lineEdit_estoque_valorCompra.text() == "" or \
                self.lineEdit_estoque_valorVenda.text() == "":
            QdialogEspacoBranco()
        else:
            dbb = BancoDeDados()
            dbb.connect()
            if dbb.ler_dados_repetidos_estoque(self.lineEdit_estoque_produto.text().upper()) > 0:
                dialog = QMessageBox()
                dialog.setIcon(QMessageBox.Warning)
                dialog.setWindowTitle("Erro")
                dialog.setText("O produto já foi adicionado!!!\nTente atualizar")
                dialog.exec()
                self.tabWidget.setCurrentWidget(self.tab_3)

            else:
                valido = ''
                vl = Vali()
                if vl.validacao_str(str(self.lineEdit_estoque_produto.text())) == 0:
                    valido += 'Formato de nome incorreto...'
                if vl.validacao_int(str(self.lineEdit_estoque_quantidade.text())) == 0:
                    valido += '\nDigite uma quantidade inteira...'
                if vl.validacao_float(str(self.lineEdit_estoque_valorCompra.text())) == 0 or \
                        vl.validacao_float(str(self.lineEdit_estoque_valorVenda.text())) == 0:
                    valido += '\nDigite apenas numeros nos valores...'
                if len(valido) > 0:
                    self.lineEdit_estoque_produto.clear()
                    self.lineEdit_estoque_valorVenda.clear()
                    self.lineEdit_estoque_quantidade.clear()
                    self.lineEdit_estoque_valorCompra.clear()

                    dialog = QMessageBox()
                    dialog.setIcon(QMessageBox.Warning)
                    dialog.setWindowTitle("Erro")
                    dialog.setText(valido)
                    dialog.exec()
                else:
                    lista_produtos = [self.lineEdit_estoque_produto.text().upper(),
                                      int(self.lineEdit_estoque_quantidade.text()),
                                      float(self.lineEdit_estoque_valorCompra.text().replace(',', '.')),
                                      float(self.lineEdit_estoque_valorVenda.text().replace(',', '.'))]
                    dbb.registrar_estoque(lista_produtos)

                    self.Atualizar()

                    dialog = QMessageBox()
                    dialog.setIcon(QMessageBox.Information)
                    dialog.setWindowTitle("ADICIONADO")
                    dialog.setText("Produto adicionado!")
                    dialog.exec()

    def ColocarTabelaEstoque(self):
        ddb = BancoDeDados()
        ddb.connect()
        resultado = ddb.ler_tabela_estoque()

        self.tableWidget_estoque_adicionar.clearContents()
        self.tableWidget_estoque_remover.clearContents()
        self.tableWidget_estoque_editar.clearContents()
        self.tableWidget_estoque_adicionar.setRowCount(len(resultado))
        self.tableWidget_estoque_remover.setRowCount(len(resultado))
        self.tableWidget_estoque_editar.setRowCount(len(resultado))
        for linha, text in enumerate(resultado):
            for coluna, data in enumerate(text):
                self.tableWidget_estoque_adicionar.setItem(linha, coluna, QTableWidgetItem(str(data)))
                self.tableWidget_estoque_remover.setItem(linha, coluna, QTableWidgetItem(str(data)))
                self.tableWidget_estoque_editar.setItem(linha, coluna, QTableWidgetItem(str(data)))
        ddb.close_connection()

    def LerDadosTabelaE(self):
        dados = []
        dados_editados = []
        for linha in range(self.tableWidget_estoque_editar.rowCount()):
            for coluna in range(self.tableWidget_estoque_editar.columnCount()):
                dados.append(self.tableWidget_estoque_editar.item(linha, coluna).text().replace(',', '.'))
            dados_editados.append(dados)
            dados = []
        return dados_editados

    def EditarProdutoEstoque(self):
        dados_editados = self.LerDadosTabelaE()

        dcb = BancoDeDados()
        dcb.connect()
        # ATUALIZAR TABELA LUCRO/INVESTIMENTO
        tabela = dcb.ler_tabela_estoque()
        contl = 0
        contc = 0
        for linha in dados_editados:
            for coluna in linha:
                if coluna != tabela[contl][contc]:
                    atual = float(linha[1]) * float(linha[2])
                    anterior = float(tabela[contl][1]) * float(tabela[contl][2])
                    dcb.adicionar_investimento(atual - anterior)
                contc += 1
            contc = 0
            contl += 1
        # ATUALIZAR TABELA ESTOQUE
        valido = 0
        for produtos in dados_editados:
            resp = dcb.editar_estoque(produtos)
            valido += resp
        dcb.close_connection()
        if valido == 0:
            dialog = QMessageBox()
            dialog.setIcon(QMessageBox.Warning)
            dialog.setWindowTitle("Atualizado")
            dialog.setText("Produto atualizado")
            dialog.exec()
            self.Atualizar()

    def DeletarProdutoEstoque(self):

        if Vali.validacao_int(self.lineEdit_estoque_remover.text()) == 0:
            dialog = QMessageBox()
            dialog.setIcon(QMessageBox.Information)
            dialog.setWindowTitle("ERRO")
            dialog.setText("Digite um número inteiro!")
            dialog.exec()
            self.lineEdit_estoque_remover.setText('0')

        else:
            dab = BancoDeDados()
            dab.connect()

            dialog = QMessageBox()
            dialog.setIcon(QMessageBox.Information)
            dialog.setWindowTitle("DELETAR")
            dialog.setText("Deseja realmente deletar?")
            dialog.setStandardButtons(QMessageBox.Yes | QMessageBox.No)
            resposta = dialog.exec()
            if resposta == QMessageBox.Yes:
                resultado = Vali.validacao_int(self.lineEdit_estoque_remover.text())
                if resultado == 0:
                    dialog = QMessageBox()
                    dialog.setIcon(QMessageBox.Information)
                    dialog.setWindowTitle("DELETAR")
                    dialog.setText("Digite apenas números inteiros!!!")
                else:
                    if int(self.lineEdit_estoque_remover.text()) == 0 or int(self.lineEdit_estoque_remover.text()) == \
                            int(self.tableWidget_estoque_remover.selectionModel().currentIndex().siblingAtColumn(
                                1).data()):
                        produto = \
                            self.tableWidget_estoque_remover.selectionModel().currentIndex().siblingAtColumn(0).data()

                        resultado = dab.deletar_estoque(produto)
                        self.ColocarTabelaEstoque()

                        dialog = QMessageBox()
                        dialog.setIcon(QMessageBox.Information)
                        dialog.setWindowTitle("DELETADO")
                        dialog.setText(resultado)
                        dialog.exec()

                    elif int(self.lineEdit_estoque_remover.text()) > int(
                            self.tableWidget_estoque_remover.selectionModel().currentIndex().siblingAtColumn(1).data()):
                        dialog = QMessageBox()
                        dialog.setIcon(QMessageBox.Information)
                        dialog.setWindowTitle("DELETAR")
                        dialog.setText("Você não tem essa quantidade!")
                        dialog.exec()

                    else:
                        quant_del = \
                            int(self.tableWidget_estoque_remover.selectionModel().currentIndex().siblingAtColumn(
                                1).data()) \
                            - int(self.lineEdit_estoque_remover.text())
                        lista = [
                            self.tableWidget_estoque_remover.selectionModel().currentIndex().siblingAtColumn(0).data(),
                            quant_del,
                            self.tableWidget_estoque_remover.selectionModel().currentIndex().siblingAtColumn(2).data(),
                            self.tableWidget_estoque_remover.selectionModel().currentIndex().siblingAtColumn(3).data()]
                        dab.editar_estoque(lista)

                        dialog = QMessageBox()
                        dialog.setIcon(QMessageBox.Information)
                        dialog.setWindowTitle("DELETADO")
                        dialog.setText('Produto deletado com sucesso!!!')
                        dialog.exec()

                self.Atualizar()
            dab.close_connection()

    ###########################################
    # CLIENTES
    ###########################################
    def ClienteVista(self):
        dfb = BancoDeDados()
        dfb.connect()
        if Vali.validacao_int(self.lineEdit_cliente_quantidade.text()) == 0:
            dialog = QMessageBox()
            dialog.setIcon(QMessageBox.Information)
            dialog.setWindowTitle("ERRO")
            dialog.setText("Digite um número inteiro!")
            dialog.exec()
        else:
            produto = self.comboBox_cliente_produto.currentText()
            quantidade = int(self.lineEdit_cliente_quantidade.text())
            dados = dfb.dados_item(produto)
            if int(quantidade) > int(dados[1]):
                dialog = QMessageBox()
                dialog.setIcon(QMessageBox.Information)
                dialog.setWindowTitle("ERRO")
                dialog.setText(f"Você não tem {quantidade} {produto}!\n{dados[1]} {produto} no estoque.")
                dialog.exec()
            else:
                valor = int(quantidade) * float(dados[3])
                lista = [produto, quantidade, valor]
                dfb.adicionar_clientevenda(lista)

                self.label_cliente_valor.setText(f'R$ {dfb.dados_valor_cliente():.2f}')
                self.label_cliente_valor.setAlignment(Qt.AlignCenter)
                self.label_cliente_valor.setFont(QFont("MS Shell Dlg 2", 15))
                self.label_cliente_valor.setStyleSheet("color: rgb(255, 255, 255)")

        self.Atualizar()
        dfb.close_connection()

        self.lineEdit_cliente_quantidade.clear()

    def ColocarTabelaClienteVenda(self):
        dgb = BancoDeDados()
        dgb.connect()
        resultado = dgb.ler_tabela_cliente_venda()

        self.tableWidget_cliente_venda.clearContents()
        self.tableWidget_cliente_venda.setRowCount(len(resultado))
        for linha, text in enumerate(resultado):
            for coluna, data in enumerate(text):
                self.tableWidget_cliente_venda.setItem(linha, coluna, QTableWidgetItem(str(data)))
        dgb.close_connection()

    def ApagarTabelaClientes(self):
        dialog = QMessageBox()
        dialog.setIcon(QMessageBox.Information)
        dialog.setWindowTitle("DELETAR")
        dialog.setText("Deseja realmente deletar?")
        dialog.setStandardButtons(QMessageBox.Yes | QMessageBox.No)
        resposta = dialog.exec()
        if resposta == QMessageBox.Yes:
            dhb = BancoDeDados()
            dhb.connect()
            dhb.apagar_tabela_clientes()
            dhb.close_connection()
            self.Atualizar()

    def VenderClientes(self):
        dib = BancoDeDados()
        dib.connect()
        dialog = QMessageBox()
        dialog.setIcon(QMessageBox.Information)
        dialog.setWindowTitle("VENDAS")
        dialog.setText("Deseja realmente concluir a venda?")
        dialog.setStandardButtons(QMessageBox.Yes | QMessageBox.No)
        resposta = dialog.exec()
        if resposta == QMessageBox.Yes:
            if len(dib.ler_tabela_cliente_venda()) == 0:
                dialog = QMessageBox()
                dialog.setIcon(QMessageBox.Information)
                dialog.setWindowTitle("ERRO")
                dialog.setText("Adicione algum produto antes!")
                dialog.exec()
            else:
                if self.radioButton_clientes_nao.isChecked():
                    if self.radioButton_cliente_novoCliente.isChecked():
                        ok = True
                        if len(self.lineEdit_cliente_novoCliente.text().upper()) == 0:
                            dialog = QMessageBox()
                            dialog.setIcon(QMessageBox.Information)
                            dialog.setWindowTitle("ERRO")
                            dialog.setText("Digite um nome ao cliente!")
                            dialog.exec()
                            ok = False
                        if Vali.validacao_str(self.lineEdit_cliente_novoCliente.text().upper()) == 0:
                            dialog = QMessageBox()
                            dialog.setIcon(QMessageBox.Information)
                            dialog.setWindowTitle("ERRO")
                            dialog.setText("Digite um nome valido!")
                            dialog.exec()
                            self.lineEdit_cliente_novoCliente.clear()
                            ok = False
                        if ok:
                            # adiciona novo cliente
                            lucrototal = 0
                            for linha in dib.ler_tabela_cliente_venda():
                                # adiciona tabela clientes
                                lista = [Vali.data_atual(), self.lineEdit_cliente_novoCliente.text().upper(),
                                         str(linha[1]), str(linha[0]), str(linha[2])]
                                lucro = dib.lucro_por_item(linha[0])
                                dib.adicionar_cliente(lista)
                                # adiciona tabela dividas
                                lucrototal += float(lucro) * int(linha[1])
                                listadivida = [Vali.data_atual(), self.lineEdit_cliente_novoCliente.text().upper(),
                                               dib.dados_valor_cliente(), lucrototal]
                                dib.adicionar_divida(listadivida)
                                # remove do estoque
                                estoque = dib.dados_item(linha[0])
                                listaalter = [estoque[0], int(estoque[1]) - int(linha[1]), estoque[2], estoque[3]]
                                dib.editar_estoque(listaalter)
                            # limpa todos os dados
                            self.lineEdit_cliente_novoCliente.clear()
                            dib.apagar_tabela_clientes()

                            dialog = QMessageBox()
                            dialog.setIcon(QMessageBox.Information)
                            dialog.setWindowTitle("COMPRA")
                            dialog.setText("Ciente adicionado!!!\nProduto adicionado ao cliente!")
                            dialog.exec()
                    if self.radioButton_cliente_cliente.isChecked():
                        lucrototal = 0
                        for linha in dib.ler_tabela_cliente_venda():
                            # adiciona tabela clientes
                            lista = [Vali.data_atual(), self.comboBox_cliente_cliente.currentText(),
                                     str(linha[1]), str(linha[0]), str(linha[2])]
                            lucro = dib.lucro_por_item(linha[0])
                            dib.adicionar_cliente(lista)
                            # adiciona tabela dividas
                            lucrototal += float(lucro) * int(linha[1])
                            listadivida = [Vali.data_atual(), str(self.comboBox_cliente_cliente.currentText()),
                                           dib.dados_valor_cliente(), lucrototal]
                            dib.adicionar_divida(listadivida)
                            # remove do estoque
                            estoque = dib.dados_item(linha[0])
                            listaalter = [estoque[0], int(estoque[1]) - int(linha[1]), estoque[2], estoque[3]]
                            dib.editar_estoque(listaalter)
                        # limpa todos os dados
                        self.lineEdit_cliente_novoCliente.clear()
                        dib.apagar_tabela_clientes()

                        dialog = QMessageBox()
                        dialog.setIcon(QMessageBox.Information)
                        dialog.setWindowTitle("COMPRA")
                        dialog.setText("Produto adicionado ao cliente!")
                        dialog.exec()
                else:
                    pass
                    lucrototal = 0
                    for linha in dib.ler_tabela_cliente_venda():
                        lucro = dib.lucro_por_item(linha[0])
                        lucrototal += float(lucro) * int(linha[1])
                        # remove do estoque
                        estoque = dib.dados_item(linha[0])
                        listaalter = [estoque[0], int(estoque[1]) - int(linha[1]), estoque[2], estoque[3]]
                        dib.editar_estoque(listaalter)
                    dib.adicionar_lucro(lucrototal)
                    dialog = QMessageBox()
                    dialog.setIcon(QMessageBox.Information)
                    dialog.setWindowTitle("COMPRA")
                    dialog.setText("Venda concluida!!!\nLucro adicionado ao balanço!")
                    dialog.exec()
                    self.lineEdit_cliente_novoCliente.clear()
                    dib.apagar_tabela_clientes()
        self.Atualizar()
        self.label_cliente_valor.setText('')
        dib.close_connection()

    def ColocarTabelaCliente(self):
        dgb = BancoDeDados()
        dgb.connect()
        resultado = dgb.ler_tabela_cliente()

        self.tableWidget_cliente_tabela.clearContents()
        self.tableWidget_cliente_tabela.setRowCount(len(resultado))
        for linha, text in enumerate(resultado):
            for coluna, data in enumerate(text):
                self.tableWidget_cliente_tabela.setItem(linha, coluna, QTableWidgetItem(str(data)))
        dgb.close_connection()

    ###########################################
    # DIVIDAS
    ###########################################
    def AtualizarTabelaDividas(self, cliente):
        djb = BancoDeDados()
        djb.connect()
        resultado = djb.ler_tabela_divida_cliente(cliente)
        self.tableWidget_dividas.clearContents()
        self.tableWidget_dividas.setRowCount(len(resultado))
        for linha, text in enumerate(resultado):
            for coluna, data in enumerate(text):
                self.tableWidget_dividas.setItem(linha, coluna, QTableWidgetItem(str(data)))
        valortotal = 0
        for linha in resultado:
            valortotal += float(linha[2])
        self.label_dividas_total.setText(f"R$ {valortotal:.2f}")
        self.label_dividas_total.setAlignment(Qt.AlignCenter)
        self.label_dividas_total.setFont(QFont("MS Shell Dlg 2", 12))
        self.label_dividas_total.setStyleSheet("color: rgb(255, 255, 255)")
        djb.close_connection()

    def TrocoDividas(self):
        valorrecebido = self.lineEdit_dividas_valorRecebido.text()
        if Vali.validacao_float(valorrecebido) == 0:
            dialog = QMessageBox()
            dialog.setIcon(QMessageBox.Information)
            dialog.setWindowTitle("ERRO")
            dialog.setText("Digite um valor valido!")
            dialog.exec()
            self.lineEdit_dividas_valorRecebido.clear()
        else:
            if self.label_dividas_total.text() == '':
                dialog = QMessageBox()
                dialog.setIcon(QMessageBox.Information)
                dialog.setWindowTitle("ERRO")
                dialog.setText("Selecione um cliente!")
                dialog.exec()
            else:
                cliente = self.comboBox_dividas_cliente.currentText()
                resposta = ''
                troco = f"{float(float(valorrecebido) - float(self.label_dividas_total.text()[2:])):.2f}"
                if float(valorrecebido) < float(self.label_dividas_total.text()[2:]):
                    resposta = f"{cliente} fica devendo R$ {str(troco).replace('-','').replace('.', ',')}"
                else:
                    resposta = f"Troco de R$ {str(troco).replace('-', '').replace('.', ',')} para {cliente}"
                self.label_dividas_troco.setText(resposta)
                self.label_dividas_troco.setAlignment(Qt.AlignCenter)
                self.label_dividas_troco.setFont(QFont("MS Shell Dlg 2", 11))
                self.label_dividas_troco.setStyleSheet("color: rgb(255, 255, 255)")

    def PagarDivida(self):
        dkb = BancoDeDados()
        dkb.connect()
        if self.label_dividas_total.text() == '' or self.label_dividas_troco.text() == '':
            dialog = QMessageBox()
            dialog.setIcon(QMessageBox.Information)
            dialog.setWindowTitle("ERRO")
            dialog.setText("Selecione um cliente e um valor recebido!")
            dialog.exec()
        else:
            dialog = QMessageBox()
            dialog.setIcon(QMessageBox.Information)
            dialog.setWindowTitle("VENDAS")
            dialog.setText(f"PAGAR DIVIDA DE {self.comboBox_dividas_cliente.currentText()}?")
            dialog.setStandardButtons(QMessageBox.Yes | QMessageBox.No)
            resposta = dialog.exec()
            if resposta == QMessageBox.Yes:
                valorrecebido = f"{float(self.lineEdit_dividas_valorRecebido.text()):.2f}"
                valordivida = f"{float(self.label_dividas_total.text()[2:]):.2f}"
                lucro = 0
                for linha in dkb.ler_tabela_divida_cliente(self.comboBox_dividas_cliente.currentText()):
                    lucro += float(linha[3])
                if float(valorrecebido) >= float(valordivida):

                    dkb.adicionar_lucro(float(lucro))
                    dkb.deletar_divida(str(self.comboBox_dividas_cliente.currentText()))

                    self.Atualizar()
                    dialog = QMessageBox()
                    dialog.setIcon(QMessageBox.Information)
                    dialog.setWindowTitle("CONTA PAGA")
                    dialog.setText("Lucro adicionado ao balanço!")
                    dialog.exec()
                else:
                    lucropagamento = float(lucro) * (((float(self.lineEdit_dividas_valorRecebido.text()) * 100)
                                                      / float(valordivida)) / 100)
                    restantelucro = float(lucro) - float(lucropagamento)
                    dividanova = \
                        float(self.label_dividas_total.text()[2:]) - float(self.lineEdit_dividas_valorRecebido.text())

                    listadividanova = [Vali.data_atual(), self.comboBox_dividas_cliente.currentText(),
                                       dividanova, restantelucro]
                    dkb.adicionar_lucro(float(lucropagamento))
                    dkb.deletar_divida(str(self.comboBox_dividas_cliente.currentText()))
                    dkb.adicionar_divida(listadividanova)

                    self.Atualizar()
                    dialog = QMessageBox()
                    dialog.setIcon(QMessageBox.Information)
                    dialog.setWindowTitle("CONTA PAGA")
                    dialog.setText("Conta paga parcialmente!")
                    dialog.exec()
        dkb.close_connection()

    def ColocarTabelaDivida(self):
        dgb = BancoDeDados()
        dgb.connect()
        resultado = dgb.ler_tabela_divida()

        self.tableWidget_dividas.clearContents()
        self.tableWidget_dividas.setRowCount(len(resultado))
        for linha, text in enumerate(resultado):
            for coluna, data in enumerate(text):
                self.tableWidget_dividas.setItem(linha, coluna, QTableWidgetItem(str(data)))
        dgb.close_connection()

    ###########################################
    # BALANÇO
    ###########################################
    def ColocarTabelaLucroInvestimento(self):
        deb = BancoDeDados()
        deb.connect()
        resultado = deb.ler_tabela_lucro_investimento()

        self.tableWidget_balanco_LI.clearContents()
        self.tableWidget_balanco_LI.setRowCount(len(resultado))

        for linha, text in enumerate(resultado):
            for coluna, data in enumerate(text):
                self.tableWidget_balanco_LI.setItem(linha, coluna, QTableWidgetItem(str(data)))

        lucro = deb.lucro_total()
        investimento = deb.investimento_total()
        self.lbl_lucro.setText(f'{float(lucro):.2f}')
        self.lbl_lucro.setAlignment(Qt.AlignCenter)
        self.lbl_lucro.setFont(QFont("MS Shell Dlg 2", 15))
        self.lbl_lucro.setStyleSheet("color: rgb(255, 255, 255)")

        self.lbl_invest.setText(f'{float(investimento):.2f}')
        self.lbl_invest.setAlignment(Qt.AlignCenter)
        self.lbl_invest.setFont(QFont("MS Shell Dlg 2", 15))
        self.lbl_invest.setStyleSheet("color: rgb(255, 255, 255)")
        deb.close_connection()

    def DeletarTabelaLucroInvestimento(self):
        dialog = QMessageBox()
        dialog.setIcon(QMessageBox.Information)
        dialog.setWindowTitle("DELETAR")
        dialog.setText("Deseja realmente deletar?")
        dialog.setStandardButtons(QMessageBox.Yes | QMessageBox.No)
        resposta = dialog.exec()
        if resposta == QMessageBox.Yes:
            dlb = BancoDeDados()
            dlb.connect()
            dlb.apagar_tabela_lucro_investimento()
            dlb.close_connection()
            self.Atualizar()

    def FiltrarTabelaBalanco(self, mes):
        dmb = BancoDeDados()
        dmb.connect()
        resultado = []
        lucro = 0
        investimento = 0
        if mes != 'TUDO':
            resultado = dmb.ler_tabela_lucro_investimento_data('/'+mes+'/')
            for linha1 in dmb.ler_tabela_lucro_investimento():
                if '/'+mes+'/' in linha1[0]:
                    lucro += float(linha1[1])
                    investimento += float(linha1[2])
                    resultado.append(linha1)

            self.tableWidget_balanco_LI.clearContents()
            self.tableWidget_balanco_LI.setRowCount(len(resultado))

            for linha, text in enumerate(resultado):
                for coluna, data in enumerate(text):
                    self.tableWidget_balanco_LI.setItem(linha, coluna, QTableWidgetItem(str(data)))
            self.lbl_lucro.setText(f'{float(lucro):.2f}')
            self.lbl_lucro.setAlignment(Qt.AlignCenter)
            self.lbl_lucro.setFont(QFont("MS Shell Dlg 2", 15))
            self.lbl_lucro.setStyleSheet("color: rgb(255, 255, 255)")

            self.lbl_invest.setText(f'{float(investimento):.2f}')
            self.lbl_invest.setAlignment(Qt.AlignCenter)
            self.lbl_invest.setFont(QFont("MS Shell Dlg 2", 15))
            self.lbl_invest.setStyleSheet("color: rgb(255, 255, 255)")
        else:
            self.Atualizar()
        dmb.close_connection()

    ###########################################

    def ColocarComboBoxClientesProduto(self):
        deb = BancoDeDados()
        deb.connect()
        lista = []
        for linha in deb.ler_tabela_estoque():
            lista.append(linha[0])
        self.comboBox_cliente_produto.addItems(lista)
        deb.close_connection()

    def ColocarComboBoxClientesCliente(self):
        deb = BancoDeDados()
        deb.connect()
        lista = []
        for linha in deb.ler_tabela_divida():
            lista.append(linha[1])
        self.comboBox_cliente_cliente.addItems(lista)
        self.comboBox_dividas_cliente.addItems(lista)
        deb.close_connection()

    def Atualizar(self):
        self.lineEdit_estoque_produto.clear()
        self.lineEdit_estoque_valorVenda.clear()
        self.lineEdit_estoque_quantidade.clear()
        self.lineEdit_estoque_valorCompra.clear()
        self.lineEdit_estoque_remover.setText('0')
        self.lineEdit_dividas_valorRecebido.clear()

        self.label_dividas_total.setText('')
        self.label_dividas_troco.setText('')

        self.tableWidget_estoque_editar.reset()
        self.tableWidget_estoque_remover.reset()
        self.tableWidget_estoque_adicionar.reset()
        self.tableWidget_balanco_LI.reset()
        self.tableWidget_cliente_venda.reset()
        self.tableWidget_cliente_tabela.reset()
        self.tableWidget_dividas.reset()

        self.ColocarTabelaClienteVenda()
        self.ColocarTabelaLucroInvestimento()
        self.ColocarTabelaEstoque()
        self.ColocarTabelaCliente()
        self.ColocarTabelaDivida()

        self.comboBox_cliente_produto.clear()
        self.ColocarComboBoxClientesProduto()
        self.comboBox_cliente_cliente.clear()
        self.comboBox_dividas_cliente.clear()
        self.ColocarComboBoxClientesCliente()


if __name__ == "__main__":
    db = BancoDeDados()
    db.connect()
    db.criar_tabela_estoque()
    db.criar_tabela_dividas()
    db.criar_tabela_clientes()
    db.criar_tabela_lucro_investimento()
    db.criar_tabela_cliente_venda()
    db.apagar_tabela_clientes_dia()
    db.close_connection()

    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    app.exec()
