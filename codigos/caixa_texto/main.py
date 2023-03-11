import sys
from PyQt5.QtWidgets import QApplication, \
    QMainWindow, QPushButton, QToolTip, \
    QLabel, QLineEdit
from PyQt5 import QtGui


class Janela(QMainWindow):
    def __init__(self):
        super().__init__()

        # definições da tela em px
        self.topo = 100  # distância que vai ficar do topo
        self.esquerda = 200  # distância que vai ficar da esquerda
        self.largura = 750
        self.altura = 900
        self.titulo = "Primeira Janela"

        # parâmetros e objeto da caixa de texto
        self.txt_edit = QLineEdit(self)
        self.txt_edit.move(250,20)
        self.txt_edit.resize(250, 50)


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

        # parâmetros e objeto do botão
        btn_3 = QPushButton("Enviar texto", self)
        btn_3.move(270, 350)
        btn_3.resize(200, 100)
        btn_3.setStyleSheet('QPushButton {background-color:#B0C4DE; font:bold; font-size:20px}')
        btn_3.clicked.connect(self.botao_3_click)


        # parâmetros e objetos do label
        self.lbl_1 = QLabel(self)
        self.lbl_1.setText("Pressione um botão:")
        self.lbl_1.resize(400, 25) # largura, altura
        self.lbl_1.move(250, 100) # esquerda, cima
        self.lbl_1.setStyleSheet('QLabel {font:bold;font-size:25px;}')

        # label para as imagens
        self.lbl_img = QLabel(self)
        self.lbl_img.resize(500, 300)
        self.lbl_img.move(250, 475)
        self.lbl_img.setPixmap(QtGui.QPixmap('thinking.png'))

        # parâmetros e objetos do label
        self.lbl_2 = QLabel(self)
        self.lbl_2.setText("Opção")
        self.lbl_2.resize(400, 25)  # largura, altura
        self.lbl_2.move(300, 800)  # esquerda, cima
        self.lbl_2.setStyleSheet('QLabel {font:bold;font-size:25px;}')

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

    def botao_3_click(self):
        conteudo = self.txt_edit.text()
        self.lbl_2.setText(conteudo)
        self.lbl_2.setStyleSheet('QLabel {font:bold;font-size:25px;color:#1E90FF;}')



app = QApplication(sys.argv)
j = Janela()
sys.exit(app.exec_())
