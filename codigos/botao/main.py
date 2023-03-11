import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton, QToolTip


class Janela(QMainWindow):
    def __init__(self):
        super().__init__()

        # definições da tela em px
        self.topo = 300  # distância que vai ficar do topo
        self.esquerda = 300  # distância que vai ficar da esquerda
        self.largura = 750
        self.altura = 500
        self.titulo = "Primeira Janela"

        # parâmetros e objeto do botão
        botao_1 = QPushButton("Botão 1 ", self)
        botao_1.move(150, 200)
        botao_1.resize(200, 100)
        botao_1.setStyleSheet('QPushButton {background-color:#1E90FF; font:bold; font-size:20px}')
        botao_1.clicked.connect(self.botao_1_click)

        # parâmetros e objeto do botão
        botao_2 = QPushButton("Botão 2", self)
        botao_2.move(400, 200)
        botao_2.resize(200, 100)
        botao_2.setStyleSheet('QPushButton {background-color:#40E0D0; font:bold; font-size:20px}')
        botao_2.clicked.connect(self.botao_2_click)

        self.carregar_janela()

    def carregar_janela(self):
        self.setGeometry(self.esquerda, self.topo, self.largura, self.altura)
        self.setWindowTitle(self.titulo)
        self.show()

    def botao_1_click(self):
        print("O botão 1 foi selecionado")

    def botao_2_click(self):
        print("=========================")


app = QApplication(sys.argv)
j = Janela()
sys.exit(app.exec_())
