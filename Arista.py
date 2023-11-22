from PyQt5.QtWidgets import QDialog, QVBoxLayout, QLabel, QLineEdit, QPushButton

class MiDialogo(QDialog):
    def __init__(self, parent=None):
        super().__init__(parent)

        self.valor1 = None
        self.valor2 = None

        self.setWindowTitle('Ingresar Valores')
        layout = QVBoxLayout(self)

        label1 = QLabel('Valor 1:')
        self.edit1 = QLineEdit(self)
        layout.addWidget(label1)
        layout.addWidget(self.edit1)

        label2 = QLabel('Valor 2:')
        self.edit2 = QLineEdit(self)
        layout.addWidget(label2)
        layout.addWidget(self.edit2)

        btnAceptar = QPushButton('Aceptar', self)
        btnAceptar.clicked.connect(self.aceptar_valores)
        layout.addWidget(btnAceptar)

    def aceptar_valores(self):
        # Obtener los valores de los QLineEdit
        valor1 = self.edit1.text()
        valor2 = self.edit2.text()

        # Puedes realizar validaciones aquí antes de aceptar los valores

        # Almacenar los valores como atributos de la instancia
        self.valor1 = valor1
        self.valor2 = valor2

        # Cerrar el cuadro de diálogo con aceptación
        self.accept()
