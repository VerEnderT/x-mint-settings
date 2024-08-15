import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QTextBrowser, QVBoxLayout, QWidget, QLabel
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QIcon, QPixmap

class LicenseViewer(QMainWindow):
    def __init__(self, app_name, author, copying_file_path, homepage):
        super().__init__()
        self.setWindowTitle("Über X-Mint settings")
        faktor = app.desktop().height()/720
        breite = int(330 * faktor)
        hoehe = int(200 * faktor)
        bts=int(32 * faktor)
        sts=int(12 * faktor)
        x_pos=int((app.desktop().width()-breite)/2)
        y_pos=int((app.desktop().height()-hoehe)/2)
        self.setGeometry(x_pos, y_pos, breite, hoehe)
        self.setGeometry(100, 100, 300, 200)
        self.setWindowIcon(QIcon('./images/logo.png')) 
        self.setMinimumSize(breite, hoehe)  # Festlegen der Größe auf 600x400 Pixel
        self.setFixedWidth(breite)
        self.setStyleSheet("background: rgba(80,80, 80, 00);")

        self.sslabel=str("""
            QLabel {
            font-size: """ + str(sts) + """px; 
            text-align: left;      
            border-radius: 10px;
            background-color: #1a1a1a;
            border: 2px solid #1a1a1a;
            padding-top: 2px;
            padding-left: 5px;
            padding-right: 5px;
            padding-bottom: 2px;
            color: white;
            }
            QTextBrowser {
            font-size: """ + str(sts) + """px; 
            text-align: left;      
            border-radius: 10px;
            background-color: #1a1a1a;
            border: 2px solid #1a1a1a;
            padding-top: 2px;
            padding-left: 5px;
            padding-right: 5px;
            padding-bottom: 2px;
            color: white;
            }
            """)


        central_widget = QWidget(self)
        self.setCentralWidget(central_widget)

        layout = QVBoxLayout(central_widget)

        # Erstelle ein Label für den Titel
        #title_label = QLabel(f"\n{app_name}\n(2023)\n <a href='{homepage}'>{app_name} Homepage</a> \n\nvon {author}\n unter der Gnu Public Licence Version 3\n")
        title_label = QLabel(f"<b  style='color: #00b99f; font-size: {bts}px;'> {app_name} </b> <br><a href='{homepage}' style='color: yellow; text-decoration: bold;'>{homepage}</a> <br><br> Autor: {author}")
       
        title_label.setOpenExternalLinks(True)  # Öffnen von externen Links erlauben
 
        title_label.setAlignment(Qt.AlignCenter)
        title_label.setStyleSheet(self.sslabel)
        layout.addWidget(title_label)

        # Erstelle einen Textbrowser
        text_browser = QTextBrowser()
        layout.addWidget(text_browser)
        text_browser.setStyleSheet(self.sslabel)
        text_browser.verticalScrollBar().setStyleSheet("QScrollBar:vertical { width: 5px; }")


        # Lade den Inhalt der COPYING-Datei
        with open(copying_file_path, 'r', encoding='utf-8') as file:
            license_text = file.read()

        # Zeige den Lizenztext im Textbrowser an
        text_browser.setPlainText(license_text)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    app_name = "X-Mint settings"
    author = "VerEnderT aka Frank Maczollek"
    copying_file_path = "COPYING"  # Passe den Dateipfad an
    homepage = "http://verlinuxt.sytes.net"

    window = LicenseViewer(app_name, author, copying_file_path, homepage)
    window.show()

    sys.exit(app.exec_())
