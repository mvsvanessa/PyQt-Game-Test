import sys
from PyQt5.QtWidgets import QApplication, QMainWindow

class Janela (QMainWindow):
    def __init__(self):
        super().__init__()

        # em px
        self.topo = 300 # distância que vai ficar do topo
        self.esquerda = 300 # distância que vai ficar da esquerda
        self.largura = 800
        self.altura = 600
        self.titulo = "Primeira Janela"
        self.carregar_janela()

    def carregar_janela(self):
        self.setGeometry(self.esquerda, self.topo, self.largura, self.altura)
        self.setWindowTitle(self.titulo)
        self.show()

app = QApplication(sys.argv)
j = Janela()
sys.exit(app.exec_())




