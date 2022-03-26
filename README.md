# wordcut
It's a way to get images from a folder, compact, format and send directly to a word (.doc) file.

MainDIsplay.py is the Pyqt5 display file
Modulo_de_funcoes.py is the logic
test.py is for tests without using GUI

REMEMBER: When u create a .exe with Pyinstaller, go for a .spec file and swap the data for responsivity:

# -*- mode: python ; coding: utf-8 -*-


block_cipher = None

#create the finder here
arquivos = [
    ('./*.ico', '.'),
    ('./*.png', '.'),
]


a = Analysis(['main_display.py'],
             pathex=[],
             binaries=[],
             datas=arquivos, #put it here and do pyinstaller main_display.spec in your terminal again (do not open the .exe before it)!
             hiddenimports=[],
             hookspath=[],
             hooksconfig={},
             runtime_hooks=[],
             excludes=[],
             win_no_prefer_redirects=False,
             win_private_assemblies=False,
             cipher=block_cipher,
             noarchive=False)
pyz = PYZ(a.pure, a.zipped_data,
             cipher=block_cipher)

exe = EXE(pyz,
          a.scripts,
          a.binaries,
          a.zipfiles,
          a.datas,  
          [],
          name='main_display',
          debug=False,
          bootloader_ignore_signals=False,
          strip=False,
          upx=True,
          upx_exclude=[],
          runtime_tmpdir=None,
          console=False,
          disable_windowed_traceback=False,
          target_arch=None,
          codesign_identity=None,
          entitlements_file=None )
