import sys
import networkx as nx
import matplotlib.pyplot as plt
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QHBoxLayout, QGraphicsView, QGraphicsScene, QLabel, QPushButton, QFrame
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QPixmap, QImage

class Node:
    def __init__(self, x, y):
        self.x = x
        self.y = y

class Lienzo:
    def __init__(self):
        self.graph = nx.Graph()
        self.pos = {}
        self.fig, self.ax = plt.subplots()
        self.cid = self.fig.canvas.mpl_connect('button_press_event', self.MouseClick)
        self.ax.set_xlim(0, 1)
        self.ax.set_ylim(0, 1)
        self.ax.axis('off')  # Desactivar ejes
        self.rect = plt.Rectangle((0, 0), 1, 1, linewidth=2, edgecolor='black', facecolor='none')
        self.ax.add_patch(self.rect)

    def MouseClick(self, event):
        if event.xdata is not None and event.ydata is not None:
            node_id = len(self.graph.nodes) + 1
            self.graph.add_node(node_id)
            self.pos[node_id] = (event.xdata, event.ydata)
            self.DibujarGrafo()

    def DibujarGrafo(self):
        # Guardar temporalmente el color del borde del rectángulo
        original_edgecolor = self.rect.get_edgecolor()

        self.ax.clear()
        self.ax.set_xlim(0, 1)
        self.ax.set_ylim(0, 1)
        self.ax.axis('off')  # Desactivar ejes
        self.rect = plt.Rectangle((0, 0), 1, 1, linewidth=2, edgecolor='black', facecolor='none')
        self.ax.add_patch(self.rect)

        # Dibujar el grafo después de restaurar el color del borde
        nx.draw(self.graph, pos=self.pos, with_labels=True, font_weight='bold', ax=self.ax)

        # Restaurar el color del borde original
        self.rect.set_edgecolor(original_edgecolor)

        plt.draw()

class MainWindow(QWidget):
    def __init__(self):
        super().__init__()

        # Crear contenedor vertical para contOpciones, contResults y contLienzo
        contMain = QWidget()
        contMain_layout = QVBoxLayout(contMain)

        # Crear contenedor horizontal para contResults y contLienzo
        contResultsLienzo = QWidget()
        contResultsLienzo_layout = QHBoxLayout(contResultsLienzo)

        # Crear contenedor vertical para contOpciones
        contOpciones = QWidget()
        contOpciones_layout = QVBoxLayout(contOpciones)

        # Agregar algunos botones a contOpciones (ajustar según sea necesario)
        buttonA = QPushButton('Botón A')
        buttonB = QPushButton('Botón B')
        contOpciones_layout.addWidget(buttonA)
        contOpciones_layout.addWidget(buttonB)

        # Agregar contOpciones a la capa principal
        contMain_layout.addWidget(contOpciones)

        # Agregar línea divisoria vertical entre contOpciones y contResults
        line1 = QFrame(self)
        line1.setFrameShape(QFrame.VLine)
        line1.setFrameShadow(QFrame.Sunken)
        contMain_layout.addWidget(line1)

        # Crear contenedor vertical para contResults
        contResults = QWidget()
        contResults_layout = QVBoxLayout(contResults)

        # Agregar widgets al contenedor de resultados
        label1 = QLabel('Resultados')
        btnLimpiar = QPushButton('Limpiar')
        contResults_layout.addWidget(label1)
        contResults_layout.addWidget(btnLimpiar)

        # Tamaño fijo para el contenedor1
        contResults.setFixedWidth(300)

        # Agregar contResults a la capa principal
        contResultsLienzo_layout.addWidget(contResults)

        # Agregar línea divisoria vertical entre contResults y contLienzo
        line2 = QFrame(self)
        line2.setFrameShape(QFrame.VLine)
        line2.setFrameShadow(QFrame.Sunken)
        contResultsLienzo_layout.addWidget(line2)

        # Crear contenedor vertical para contLienzo
        contLienzo = QWidget()
        contLienzo_layout = QVBoxLayout(contLienzo)

        contLienzo.setMinimumWidth(500)
        contLienzo.setMinimumHeight(500)

        # Agregar widgets al contenedor del Lienzo
        label2 = QLabel('Lienzo')
        contLienzo_layout.addWidget(label2)

        # Crear instancia de la clase Lienzo y agregarla al contenedor del Lienzo
        self.lienzo = Lienzo()
        contLienzo_layout.addWidget(self.lienzo.fig.canvas)

        # Agregar contLienzo a la capa principal
        contResultsLienzo_layout.addWidget(contLienzo)

        # Agregar contResultsLienzo a la capa principal
        contMain_layout.addWidget(contResultsLienzo)

        # Configurar el diseño de la ventana principal
        main_layout = QVBoxLayout(self)
        main_layout.addWidget(contMain)

        self.setGeometry(100, 100, 800, 400)
        self.setWindowTitle('Grafos')

    def resizeEvent(self, event):
        super().resizeEvent(event)

    def add_node(self, node):
        # Agregar el nodo al grafo y actualizar el gráfico
        node_id = len(self.lienzo.graph.nodes) + 1
        self.lienzo.graph.add_node(node_id)
        self.lienzo.pos[node_id] = (node.x, node.y)
        self.lienzo.DibujarGrafo()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    main_window = MainWindow()
    main_window.show()
    sys.exit(app.exec_())
