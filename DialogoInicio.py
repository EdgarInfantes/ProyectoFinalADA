from PyQt5.QtWidgets import QDialog, QVBoxLayout,QHBoxLayout, QLabel, QLineEdit, QPushButton
from PyQt5.QtWidgets import QApplication, QWidget, QMessageBox
from PyQt5.QtGui import QIntValidator


class dialogoNodoInicio(QDialog):
    def __init__(self, parent=None):
        super().__init__(parent)

        self.valor1 = None
        self.setWindowTitle('Comenzando desde el nodo...')
        layout = QHBoxLayout(self)

        label1 = QLabel('Ingresa ID del Nodo:')
        self.edit1 = QLineEdit(self)
        self.edit1.setValidator(QIntValidator())
        layout.addWidget(label1)
        layout.addWidget(self.edit1)
      

        btnAceptar = QPushButton('Aceptar', self)
        btnAceptar.clicked.connect(self.aceptar_valores)
        layout.addWidget(btnAceptar)

    def aceptar_valores(self):
        # Obtener los valores de los QLineEdit
        valor1 = self.edit1.text()
        # Almacenar los valores como atributos de la instancia
        self.valor1 = valor1

        if self.valor1 != '':
        # Cerrar el cuadro de diálogo con aceptación
            self.accept()
        else:
            alerta = QMessageBox()
            alerta.setIcon(QMessageBox.Warning)
            alerta.setText("Error")
            alerta.setInformativeText("Ingrese los datos correctos.")
            alerta.setWindowTitle("Alerta")
            alerta.exec_()