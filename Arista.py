from PyQt5.QtWidgets import QDialog, QVBoxLayout,QHBoxLayout, QLabel, QLineEdit, QPushButton

class MiDialogo(QDialog):
    def __init__(self, parent=None):
        super().__init__(parent)

        self.valor1 = None
        self.valor2 = None
        self.valor3=None
        self.setWindowTitle('Ingresar Valores')
        layout = QHBoxLayout(self)

        label1 = QLabel('Nodo Padre:')
        self.edit1 = QLineEdit(self)
        layout.addWidget(label1)
        layout.addWidget(self.edit1)

        label2 = QLabel('Nodo Hijo:')
        self.edit2 = QLineEdit(self)
        layout.addWidget(label2)
        layout.addWidget(self.edit2)

        label3 = QLabel('Peso:')
        self.edit3 = QLineEdit(self)
        layout.addWidget(label3)
        layout.addWidget(self.edit3)

        btnAceptar = QPushButton('Aceptar', self)
        btnAceptar.clicked.connect(self.aceptar_valores)
        layout.addWidget(btnAceptar)

    def aceptar_valores(self):
        # Obtener los valores de los QLineEdit
        valor1 = self.edit1.text()
        valor2 = self.edit2.text()
        valor3=self.edit3.text()
        # Almacenar los valores como atributos de la instancia
        self.valor1 = valor1
        self.valor2 = valor2
        self.valor3= valor3
        # Cerrar el cuadro de diálogo con aceptación
        self.accept()
