# wordcut
It's a way to get images from a folder, compact, format and send directly to a word (.doc) file.

MainDIsplay.py is the Pyqt5 display file
Modulo_de_funcoes.py is the logic
test.py is for tests without using GUI

REMEMBER: When u create a .exe with Pyinstaller, go for a .spec file and swap the data for responsivity:

#-*- mode: python ; coding: utf-8 -*-


block_cipher = None

#create the finder here
arquivos = [
    ('./*.ico', '.'),
    ('./*.png', '.'),
]


a = Analysis(datas=arquivos) #put it here and do pyinstaller main_display.spec in your terminal again (do not open the .exe before it)!
             
