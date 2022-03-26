import sys
import webbrowser
import PyQt5
from pkg_resources import resource_filename
from modulo_de_funcoes import convert_image
from design import *
from PyQt5.QtWidgets import QMainWindow, QApplication, QFileDialog, QMessageBox
from PyQt5.QtGui import QPixmap
import shutil
import os


class Novo(QMainWindow, Ui_MainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)
        super().setupUi(self)
        
        #janela de popup caso alguém tente criar denovo na mesma pasta (fonte https://www.techwithtim.net/tutorials/pyqt5-tutorial/messageboxes/)
        self.msg = QMessageBox()
        self.msg.setWindowTitle("Pasta incompatível")
        self.msg.setText("Favor selecionar pasta com apenas fotos!")
        self.msg.setInformativeText("Verificar se a pasta contém arquivos somente de fotos e caso sim, confirmar se já não houve a conversão.")
        self.msg.setIcon(QMessageBox.Warning)
        self.msg.setStandardButtons(QMessageBox.Ok)
        self.msg.setWindowIcon(QtGui.QIcon(os.path.join(os.path.dirname(__file__), 'icon.png')))
        
        
        #janela de popup caso alguém tente criar denovo na mesma pasta
        self.done = QMessageBox()
        self.done.setWindowTitle("Formatado com sucesso!")
        self.done.setText("Arquivo formatado com sucesso")
        self.done.setInformativeText("Verificar na pasta de origem das fotos.")
        self.done.setIcon(QMessageBox.Information)
        self.done.setStandardButtons(QMessageBox.Ok)
        self.done.setWindowIcon(QtGui.QIcon(os.path.join(os.path.dirname(__file__), 'icon.png')))
        
        self.btnEscolherPasta.clicked.connect(self.escolher_pasta)
        self.btnFormatar.clicked.connect(self.formatar)
        self.radioButton1.clicked.connect(self.qual_formato)
        self.radioButton2.clicked.connect(self.qual_formato)
        self.pushButton.clicked.connect(self.open_webbrowser)
        self.radioButton1.setChecked(True)
        self.pixmapdouble = QPixmap(resource_filename(__name__, 'double.ico'))
        self.double_label.setPixmap(self.pixmapdouble)
        self.pixmaptriple = QPixmap(resource_filename(__name__, 'triple.PNG'))
        self.triple_label.setPixmap(self.pixmaptriple)
        self.pixmapcamera = QPixmap(os.path.join(os.path.dirname(__file__), 'cam.png'))
        self.label_camera.setPixmap(self.pixmapcamera)
        self.setWindowIcon(QtGui.QIcon(os.path.join(os.path.dirname(__file__), 'icon.png')))
        self.inputAbrirArquivo.setDisabled(True)
        self.formato = 0
        
        #formatação css
        self.btnEscolherPasta.setStyleSheet(
            "QPushButton"
            "{"
            'align-items: center;'
            'appearance: none;'
            'background-color: #fff;'
            'border: 1px solid #dbdbdb;'
            'border-radius: .375em;'
            'box-shadow: none;'
            'box-sizing: border-box;'
            'color: #363636;'
            'cursor: pointer;'
            'display: inline-flex;'
            'font-family: BlinkMacSystemFont,-apple-system,"Segoe UI",Roboto,Oxygen,Ubuntu,Cantarell,"Fira Sans","Droid Sans","Helvetica Neue",Helvetica,Arial,sans-serif;'
            'font-size: 1rem;'
            'height: 2em;'
            'justify-content: center;'
            'line-height: 1.5;'
            'padding: calc(.5em - 1px) 1em;'
            'position: relative;'
            'text-align: center;'
            'user-select: none;'
            '-webkit-user-select: none;'
            'touch-action: manipulation;'
            'vertical-align: top;'
            'white-space: nowrap;'
            '}'
            'QPushButton::active' 
            '{'
            'border-color: #4a4a4a;'
            'outline: 0;'
            '}'

            'QPushButton::focus' 
            '{'
            'border-color: #485fc7;'
            'outline: 0;'
            '}'

            'QPushButton::hover' 
            '{'
            'border-color: #b5b5b5;'
            '}'

            'QPushButton::focus::not(:active)' 
            '{'
            'box-shadow: rgba(72, 95, 199, .25) 0 0 0 .125em;'
            '}'          
        )
        self.btnFormatar.setStyleSheet(
            "QPushButton"
            "{"
            'align-items: center;'
            'appearance: none;'
            'background-color: #fff;'
            'border: 1px solid #dbdbdb;'
            'border-radius: .375em;'
            'box-shadow: none;'
            'box-sizing: border-box;'
            'color: #363636;'
            'cursor: pointer;'
            'display: inline-flex;'
            'font-family: BlinkMacSystemFont,-apple-system,"Segoe UI",Roboto,Oxygen,Ubuntu,Cantarell,"Fira Sans","Droid Sans","Helvetica Neue",Helvetica,Arial,sans-serif;'
            'font-size: 1rem;'
            'height: 2em;'
            'justify-content: center;'
            'line-height: 1.5;'
            'padding: calc(.5em - 1px) 1em;'
            'position: relative;'
            'text-align: center;'
            'user-select: none;'
            '-webkit-user-select: none;'
            'touch-action: manipulation;'
            'vertical-align: top;'
            'white-space: nowrap;'
            '}'
            'QPushButton::active' 
            '{'
            'border-color: #4a4a4a;'
            'outline: 0;'
            '}'

            'QPushButton::focus' 
            '{'
            'border-color: #485fc7;'
            'outline: 0;'
            '}'

            'QPushButton::hover' 
            '{'
            'border-color: #b5b5b5;'
            '}'

            'QPushButton::focus::not(:active)' 
            '{'
            'box-shadow: rgba(72, 95, 199, .25) 0 0 0 .125em;'
            '}'          
        )
        self.inputAbrirArquivo.setStyleSheet(
            '* {background: white}'
        )
        self.centralwidget.setStyleSheet(
            '* {background: white; color: #000}'
        )
        self.pushButton.setStyleSheet(
            '* {background: transparent}'
        )
        self.pushButton_2.setStyleSheet(
            '* {background: transparent}'
        )
        
    #link pro insta    
    def open_webbrowser(self):
        webbrowser.open('https://www.instagram.com/wagnermonstro51/')
    
    #seleciona a pasta das fotos   
    def escolher_pasta(self):
        pasta_escolhida = QFileDialog.getExistingDirectory(
            self.centralwidget,
            'Escolher pasta',
            r'C:',
            #options=QFileDialog.DontUseNativeDialog
        )
        try:
            self.inputAbrirArquivo.setText(pasta_escolhida.replace('\\', '/'))
            return pasta_escolhida
        except Exception as e:
            pass
        
    #checkbox do formato desejado    
    def qual_formato(self):
        if self.radioButton1.isChecked():
            self.formato = 0      
        if self.radioButton2.isChecked():
            self.formato = 1      
       
    #formata e joga no word    
    def formatar(self):
        try:
            caminho = str(self.inputAbrirArquivo.text())
            formato = self.formato
            convert_image(caminho, formato)
            y = self.done.exec_()
        except Exception as e:
            x = self.msg.exec_()
            try:
                temp = os.path.join(caminho, 'temporary_folder')
                shutil.rmtree(temp)
            except Exception as e:
                pass
            
 


if __name__ == '__main__':
    qt = QApplication(sys.argv)
    novo = Novo()
    novo.show()
    qt.exec_()
