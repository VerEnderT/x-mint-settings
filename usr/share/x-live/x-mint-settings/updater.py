import sys 
import os
import subprocess
from PyQt5.QtCore import *
from PyQt5.QtGui import QIcon, QPixmap
from PyQt5.QtWidgets import (QApplication, QComboBox, QHBoxLayout, QLabel,
                             QLineEdit, QListWidget, QPushButton, QSlider, 
                             QVBoxLayout, QWidget, QMessageBox)

class MyWidget(QWidget):
    def __init__(self):
        super().__init__()

        self.initUI()

    def initUI(self):


        faktor = app.desktop().height()/720
        self.faktor = app.desktop().height()/720
        breite = int(250 * faktor)
        hoehe = int(60 * faktor)
        bts=int(16 * faktor)
        sts=int(24 * faktor)
        btn_sel_color = '#1f8973'
        pos_x = int((app.desktop().width()-breite)/2)
        pos_y = int((app.desktop().height()-hoehe)/2)
        # color yellow #635313
        # color green #0ca057
      
        #  StyleSheet 
        
        self.ssbtn1=str("""
            QWidget {
            background-color: #130343;
            }
            QLabel {
            font-size: """ + str(sts) + """px; 
            text-align: left;      
            border-radius: 10px;
            background-color: """ + btn_sel_color  + """;
            border: 2px solid """ + btn_sel_color  + """;
            padding-top: 2px;
            padding-left: 5px;
            padding-right: 5px;
            padding-bottom: 2px;
            color: white;
            }
            """)
            

        # Erstelle ein Layout für das Hauptfenster
        layout = QVBoxLayout()
        self.label = QLabel("bitte warten", self)
        self.label.setStyleSheet(self.ssbtn1)
        layout.addWidget(self.label)

        # Setze das Layout für das Hauptfenster
        self.setLayout(layout)

        self.setWindowTitle('ComboBox Beispiel')
        self.setGeometry(pos_x, pos_y,breite,hoehe)
        self.setWindowIcon(QIcon.fromTheme('settings'))  # Setze das systemweite Theme-Icon als Fenstericon
        self.setWindowTitle("X-Mint Einstellungstool")
        self.setMinimumSize(breite, hoehe)  # Festlegen der Größe auf 600x400 Pixel
        self.setFixedWidth(breite)
        self.setStyleSheet("background: rgba(80,80, 80, 00);")  # Hintergrundfarbe festlegen

        self.setAttribute(Qt.WA_TranslucentBackground)
        self.setWindowFlags(self.windowFlags() | Qt.FramelessWindowHint)  # Entfernt die Fensterdekoration
        self.show()
        self.start_upgrade()


    def start_upgrade(self):
        self.start_warten()
        x = self.shell_cmd("pkexec sudo /usr/bin/apt update 2>/dev/null")

        updates = self.shell_cmd(" apt list --upgradable 2>/dev/null | grep 'aktu'")
        count = 0
        updates_list = ""
        upgradable_list = []
        if updates != None :
            count = len(updates)
            for x in updates:
                updates_list = updates_list + x[0:x.find("/")] + "\n"
                upgradable_list.append(x[0:x.find("/")])
        self.kill_warten()
        print(upgradable_list)
        for x in upgradable_list:

            self.label.setText(x+" wird aktuallisiert !")
            os.system("sudo apt install "+x+" -y")

        sys.exit()


    def shell_cmd(self, command):
        try:
            # Führe den übergebenen Befehl aus und erfasse die Ausgabe
            result = subprocess.check_output(command, shell=True, universal_newlines=True)
            
            # Teile die Ausgabe in Zeilen auf
            output_lines = result.splitlines()
            
            return output_lines
        except subprocess.CalledProcessError as e:
            #print(f"Fehler beim Ausführen des Befehls: {e}")
            return None
        
    def start_warten(self):
        print("start")
        subprocess.Popen("python3 ./bitte_warten.py", shell=True)

    def kill_warten(self):
        print("stop")
        subprocess.Popen("pkill -f bitte_warten.py", shell=True)   

if __name__ == '__main__':
    app = QApplication(sys.argv)
    widget = MyWidget()
    sys.exit(app.exec_())
