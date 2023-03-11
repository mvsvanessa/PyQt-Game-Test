import sys
from PyQt5.QtWidgets import QApplication, \
    QMainWindow, QPushButton, QToolTip, QLabel
from PyQt5 import QtGui


class Janela(QMainWindow):
    def __init__(self):
        super().__init__()

        # definições da tela em px
        self.topo = 300  # distância que vai ficar do topo
        self.esquerda = 300  # distância que vai ficar da esquerda
        self.largura = 750
        self.altura = 700
        self.titulo = "Primeira Janela"

        # parâmetros e objeto do botão
        btn_1 = QPushButton("Botão 1 ", self)
        btn_1.move(150, 200)
        btn_1.resize(200, 100)
        btn_1.setStyleSheet('QPushButton {background-color:#1E90FF; font:bold; font-size:20px}')
        btn_1.clicked.connect(self.botao_1_click)

        # parâmetros e objeto do botão
        btn_2 = QPushButton("Botão 2", self)
        btn_2.move(400, 200)
        btn_2.resize(200, 100)
        btn_2.setStyleSheet('QPushButton {background-color:#40E0D0; font:bold; font-size:20px}')
        btn_2.clicked.connect(self.botao_2_click)

        # parâmetros e objetos do label
        self.lbl_1 = QLabel(self)
        self.lbl_1.setText("Pressione um botão:")
        self.lbl_1.resize(400, 25) # largura, altura
        self.lbl_1.move(250, 50)
        self.lbl_1.setStyleSheet('QLabel {font:bold;font-size:25px;}')

        # label para as imagens
        self.lbl_img = QLabel(self)
        self.lbl_img.resize(500, 300)
        self.lbl_img.move(250, 350)
        self.lbl_img.setPixmap(QtGui.QPixmap('thinking.png'))

        self.carregar_janela()

    def carregar_janela(self):
        self.setGeometry(self.esquerda, self.topo, self.largura, self.altura)
        self.setWindowTitle(self.titulo)
        self.show()

    def botao_1_click(self):
        print("O botão 1 foi selecionado")
        self.lbl_1.setText("Botão 1 selecionado")
        self.lbl_1.setStyleSheet('QLabel {font:bold;font-size:25px;color:#1E90FF;}')
        self.lbl_img.setPixmap(QtGui.QPixmap('spa.png'))

    def botao_2_click(self):
        print("=========================")
        self.lbl_1.setText("Botão 2 selecionado")
        self.lbl_1.setStyleSheet('QLabel {font:bold;font-size:25px;color:#40E0D0;}')
        self.lbl_img.setPixmap(QtGui.QPixmap('space.png'))


app = QApplication(sys.argv)
j = Janela()
sys.exit(app.exec_())
