import sys 
import os
import re
import time
import subprocess
from PyQt5.QtCore import *
from PyQt5.QtGui import QIcon, QPixmap, QCursor
from PyQt5.QtWidgets import (QApplication, QComboBox, QHBoxLayout, QLabel,
                             QLineEdit, QListWidget, QPushButton, QSlider, 
                             QVBoxLayout, QWidget, QMessageBox, QScrollArea)

# Pfad zum gewünschten Arbeitsverzeichnis # Das Arbeitsverzeichnis festlegen
arbeitsverzeichnis = os.path.expanduser('/usr/share/x-live/x-mint-settings')

os.chdir(arbeitsverzeichnis)




class MyWidget(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
    
        #  skalierungsberechnung
        faktor = app.desktop().height()/780
        self.faktor = faktor
        breite = int(680 * faktor)
        hoehe = int(570 * faktor)
        bts=int(16 * faktor)
        # sts=int(14 * faktor)
        self.sts=int(14 * faktor)
        self.akzent_color()
        self.cursor_theme = None
        self.updates = None
        self.updates_checked = 0
        self.installed_apps=str(self.shell_cmd("apt list --installed 2>/dev/null"))
      
        self.ssbtn=str("""
            QWidget {
            background-color: #130343;
            }
            QPushButton {
            font-size: """ + str(self.sts) + """px; 
            text-align: left;      
            border-radius: """+ str(int(8*self.faktor))+""";
            background-color: #333333;
            border: 2px solid #333333;
            padding-top: 2px;
            padding-left: 5px;
            padding-right: 5px;
            padding-bottom: 2px;
            color: white;
            }
            QLabel {
            font-size: """ + str(self.sts) + """px; 
            text-align: centre;      
            border-radius: """+ str(int(8*self.faktor))+""";
            background-color: #333333;
            border: 2px solid #333333;
            color: white;
            }
            QPushButton:hover {
            font-size: """ + str(int(int(self.sts)/14*16)) + """px;  
            background-color: #1b1b1b;
            border: 2px solid #1b1b1b;
            }
            """)

        self.ssbtn_c=str("""
            QWidget {
            background-color: #130343;
            }
            QPushButton {
            font-size: """ + str(int(self.sts*0.95)) + """px; 
            text-align: centre;      
            border-radius: """+ str(int(8*self.faktor))+""";
            background-color: #333333;
            border: 2px solid #333333;
            padding-top: 2px;
            padding-left: 5px;
            padding-right: 5px;
            padding-bottom: 2px;
            color: white;
            }
            QPushButton:hover {
            font-size: """ + str(int(int(self.sts*1))) + """px;  
            background-color: #1b1b1b;
            border: 0px solid #1b1b1b;
            padding-left: 1px;
            padding-right: 1px;
            }
            """)
        
        self.sscat_btn=str("""
            QWidget {
            background-color: #130343;
            }
            QPushButton {
            font-size: """ + str(self.sts) + """px; 
            text-align: left;      
            border-radius: """+ str(int(8*self.faktor))+""";
            background-color: #333333;
            border: 2px solid #333333;
            padding-top: 2px;
            padding-left: 5px;
            padding-right: 5px;
            padding-bottom: 2px;
            color: white;
            }
            QPushButton:hover {
            font-size: """ + str(int(int(self.sts)/14*15)) + """px;  
            background-color: #444444;
            border: 0px solid #444444;
            }
            """)

        self.sscat_btn_xs=str("""
            QWidget {
            background-color: #130343;
            }
            QPushButton {
            font-size: """ + str(int(self.sts*0.8)) + """px; 
            text-align: left;      
            border-radius: """+ str(int(8*self.faktor))+""";
            background-color: #333333;
            border: 2px solid #333333;
            padding-top: 2px;
            padding-left: 5px;
            padding-right: 5px;
            padding-bottom: 2px;
            color: white;
            }
            QPushButton:hover {
            font-size: """ + str(int(int(self.sts)*0.9)) + """px;  
            background-color: #444444;
            border: 0px solid #444444;
            }
            """)

        self.sscat_btn_warn=str("""
            QWidget {
            background-color: #130343;
            }
            QPushButton {
            font-size: """ + str(self.sts) + """px; 
            text-align: left;      
            border-radius: """+ str(int(8*self.faktor))+""";
            background-color: #d26e00;
            border: 2px solid #d26e00;
            padding-top: 2px;
            padding-left: 5px;
            padding-right: 5px;
            padding-bottom: 2px;
            color: white;
            }
            QPushButton:hover {
            font-size: """ + str(int(int(self.sts)/14*15)) + """px;  
            background-color: #444444;
            border: 0px solid #444444;
            }
            """)
            
        self.sscat=str("""
            QLabel {
            font-size: """ + str(self.sts) + """px; 
            text-align: left;      
            border-radius: """+ str(int(8*self.faktor))+""";
            background-color: #1a1a1a;
            border: 0px solid #131313;
            padding-top: 2px;
            padding-left: 5px;
            padding-right: 5px;
            padding-bottom: 2px;
            color: yellow;
            }
            QWidget {
            font-size: """ + str(self.sts) + """px; 
            text-align: left;      
            border-radius: """+ str(int(8*self.faktor))+""";
            background-color: #1a1a1a;
            border: 0px solid #131313;
            padding-top: 2px;
            padding-left: 5px;
            padding-right: 5px;
            padding-bottom: 2px;
            color: yellow;
            }
            QComboBox {
            font-size: """ + str(int(self.sts/2*1.8)) + """px; 
            text-align: left;      
            border-radius: 0px;
            background-color: #282828;
            border: 2px solid #282828;
            padding-top: 2px;
            padding-left: 5px;
            padding-right: 5px;
            padding-bottom: 2px;
            color: white;
            }
            QPushButton {
            font-size: """ + str(self.sts) + """px; 
            text-align: left;      
            border-radius: """ + str(int(int(self.sts)/2)) + """px;
            background-color: #232323;
            border: 0px solid #030303;
            padding-top: 2px;
            padding-left: 5px;
            padding-right: 5px;
            padding-bottom: 2px;
            color: white;
            }
            QPushButton:hover {
            font-size: """ + str(int(int(self.sts)/14*15)) + """px;  
            background-color: #2b2b2b;
            border: 0px solid #2b2b2b;
            padding-top: 0px;
            padding-left: 5px;
            padding-right: 5px;
            padding-bottom: 0px;
            }
            QListWidget {
            font-size: """ + str(self.sts) + """px; 
            text-align: left;      
            border-radius: """ + str(int(int(self.sts)/2)) + """px;
            background-color: #232323;
            border: 1px solid #636363;
            padding-top: 2px;
            padding-left: 5px;
            padding-right: 5px;
            padding-bottom: 2px;
            color: white;
            }
            QLineEdit {
            font-size: """ + str(self.sts) + """px; 
            text-align: left;      
            border-radius: """ + str(int(int(self.sts)/2)) + """px;
            background-color: #232323;
            border: 1px solid #636363;
            padding-top: 2px;
            padding-left: 5px;
            padding-right: 5px;
            padding-bottom: 2px;
            color: white;
            }
            """)

        self.sslabel=str("""
            QLabel {
            font-size: """ + str(self.sts) + """px; 
            text-align: left;      
            padding-top: 2px;
            padding-left: 5px;
            padding-right: 5px;
            padding-bottom: 2px;
            color: white;
            }
            QPushButton {
            font-size: """ + str(self.sts) + """px; 
            text-align: left;      
            border-radius: """+ str(int(8*self.faktor))+""";
            background-color: #1a1a1a;
            border: 2px solid #1a1a1a;
            padding-top: 2px;
            padding-left: 5px;
            padding-right: 5px;
            padding-bottom: 2px;
            color: white;
            }
            QPushButton:hover {
            font-size: """ + str(self.sts) + """px; 
            text-align: left;      
            border-radius: """+ str(int(8*self.faktor))+""";
            background-color: #1a1a1a;
            border: 2px solid #1a1a1a;
            padding-top: 2px;
            padding-left: 5px;
            padding-right: 5px;
            padding-bottom: 2px;
            color: white;
            }
            """)
        
        self.sslabelU=str("""
            QPushButton {
            font-size: """ + str(int(self.sts*1.7)) + """px; 
            text-align: left;      
            border-radius: """+ str(int(8*self.faktor))+""";
            background-color: #1a1a1a;
            border: 2px solid #1a1a1a;
            padding-top: 2px;
            padding-left: 5px;
            padding-right: 5px;
            padding-bottom: 2px;
            color: #00ffca;
            }
            """)

        self.sslabelU1=str("""
            QLabel{
            font-size: """ + str(int(self.sts*1.4)) + """px; 
            text-align: left;      
            padding-top: 0px;
            padding-left: 5px;
            padding-right: 5px;
            padding-bottom: 0px;
            color: yellow;
            }
            """)

        self.sslabelP=str("""
            QLabel{
            font-size: """ + str(self.sts) + """px; 
            text-align: left;      
            padding-top: 0px;
            padding-left: 5px;
            padding-right: 5px;
            padding-bottom: 0px;
            color: white;
            }
            QPushButton{
            font-size: """ + str(self.sts) + """px; 
            text-align: left;      
            padding-top: 0px;
            padding-left: 5px;
            padding-right: 5px;
            padding-bottom: 0px;
            color: white;
            }
            QPushButton:hover {
            font-size: """ + str(self.sts*1.5) + """px;  
            text-align: left;      
            padding-top: 0px;
            padding-left: 5px;
            padding-right: 5px;
            padding-bottom: 0px;
            }
            """)
        
        self.sslabelP1=str("""
            QLabel{
            font-size: """ + str(self.sts) + """px; 
            text-align: right;      
            padding-top: 0px;
            padding-left: 5px;
            padding-right: 5px;
            padding-bottom: 0px;  
            color: white;
            }
            """)

        self.sslabelP2=str("""
            QLabel{
            font-size: """ + str(self.sts) + """px; 
            text-align: left;      
            padding-top: 0px;
            padding-left: 5px;
            padding-right: 5px;
            padding-bottom: 0px;  
            color: yellow;
            }
            """)


        # Layout gestaltung
        mainLayout = QHBoxLayout()
        categoryLayout = QVBoxLayout()
        mainLayout.addLayout(categoryLayout)
        contentLayout = QVBoxLayout()
        mainLayout.addLayout(contentLayout)

        # Titelbild einbinden
        self.title_pic = QLabel(self)
        pixmap = QPixmap('./images/settings_de.png')
        self.pb = int(int(440*self.faktor))
        self.ph = int(self.pb/5)
        self.title_pic.setPixmap(pixmap.scaled(self.pb, self.ph))
        self.title_pic.setStyleSheet("background: rgba(80,80, 80, 0);")
        self.title_pic.setFixedSize(self.pb, self.ph)
        self.title_pic.setAlignment(Qt.AlignLeft)
        
        # Kategorie Logo
        self.logo_label = QLabel()
        self.logo_label_lb = int(150*self.faktor)
        pixmap = QPixmap('./images/logo.png')
        self.logo_label.setPixmap(pixmap.scaled(self.logo_label_lb, self.logo_label_lb))
        self.logo_label.setFixedWidth(self.logo_label_lb)

        categoryLayout.addWidget(self.logo_label)
        categoryLayout.addStretch(1)
        contentLayout.addWidget(self.title_pic)
        contentLayout.addStretch(1)
        self.setLayout(mainLayout)


        # Erstellen der Kategorie-Buttons
        categories = ["Gestaltung", "Geräte", "System", "Sicherheit", "Informationen"]
        self.categoryButtons = []
        for category in categories:
            button = QPushButton(category)
            button.setFixedWidth(int(150*self.faktor))  # Kategorienbreite auf 150px festlegen
            button.setStyleSheet(self.ssbtn)  # stylesheet für kategoriebutton festlegen
            button.clicked.connect(lambda checked, cat=category: self.onCategoryClicked(cat))
            categoryLayout.addWidget(button)
            self.categoryButtons.append(button)

        label_leer = QLabel("")
        label_leer.setStyleSheet("background: rgba(80,80, 80, 0);")
        ueber = QPushButton("Über")
        ueber.setFixedWidth(int(50*self.faktor))  
        ueber.setStyleSheet(self.ssbtn_c)
        ueber.clicked.connect(lambda: os.system("python3 ./ueber.py"))
        old_settings = QPushButton("alle Einstellungen")
        old_settings.setFixedWidth(int(120*self.faktor))  
        old_settings.setStyleSheet(self.ssbtn_c)
        old_settings.clicked.connect(lambda: os.system("xfce4-settings-manager"))
        categoryLayout.addStretch(3)
        ueber_settings = QHBoxLayout()
        ueber_settings.addWidget(ueber)
        ueber_settings.addWidget(old_settings)
        categoryLayout.addLayout(ueber_settings)

        self.contents = {"Gestaltung": self.createContent1,
                         "Geräte": self.createContent2,
                         "System": self.createContent3,
                         "Sicherheit": self.createContent4,
                         "Informationen": self.createContent5}

        self.contentWidget = None
        self.scrollArea = None 
        
        self.setWindowIcon(QIcon('./images/logo.png'))  # Setze das systemweite Theme-Icon als Fenstericon
        self.setWindowTitle("X-Mint Einstellungen")
        x_pos=int((app.desktop().width()-breite)/2)
        y_pos=int((app.desktop().height()-hoehe)/2)
        self.setGeometry(x_pos, y_pos, breite, hoehe)
        self.setFixedSize(breite, hoehe)  # Festlegen der Größe 
        self.setFixedWidth(breite)
        self.setStyleSheet("background: rgba(80,80, 80, 00);") # Hintergrundfarbe festlegen

        # Entfernen der Fensterdekoration
        # self.setWindowFlags(Qt.FramelessWindowHint)
        # Setzen eines transparenten Hintergrunds
        # self.setAttribute(Qt.WA_TranslucentBackground)
        # self.setWindowOpacity(0.98) # komplettes fenster transparenz
        self.show()

        # Die erste Kategorie standardmäßig auswählen
        if self.categoryButtons:
            self.categoryButtons[0].click()

    def createContent1(self):
        self.categoryButtons[0].setStyleSheet(self.ssbtn1)
        pixmap = QPixmap('./images/design.png')
        if self.light_mode()==True:
            pixmap = QPixmap('./images-light/design.png')
        self.logo_label.setPixmap(pixmap.scaled(self.logo_label_lb, self.logo_label_lb))
        icon_size=int(24*self.faktor)

        # Akzentfarbe auswahl buttons
        label_themes = QPushButton("AkzentFarbe") 
        icon = QIcon("./icons/theme.png")
        label_themes.setIcon(icon)
        label_themes.setIconSize(QSize(icon_size,icon_size))
        label_themes.setStyleSheet(self.sslabel)
        
        self.fr_theme_list = self.check_flatremix_themes()
        layout_color_btns=QHBoxLayout()
        current_theme1=str(self.shell_cmd("xfconf-query -c xsettings -p /Net/ThemeName")[0]).replace("Flat-Remix-GTK-","")
        color_btns=[]
        if self.fr_theme_list != []:
            for theme in self.fr_theme_list:
                button=QPushButton()
                button.setToolTip(theme[2])
                button.setStyleSheet(str("""QPushButton {font-size: """ + str(self.sts) + """px; 
                                            border-radius: """+ str(int(8*self.faktor))+"""; 
                                            background-color: #"""+theme[1] +"""; 
                                            border: 2px solid #333333; 
                                            color: white; }
                                            QToolTip {font-size: """ + str(self.sts) + """px; 
                                            background-color: #222222; 
                                            border: 2px solid #333333; 
                                            color: white; }
                                            QPushButton:hover {font-size: """ + str(self.sts) + """px; 
                                            border-radius: """+ str(int(8*self.faktor))+"""; 
                                            background-color: #"""+theme[1] +"""; 
                                            border: 2px solid #ffffff; 
                                            color: white; }
                                            """))
                if current_theme1.startswith(theme[0]):
                    button.setStyleSheet(str("""QPushButton {font-size: """ + str(self.sts) + """px; 
                                                border-radius: """+ str(int(8*self.faktor))+"""; 
                                                background-color: #"""+theme[1] +"""; 
                                                border: 2px solid #ffffff; 
                                                color: white; }
                                                QToolTip {font-size: """ + str(self.sts) + """px; 
                                                background-color: #222222; 
                                                border: 2px solid #333333; 
                                                color: white; }
                                                QPushButton:hover {font-size: """ + str(self.sts) + """px; 
                                                border-radius: """+ str(int(8*self.faktor))+"""; 
                                                background-color: #"""+theme[1] +"""; 
                                                border: 2px solid #ffffff; 
                                                color: white; }
                                                """))
                button.setFixedWidth(int(23*self.faktor))
                button.setFixedHeight(int(16*self.faktor))
                button.clicked.connect(lambda checked, color=theme[0]: self.color_change(color))
                color_btns.append(button)
                layout_color_btns.addWidget(button)
                
        # Layout einbindung Themes
                    
        layout = QVBoxLayout()
        theme_layout = QHBoxLayout()
        theme_layout.addWidget(label_themes)
        theme_layout.addStretch()
        theme_layout.addLayout(layout_color_btns)
        layout.addLayout(theme_layout)


        self.fr_icons_list = self.check_flatremix_icons()

        current_icon=str(self.shell_cmd("xfconf-query -c xsettings -p /Net/IconThemeName")[0]).replace("Flat-Remix-","")
        layout_icons_btns=QHBoxLayout()
        icons_btns=[]
        if self.fr_icons_list != []:
            for theme in self.fr_icons_list:
                button=QPushButton()
                icon_path=str("/usr/share/icons/Flat-Remix-"+theme[0]+"-Dark/places/scalable/folder.svg")
                icon = QIcon(icon_path)
                button.setIcon(icon)
                button.setToolTip(theme[2])
                button.setIconSize(QSize(int(16*self.faktor),int(16*self.faktor)))
                button.setStyleSheet(str("""QPushButton {font-size: """ + str(self.sts) + """px; 
                                            border-radius: """+ str(int(6*self.faktor))+"""; 
                                            border: 2px ; 
                                            text-align: centre;      
                                            color: white; }
                                            QToolTip {font-size: """ + str(self.sts) + """px; 
                                            background-color: #222222; 
                                            border: 2px solid #333333; 
                                            color: white; }
                                            QPushButton:hover {font-size: """ + str(self.sts) + """px; 
                                            border-radius: """+ str(int(6*self.faktor))+"""; 
                                            border: 2px solid #"""+theme[1] +"""; 
                                            text-align: centre;  
                                            color: white; }
                                            """))
                if current_icon.startswith(theme[0]):
                    button.setStyleSheet(str("""QPushButton {font-size: """ + str(self.sts) + """px; 
                                                border-radius: """+ str(int(6*self.faktor))+"""; 
                                                border: 2px solid #ffffff; 
                                                text-align: centre;      
                                                color: white; }
                                                QToolTip {font-size: """ + str(self.sts) + """px; 
                                                background-color: #222222; 
                                                border: 2px solid #333333; 
                                                color: white; }
                                                QPushButton:hover {font-size: """ + str(self.sts) + """px; 
                                                border-radius: """+ str(int(6*self.faktor))+"""; 
                                                border: 2px solid #"""+theme[1] +"""; 
                                                text-align: centre;  
                                                color: white; }
                                                """))

                button.setFixedWidth(int(21*self.faktor))
                button.clicked.connect(lambda checked, color=theme[0]: self.icon_change(color))
                icons_btns.append(button)
                layout_icons_btns.addWidget(button)
                






        # symbole farbe einbinden
        label_leer = QLabel("")
        label_icons = QPushButton("SymbolFarbe")
        icon = QIcon("./icons/file.png")
        label_icons.setIcon(icon)
        label_icons.setIconSize(QSize(icon_size,icon_size))
        label_icons.setStyleSheet(self.sslabel)


        # Layout icons einbinden
        icon_layout = QHBoxLayout()
        icon_layout.addWidget(label_icons)
        icon_layout.addLayout(layout_icons_btns)
        layout.addLayout(icon_layout)



        # Dunkel oder Heller Modus einbinden
        #label_leer = QLabel("")
        label_dark = QPushButton("Dunkelmodus")
        icon = QIcon("./icons/darkmode.png")
        label_dark.setIcon(icon)
        label_dark.setIconSize(QSize(icon_size,icon_size))
        label_dark.setStyleSheet(self.sslabel)



        layout_dark_mode=QHBoxLayout()

        button=QPushButton()
        button.setToolTip("Hell")
        button.setStyleSheet(str("""QPushButton {font-size: """ + str(self.sts) + """px; 
                                    background-color: white; 
                                    border-radius: """+ str(int(6*self.faktor))+"""; 
                                    border: 2px ; 
                                    text-align: centre;      
                                    color: white; }
                                    QToolTip {font-size: """ + str(self.sts) + """px; 
                                    background-color: #222222; 
                                    border: 2px solid #333333; 
                                    color: white; }
                                    QPushButton:hover {font-size: """ + str(self.sts) + """px; 
                                    border-radius: """+ str(int(6*self.faktor))+"""; 
                                    border: 2px solid #"""+theme[1] +"""; 
                                    text-align: centre;  
                                    color: white; }
                                    """))
        button.setFixedWidth(int(90*self.faktor))
        button.clicked.connect(lambda checked, color=0: self.dark_mode(color))
        layout_dark_mode.addWidget(button)

        button=QPushButton()
        button.setToolTip("Mittel")
        button.setStyleSheet(str("""QPushButton {font-size: """ + str(self.sts) + """px; 
                                    background-color: grey; 
                                    border-radius: """+ str(int(6*self.faktor))+"""; 
                                    border: 2px ; 
                                    text-align: centre;      
                                    color: white; }
                                    QToolTip {font-size: """ + str(self.sts) + """px; 
                                    background-color: #222222; 
                                    border: 2px solid #333333; 
                                    color: white; }
                                    QPushButton:hover {font-size: """ + str(self.sts) + """px; 
                                    border-radius: """+ str(int(6*self.faktor))+"""; 
                                    border: 2px solid #"""+theme[1] +"""; 
                                    text-align: centre;  
                                    color: white; }
                                    """))
        button.setFixedWidth(int(90*self.faktor))
        button.clicked.connect(lambda checked, color=1: self.dark_mode(color))
        layout_dark_mode.addWidget(button)

        button=QPushButton()
        button.setToolTip("Dunkel")
        button.setStyleSheet(str("""QPushButton {font-size: """ + str(self.sts) + """px; 
                                    background-color: black; 
                                    border-radius: """+ str(int(6*self.faktor))+"""; 
                                    border: 2px ; 
                                    text-align: centre;      
                                    color: white; }
                                    QToolTip {font-size: """ + str(self.sts) + """px; 
                                    background-color: #222222; 
                                    border: 2px solid #333333; 
                                    color: white; }
                                    QPushButton:hover {font-size: """ + str(self.sts) + """px; 
                                    border-radius: """+ str(int(6*self.faktor))+"""; 
                                    border: 2px solid #"""+theme[1] +"""; 
                                    text-align: centre;  
                                    color: white; }
                                    """))
        button.setFixedWidth(int(90*self.faktor))
        button.clicked.connect(lambda checked, color=2: self.dark_mode(color))
        layout_dark_mode.addWidget(button)


        # Layout Fenstermanager Fensterdeko einbinden
        xfwm_layout = QHBoxLayout()
        xfwm_layout.addWidget(label_dark)
        xfwm_layout.addLayout(layout_dark_mode)
        layout.addLayout(xfwm_layout)



        # cursor auswahl menü
        label_leer = QLabel("")
        label_crsr = QPushButton("Mauszeiger")
        icon = QIcon("./icons/cursor.png")
        label_crsr.setIcon(icon)
        label_crsr.setIconSize(QSize(icon_size,icon_size))
        label_crsr.setStyleSheet(self.sslabel)

        # systemweiter ordner durchsuchen
        self.crsr_btn = QPushButton()
        current_crsr = str(self.shell_cmd("xfconf-query -c xsettings -p /Gtk/CursorThemeName")[0])
        current_crsrsize = str(self.shell_cmd("xfconf-query -c xsettings -p /Gtk/CursorThemeSize")[0])
        self.crsr_btn = QPushButton(current_crsr+" - "+current_crsrsize)
        self.crsr_btn.clicked.connect(lambda: self.open_cmd("xfce4-mouse-settings",0))

        # Layout Mauszeiger einbinden
        crsr_layout = QHBoxLayout()
        crsr_layout.addWidget(label_crsr)
        crsr_layout.addWidget(self.crsr_btn)
        layout.addLayout(crsr_layout)




        # Wallpaper
        workspace = self.shell_cmd("wmctrl -l | grep 'X-Mint Einstellung' | awk '{ print $2 }'")[0]
        
        wallpaper_path = "./icons/computer.png"
        if self.shell_cmd("xrandr --listmonitors | grep '*' | awk '{ print $4 }'"):
            monitor= self.shell_cmd("xrandr --listmonitors | grep '*' | awk '{ print $4 }'")[0]
        else:
            monitor= self.shell_cmd("xrandr --listmonitors | awk '{ print $4 }'")[0]
            if monitor == '':
                monitor = self.shell_cmd("xrandr --listmonitors | awk '{ print $4 }'")[1]

        wallpaper_path = self.shell_cmd("xfconf-query -c xfce4-desktop -p /backdrop/screen0/monitor"+monitor+"/workspace"+workspace+"/last-image")[0]


        label_leer = QLabel("")
        label_wp = QPushButton("Hintergrundbild")
        icon = QIcon("./icons/computer.png")
        label_wp.setIcon(icon)
        label_wp.setIconSize(QSize(icon_size,icon_size))
        label_wp.setStyleSheet(self.sslabel)
        self.wp_pixmap = QPushButton()
        #self.wp_pixmap.setStyleSheet(self.sslabel)
        self.wp_pixmap.setStyleSheet("text-align: centre; background: rgba(35,37, 46, 0);")
        icon = QIcon(wallpaper_path)
        self.wp_label_lb = int(220*self.faktor)
        self.wp_label_lh = int(self.wp_label_lb / 1.77)
        self.wp_pixmap.setIcon(icon)
        self.wp_pixmap.setIconSize(QSize(self.wp_label_lb, self.wp_label_lh))
        self.wp_pixmap.setFixedSize(self.wp_label_lb, self.wp_label_lh)
        self.wp_pixmap.clicked.connect(self.wallpaper_change)

        # Layout wallpaper einbinden
        wp_layout = QHBoxLayout()
        wp_layout.addWidget(label_wp, alignment=Qt.AlignTop)
        wp_layout.addStretch(2)
        wp_layout.addWidget(self.wp_pixmap, alignment=Qt.AlignRight)
        layout.addLayout(wp_layout)



        # Layout
        
        label_lo = QPushButton("Desktop-Layout")
        icon = QIcon("./icons/layout.png")
        label_lo.setIcon(icon)
        label_lo.setIconSize(QSize(icon_size,icon_size))
        label_lo.setStyleSheet(self.sslabel)

        self.lo_pixmap = QPushButton()
        icon = QIcon("./layouts/images/X-Mint.png")
        self.lo_label_lb = int(290*self.faktor)
        self.lo_label_lh = int(self.lo_label_lb / 1.77)
        self.lo_pixmap.setIcon(icon)
        self.lo_pixmap.setIconSize(QSize(self.lo_label_lb, self.lo_label_lh))
        self.lo_pixmap.setFixedSize(self.lo_label_lb, self.lo_label_lh)

        self.lo1_btn = QPushButton("X-Mint")
        self.lo1_btn.setStyleSheet(self.sscat_btn_xs_sel)
        self.lo1_btn.clicked.connect(lambda: self.layout_select("X-Mint", self.lo1_btn))
        self.lo1_btn.setFixedWidth(int(100*self.faktor))
        self.lo2_btn = QPushButton("Duo")
        self.lo2_btn.setStyleSheet(self.sscat_btn_xs)
        self.lo2_btn.clicked.connect(lambda: self.layout_select("X-Mint-Duo", self.lo2_btn))
        self.lo2_btn.setFixedWidth(int(100*self.faktor))
        self.lo3_btn = QPushButton("Comunity")
        self.lo3_btn.setStyleSheet(self.sscat_btn_xs)
        self.lo3_btn.clicked.connect(lambda: self.layout_select("X-Mint-Comunity", self.lo3_btn))
        self.lo3_btn.setFixedWidth(int(100*self.faktor))
        self.lo4_btn = QPushButton("OldSchool")
        self.lo4_btn.setStyleSheet(self.sscat_btn_xs)
        self.lo4_btn.clicked.connect(lambda: self.layout_select("X-Mint-Oldschool", self.lo4_btn))
        self.lo4_btn.setFixedWidth(int(100*self.faktor))
        self.loc_btn = QPushButton("Anwenden")
        self.loc_btn.setStyleSheet(self.sscat_btn_xs)
        self.loc_btn.setFixedWidth(int(100*self.faktor))
        self.desktop_layout= "X-Mint"
        self.loc_btn.clicked.connect(self.layout_change)

        # Layout icons einbinden

        lo2_layout = QVBoxLayout()
        #lo2_layout.addWidget(label_lo)
        lo2_layout.addStretch()
        lo2_layout.addWidget(self.lo1_btn)
        lo2_layout.addWidget(self.lo2_btn)
        lo2_layout.addWidget(self.lo3_btn)
        lo2_layout.addWidget(self.lo4_btn)
        lo2_layout.addStretch()
        lo2_layout.addWidget(self.loc_btn)
        
        lo1_layout = QHBoxLayout()
        lo1_layout.addStretch(1)
        lo1_layout.addLayout(lo2_layout)
        lo1_layout.addStretch(2)
        lo1_layout.addWidget(self.lo_pixmap)
        lo1_layout.addStretch(0)

        layout.addWidget(label_lo)
        layout.addLayout(lo1_layout)

        # weitere Einstellungen
        layout.addStretch()  
        btn_breite = int(115 * self.faktor)
        label_weitere = QLabel("\nWeitere Einstellungsmöglichkeiten")
        label_weitere.setStyleSheet(self.sscat)
        layout.addWidget(label_weitere)

        btn_weitere01 = QPushButton("Arbeitsflächen")
        btn_weitere01.setStyleSheet(self.sscat_btn_xs)
        btn_weitere01.setFixedWidth(btn_breite)
        btn_weitere01.clicked.connect(lambda:os.system("xfwm4-workspace-settings"))

        btn_weitere02 = QPushButton("Benachrichtigung")
        btn_weitere02.setStyleSheet(self.sscat_btn_xs)
        btn_weitere02.setFixedWidth(btn_breite)
        btn_weitere02.clicked.connect(lambda:os.system("xfce4-notifyd-config"))

        btn_weitere03 = QPushButton("Leisten")
        btn_weitere03.setStyleSheet(self.sscat_btn_xs)
        btn_weitere03.setFixedWidth(btn_breite)
        btn_weitere03.clicked.connect(lambda:os.system("xfce4-panel --preferences"))

        layout_weitere01 = QHBoxLayout()
        layout_weitere01.addWidget(btn_weitere01)
        layout_weitere01.addWidget(btn_weitere02)
        layout_weitere01.addWidget(btn_weitere03)
        layout.addLayout(layout_weitere01)
        
        # Layout unterer bzw finish bereich 
        layout.addStretch()  
        widget = QWidget()
        widget.setLayout(layout)
        widget.setStyleSheet(self.sscat)
        #widget.setFixedHeight(int(350*self.faktor))

        return widget

    def createContent2(self):
        self.categoryButtons[1].setStyleSheet(self.ssbtn1)
        pixmap = QPixmap('./images/hardware.png')
        if self.light_mode()==True:
            pixmap = QPixmap('./images-light/hardware.png')
        self.logo_label.setPixmap(pixmap.scaled(self.logo_label_lb, self.logo_label_lb))

        drucker= self.shell_cmd("lpstat -p 2>/dev/null")
        self.drucker_layout = QVBoxLayout()
        if drucker != [""]:
            label = QLabel("Bekannte Drucker:")
            label.setStyleSheet(self.sscat)
            self.drucker_layout.addWidget(label)
            for x in drucker:
                p1= x.find(" ")+1
                p2 = x[p1:].find(" ")
                self.drucker_list = QLabel(str(x[p1:p1+p2]))
                self.drucker_list.setStyleSheet(self.sslabelP)
                self.drucker_layout.addWidget(self.drucker_list)
            label = QLabel("Standarddrucker:")
            label.setStyleSheet(self.sscat)
            self.drucker_layout.addWidget(label)
            standart_drucker = self.shell_cmd("lpstat -d | grep ':'")
            if standart_drucker != [""]:
                drucker = standart_drucker[0][standart_drucker[0].find(":")+2:]
                label = QLabel(drucker)
                label.setStyleSheet(self.sscat)
                self.drucker_layout.addWidget(label)
            else:
                label = QLabel("Es wurde kein Standarddrucker ausgewäht")
                label.setStyleSheet(self.sscat)
                self.drucker_layout.addWidget(label)


        else:
            self.drucker_list = QLabel("kein drucker vorhanden")
            self.drucker_list.setStyleSheet(self.sscat)
            self.drucker_layout.addWidget(self.drucker_list)
        
        label_Drucker = QPushButton("\tDrucker und Scanner")
        label_Drucker.setStyleSheet(self.sslabel)
        icon = QIcon('./icons/printer.png')

        label_Drucker.setIcon(icon)
        label_Drucker.setIconSize(QSize(int(32*self.faktor),int(32*self.faktor)))

        btn_drucker = QPushButton("\tDrucker einrichten oder hinzufügen")
        btn_drucker.setStyleSheet(self.sscat_btn)
        btn_drucker.clicked.connect(self.printer_settings)

        layout_drucker = QHBoxLayout()
        layout_drucker.addWidget(label_Drucker)
        layout_drucker.addStretch()
        layout_drucker.addWidget(btn_drucker)

        layout = QVBoxLayout()
        layout.addLayout(layout_drucker)
        layout.addLayout(self.drucker_layout)
        label_leer = QLabel()
        layout.addWidget(label_leer)

        # Bluetooth
        label_bt = QPushButton("\tBluetooth")
        label_bt.setStyleSheet(self.sslabel)
        icon = QIcon('./icons/bluetooth.png')
        label_bt.setIcon(icon)
        label_bt.setIconSize(QSize(int(32*self.faktor),int(32*self.faktor)))
        layout_bt = QHBoxLayout()
        layout_bt.addWidget(label_bt)
        layout_bt.addStretch()
        layout.addLayout(layout_bt)

        self.bt_layout = QVBoxLayout()
        btn_bt= None
        if self.shell_cmd("hciconfig") != []:
            bt_devices=self.shell_cmd("bluetoothctl devices")
            if bt_devices != []:
                label = QLabel("Bekannte Geräte:")
                label.setStyleSheet(self.sscat)
                self.bt_layout.addWidget(label)
                for x in bt_devices:
                    y = x.split(" ")
                    name = " ".join(y[2:])
                    mac = y[1]
                    verbunden = str(self.shell_cmd("bluetoothctl info "+mac+" | grep Connected")).replace("'","").replace("]","").split(": ")[1].replace("yes", "ja").replace("no", "nein")
                    icon = str(self.shell_cmd("bluetoothctl info "+mac+" | grep Icon")[0]).split(": ")[1].replace(" ","")
                    #label = QPushButton("\t\t"+str(name)+" \n\t\tmac: "+mac+"\n\t\tverbunden: "+verbunden)
                    label = QPushButton("\t\t"+str(name)+"\n\t\tverbunden: "+verbunden)
                    bt_icon = QIcon('./bt-icons/'+icon+'.png')
                    label.setIcon(bt_icon)
                    label.setIconSize(QSize(int(24*self.faktor),int(24*self.faktor)))
                    label.setStyleSheet(self.sslabel)
                    self.bt_layout.addWidget(label)
            else:
                label = QLabel("Kein bekannte Geräte vorhanden")
                label.setStyleSheet(self.sslabelP)
                self.bt_layout.addWidget(label)
            
            btn_bt = QPushButton("\tBluetooth-Geräte suchen und verwalten ")
            btn_bt.setStyleSheet(self.sscat_btn)
            btn_bt.clicked.connect(self.bt_settings)

        else:
            label = QLabel("Ihr System besitzt kein Bluetoothadapter")
            label.setStyleSheet(self.sslabelP)
            self.bt_layout.addWidget(label)

        layout.addLayout(self.bt_layout)
        if btn_bt != None:
            layout_bt.addWidget(btn_bt)
        label_leer = QLabel()
        layout.addWidget(label_leer)

        # Maus
        label_mouse = QPushButton("\tMaus und Touchpad")
        label_mouse.setStyleSheet(self.sslabel)
        icon = QIcon('./icons/maus.png')
        label_mouse.setIcon(icon)
        label_mouse.setIconSize(QSize(int(32*self.faktor),int(32*self.faktor)))
        layout_maus = QHBoxLayout()
        layout.addLayout(layout_maus)
        layout_maus.addWidget(label_mouse)
        layout_maus.addStretch()
        label = QLabel("Erkannte Geräte:")
        label.setStyleSheet(self.sscat)
        layout.addWidget(label)

        mausliste_all = self.shell_cmd("xinput list | grep -v -i virtual | grep -i mouse | grep -v keyboard | grep -v Control")
        mausliste = []
        for maus in mausliste_all:
            element=maus[6:].split("id=")[0]
            if element not in mausliste:
                mausliste.append(element)
        maus = '\n'.join(mausliste)
        label_maus = QLabel(maus)
        label_maus.setStyleSheet(self.sslabel)
        layout.addWidget(label_maus)
        btn_maus = QPushButton("\tMauseinstellungen verwalten ")
        btn_maus.setStyleSheet(self.sscat_btn)
        btn_maus.clicked.connect(lambda: self.shell_cmd("xfce4-mouse-settings"))
        layout_maus.addWidget(btn_maus)
        label_leer = QLabel()
        layout.addWidget(label_leer)


        # keyboard
        label_kb = QPushButton("\tTastatur")
        label_kb.setStyleSheet(self.sslabel)
        icon = QIcon('./bt-icons/input-keyboard.png')
        label_kb.setIcon(icon)
        label_kb.setIconSize(QSize(int(32*self.faktor),int(32*self.faktor)))
        layout_kb = QHBoxLayout()
        layout_kb.addWidget(label_kb)
        layout_kb.addStretch()
        layout.addLayout(layout_kb)
        label = QLabel("Erkannte Geräte:")
        label.setStyleSheet(self.sscat)
        layout.addWidget(label)

        kbliste_all = self.shell_cmd("xinput list | grep -v -i button | grep -v -i virtual | grep -v -i mouse | grep -i keyboard | grep -v Control")[1:]
        kbliste = []
        for kb in kbliste_all:
            element = kb[6:].split("id=")[0]
            if element not in kbliste:
                kbliste.append(element)
        maus = '\n'.join(kbliste)
        label_kbs = QLabel(maus)
        label_kbs.setStyleSheet(self.sslabel)
        layout.addWidget(label_kbs)

        btn_kb = QPushButton("\tTastatureinstellungen und Tastenkürzel verwalten ")
        btn_kb.setStyleSheet(self.sscat_btn)
        btn_kb.clicked.connect(lambda: self.shell_cmd("xfce4-keyboard-settings"))
        layout_kb.addWidget(btn_kb)
        label_leer = QLabel()
        layout.addWidget(label_leer)

        #Grafikkarte
        command = self.shell_cmd("hwinfo --gfxcard --short 2>/dev/null | tail -n +2 | head -n -1")
        if command == []:
            gfxcard = ["Unbekannt"]
        else:
            gfxcard = command[0].lstrip().replace("[", "- ").replace("]", "")
        
        self.nvidia = False
        if gfxcard.startswith("nVidia"):
            self.nvidia = True
        label_gpu = QPushButton("\tGrafikkarte")
        label_gpu.setStyleSheet(self.sslabel)
        icon = QIcon('./images/grafik.png')
        label_gpu.setIcon(icon)
        label_gpu.setIconSize(QSize(int(32*self.faktor),int(32*self.faktor)))
        layout_gpu = QHBoxLayout()
        layout_gpu.addWidget(label_gpu)
        layout_gpu.addStretch() 
        layout.addLayout(layout_gpu)
        label = QLabel("Erkannte Geräte:")
        label.setStyleSheet(self.sscat)
        layout.addWidget(label)

       
        label_gpuname = QLabel(gfxcard)
        label_gpuname.setStyleSheet(self.sslabel)
        layout.addWidget(label_gpuname)

        btn_gpu = QPushButton("\tNach Treiber suchen")
        btn_gpu.setStyleSheet(self.sscat_btn)
        btn_gpu.clicked.connect(lambda: self.shell_cmd("driver-manager"))
        layout_gpu.addWidget(btn_gpu)
        label_leer = QLabel()
        layout.addWidget(label_leer)



        #Monitore

        # Erhalte die Liste der angeschlossenen Monitore
        xrandr_output = subprocess.check_output(["xrandr"]).decode("utf-8")
        monitors_info = re.findall(r"(\S+) connected.*?(\d+x\d+)", xrandr_output)
        monitore = ""
        for monitor, resolution in monitors_info:
            monitore=monitore+(f"{monitor}  {resolution}\n")

        label_mon = QPushButton("\tAnzeige")
        label_mon.setStyleSheet(self.sslabel)
        icon = QIcon('./icons/computer.png')
        label_mon.setIcon(icon)
        label_mon.setIconSize(QSize(int(32*self.faktor),int(32*self.faktor)))
        layout_mon = QHBoxLayout()
        layout_mon.addWidget(label_mon)
        layout_mon.addStretch() 
        layout.addLayout(layout_mon)
        label = QLabel("Erkannte Geräte:")
        label.setStyleSheet(self.sscat)
        layout.addWidget(label)

       
        label_monname = QLabel(monitore)
        label_monname.setStyleSheet(self.sslabel)
        layout.addWidget(label_monname)

        btn_mon = QPushButton("\tAnzeige einstellen")
        btn_mon.setStyleSheet(self.sscat_btn)
        btn_mon.clicked.connect(lambda: self.shell_cmd("xfce4-display-settings"))
        btn_nvidia = QPushButton("\tNvidia-einstellungen")
        btn_nvidia.setStyleSheet(self.sscat_btn)
        btn_nvidia.clicked.connect(lambda: self.shell_cmd("nvidia-settings"))
        layout_mon.addWidget(btn_mon)
        if self.nvidia == True:
            layout_mon.addWidget(btn_nvidia)
        label_leer = QLabel()
        layout.addWidget(label_leer)



        # Endbereich
        layout.addStretch()  # Elastischer Bereich am Ende des Inhalts
        widget = QWidget()
        widget.setLayout(layout)
        widget.setStyleSheet(self.sscat)

        return widget

    def createContent3(self):
        self.categoryButtons[2].setStyleSheet(self.ssbtn1)
        pixmap = QPixmap('./images/system.png')
        if self.light_mode()==True:
            pixmap = QPixmap('./images-light/system.png')
        self.logo_label.setPixmap(pixmap.scaled(self.logo_label_lb, self.logo_label_lb))

        # Autostart Programme
        asapps = self.shell_cmd("ls -i ~/.config/autostart/ 2>/dev/null | wc -l")[0]
        asgapps = self.shell_cmd("ls -i /etc/xdg/autostart/ 2>/dev/null | wc -l")[0]
        label_autostart = QPushButton(" Autostart Programme")
        icon = QIcon("./icons/autostart.png")
        label_autostart.setIcon(icon)
        label_autostart.setIconSize(QSize(int(33*self.faktor),int(33*self.faktor)))
        label_autostart.setStyleSheet(self.sslabel)

        label_autostart_status = QLabel("Es befinden sich "+str(asapps)+" Programme im Autostart\nund "+str(asgapps)+" Programme im systemweiten Autostart.")
        btn_autostart = QPushButton(" Startverhalten anpassen ")
        btn_autostart.setStyleSheet(self.sscat_btn)
        btn_autostart.clicked.connect(lambda:os.system("xfce4-session-settings"))


        autostart_layout = QHBoxLayout()
        autostart_layout.addWidget(label_autostart)
        autostart_layout.addStretch()
        autostart_layout.addWidget(btn_autostart)


        # benutzer 
        users = self.shell_cmd("cat /etc/passwd 2>/dev/null| grep -E '/bin/bash|/bin/zsh' | cut -d: -f1 | grep -v root")
        label_users = QPushButton(" Vorhandene Benutzer")
        icon = QIcon("./icons/benutzer.png")
        label_users.setIcon(icon)
        label_users.setIconSize(QSize(int(33*self.faktor),int(33*self.faktor)))
        label_users.setStyleSheet(self.sslabel)

        label_users_status = QLabel("Es befinden sich "+str(len(users))+" erstellte Benutzerkonten auf dem System.")
        if len(asapps) == 1:
            label_users_status = QLabel("Es befindet sich 1 erstelltes Benutzerkonto auf dem System.")
        btn_users = QPushButton(" Benutzerkonten verwalten ")
        btn_users.setStyleSheet(self.sscat_btn)
        btn_users.clicked.connect(lambda:os.system("users-admin"))


        users_layout = QHBoxLayout()
        users_layout.addWidget(label_users)
        users_layout.addStretch()
        users_layout.addWidget(btn_users)


        # Datum und zeit 
        # Aktuelles Datum und Uhrzeit abrufen
        heute = time.strftime('%Y-%m-%d', time.localtime())
        zeit = time.strftime('%H:%M:%S', time.localtime())

        # Zeitzone abrufen
        timezone = time.strftime('%Z', time.gmtime())
        
        
        label_time = QPushButton(" Datum und zeit ")
        icon = QIcon("./icons/kalender.png")
        label_time.setIcon(icon)
        label_time.setIconSize(QSize(int(32*self.faktor),int(32*self.faktor)))
        label_time.setStyleSheet(self.sslabel)

        label_time_status = QLabel("Datum: " + heute + "    Uhrzeit: " + zeit + "    Zeitzone: " + timezone)
        btn_time = QPushButton(" Datum und Zeit korigieren ")
        btn_time.setStyleSheet(self.sscat_btn)
        btn_time.clicked.connect(lambda:os.system("time-admin"))


        time_layout = QHBoxLayout()
        time_layout.addWidget(label_time)
        time_layout.addStretch()
        time_layout.addWidget(btn_time)


        # speicher bereinigen
        # bleachbit --preview --all-but-warning 2>/dev/null | grep Gewonnen
        gewinntest = self.shell_cmd("bleachbit --preview --all-but-warning 2>/dev/null | grep Gewonnen")
        if gewinntest == ['']:
            gewinnbar = "nicht ermittelbar."
        else:
            gewinnbar = str(gewinntest[0].split(":")[1])

        clean_mem = QPushButton(" Speicher bereinigen ")
        icon = QIcon("./icons/cleaner.png")
        clean_mem.setIcon(icon)
        clean_mem.setIconSize(QSize(int(32*self.faktor),int(32*self.faktor)))
        clean_mem.setStyleSheet(self.sslabel)

        self.label_clean_status = QLabel("Gewinnbarer Speicherplatz: " + gewinnbar)
        btn_clean = QPushButton(" Speicher bereinigen ")
        btn_clean.setStyleSheet(self.sscat_btn)
        btn_clean.clicked.connect(self.memory_clean_cleaner)
        btn_clean_check = QPushButton(" prüfen ")
        btn_clean_check.setStyleSheet(self.sscat_btn)
        btn_clean_check.clicked.connect(self.memory_clean_checker)


        clean_layout = QHBoxLayout()
        clean_layout.addWidget(clean_mem)
        clean_layout.addStretch()
        clean_layout.addWidget(btn_clean_check)
        clean_layout.addWidget(btn_clean)







        # Festplatten Verwaltung
        #df -h | grep -v 'tmpfs' | grep -v 'efivarfs' | grep -v '/boot/efi'

        label_leer = QLabel()
        layout = QVBoxLayout()
        layout.addLayout(autostart_layout)
        layout.addWidget(label_autostart_status)
        layout.addWidget(label_leer)
        layout.addLayout(users_layout)
        layout.addWidget(label_users_status)
        layout.addWidget(label_leer)
        layout.addLayout(time_layout)
        layout.addWidget(label_time_status)
        layout.addWidget(label_leer)
        layout.addLayout(clean_layout)
        layout.addWidget(self.label_clean_status)
        layout.addWidget(label_leer)
        layout.addStretch()  # Elastischer Bereich am Ende des Inhalts

        widget = QWidget()
        widget.setLayout(layout)
        widget.setStyleSheet(self.sscat)
        #widget.setFixedHeight(int(350*self.faktor))

        return widget
        
    def createContent4(self):
        self.categoryButtons[3].setStyleSheet(self.ssbtn1)
        pixmap = QPixmap('./images/security.png')
        if self.light_mode()==True:
            pixmap = QPixmap('./images-light/security.png')
        self.logo_label.setPixmap(pixmap.scaled(self.logo_label_lb, self.logo_label_lb))
        #self.installed_apps=str(self.shell_cmd("apt list --installed 2>/dev/null"))

        # Aktuallisierungen
        layout = QVBoxLayout()
        label_update = QPushButton("Aktualisierung")
        icon = QIcon("./icons/update.png")
        label_update.setIcon(icon)
        label_update.setIconSize(QSize(int(33*self.faktor),int(33*self.faktor)))
        label_update.setStyleSheet(self.sslabel)
        self.btn_update = QPushButton("auf Aktuallisierungen prüfen")
        self.btn_update.setStyleSheet(self.sscat_btn_warn)
        self.btn_update.clicked.connect(self.updates_pruefen)
        count = 0
        self.label_updates_count = QLabel("noch nicht nach Aktualisierungen gesucht")
        updater_layout = QHBoxLayout()
        updater_layout.addWidget(self.label_updates_count)
        updater_layout.addStretch()

        if self.updates_checked == 1:
            count = 0
            if self.updates:
                count = len(self.updates)
            self.btn_update.setStyleSheet(self.sscat_btn)
            self.btn_update.setText("erneut auf Aktuallisierungen prüfen")
            self.label_updates_count.setText("Es sind " + str(count) + " Aktualisierungen verfügbar")

        if self.updates != None :
            count = len(self.updates)
            btn_updater=QPushButton("Aktuallisieren")
            btn_updater.setStyleSheet(self.sscat_btn_warn)
            btn_updater.clicked.connect(lambda:os.system("mintupdate"))
            updater_layout.addWidget(btn_updater)

        
   
        update_layout = QHBoxLayout()
        update_layout.addWidget(label_update)
        update_layout.addStretch()
        update_layout.addWidget(self.btn_update)

        layout.addLayout(update_layout)
        layout.addLayout(updater_layout)
        label_leer = QLabel("")
        layout.addWidget(label_leer)

        # Firewall
        gufw = self.installed_apps.find("gufw/")
        #gufw = self.shell_cmd("apt list --installed 2>/dev/null | grep gufw")
        label_firewall = QPushButton(" Firewall")
        icon = QIcon("./icons/shield.png")
        label_firewall.setIcon(icon)
        label_firewall.setIconSize(QSize(int(33*self.faktor),int(33*self.faktor)))
        label_firewall.setStyleSheet(self.sslabel)

        if gufw != -1:
            label_firewall_status = QLabel("GUFW ist auf ihrem System installiert")
            btn_firewall = QPushButton(" Firewall verwalten ")
            btn_firewall.setStyleSheet(self.sscat_btn)
            btn_firewall.clicked.connect(lambda:os.system("gufw"))

        else:
            label_firewall_status = QLabel("GUFW ist auf ihrem System nicht installiert !!!")
            btn_firewall = QPushButton(" Firewall installieren ")
            btn_firewall.setStyleSheet(self.sscat_btn_warn)
            btn_firewall.clicked.connect(lambda: self.install_app("gufw",3))

        firewall_layout = QHBoxLayout()
        firewall_layout.addWidget(label_firewall)
        firewall_layout.addStretch()
        firewall_layout.addWidget(btn_firewall)

        layout.addLayout(firewall_layout)
        layout.addWidget(label_firewall_status)

        label_leer = QLabel("")
        layout.addWidget(label_leer)

        # Timeshift 

        snapshot = self.installed_apps.find("timeshift/")
        #snapshot = self.shell_cmd("apt list --installed 2>/dev/null | grep timeshift")
        label_snapshot = QPushButton("Wiederherstellung")
        icon = QIcon("./icons/snapshot.png")
        label_snapshot.setIcon(icon)
        label_snapshot.setIconSize(QSize(int(33*self.faktor),int(33*self.faktor)))
        label_snapshot.setStyleSheet(self.sslabel)

        if snapshot != -1:
            label_snapshot_status = QLabel("Timeshift ist auf ihrem System installiert")
            btn_snapshot = QPushButton("  Wiederherstellung verwalten  ")
            btn_snapshot.setStyleSheet(self.sscat_btn)
            btn_snapshot.clicked.connect(lambda:os.system("timeshift-launcher"))


        else:
            label_snapshot_status = QLabel("Timeshift ist auf ihrem System nicht installiert !!!")
            btn_snapshot = QPushButton("  Timeshift installieren  ")
            btn_snapshot.setStyleSheet(self.sscat_btn_warn)
            btn_snapshot.clicked.connect(lambda: self.install_app("timeshift",3))

        snapshot_layout = QHBoxLayout()
        snapshot_layout.addWidget(label_snapshot)
        snapshot_layout.addStretch()
        snapshot_layout.addWidget(btn_snapshot)

        layout.addLayout(snapshot_layout)
        layout.addWidget(label_snapshot_status)

        label_leer = QLabel("")
        layout.addWidget(label_leer)


        # Backups mit deja-dup



        backup = self.installed_apps.find("deja-dup/")
        #backup = self.shell_cmd("apt list --installed 2>/dev/null | grep deja-dup")
        label_backup = QPushButton(" Daten-Backups")
        icon = QIcon("./icons/backup.png")
        label_backup.setIcon(icon)
        label_backup.setIconSize(QSize(int(33*self.faktor),int(33*self.faktor)))
        label_backup.setStyleSheet(self.sslabel)

        if backup != -1:
            label_backup_status = QLabel("Deja-Dup ist auf ihrem System installiert")
            btn_backup = QPushButton("  Backups verwalten  ")
            btn_backup.setStyleSheet(self.sscat_btn)
            btn_backup.clicked.connect(lambda:os.system("deja-dup"))


        else:
            label_backup_status = QLabel("Deja-Dup ist auf ihrem System nicht installiert !!!")
            btn_backup = QPushButton("  Backup-Tool installieren  ")
            btn_backup.setStyleSheet(self.sscat_btn_warn)
            btn_backup.clicked.connect(lambda: self.install_app("deja-dup",3))

        backup_layout = QHBoxLayout()
        backup_layout.addWidget(label_backup)
        backup_layout.addStretch()
        backup_layout.addWidget(btn_backup)

        layout.addLayout(backup_layout)
        layout.addWidget(label_backup_status)

        label_leer = QLabel("")
        layout.addWidget(label_leer)
        layout.addStretch()  # Elastischer Bereich am Ende des Inhalts

        widget = QWidget()
        widget.setLayout(layout)
        widget.setStyleSheet(self.sscat)
        #widget.setFixedHeight(int(350*self.faktor))

        return widget

    def createContent5(self):
        self.categoryButtons[4].setStyleSheet(self.ssbtn1)
        pixmap = QPixmap('./images/info.png')
        if self.light_mode()==True:
            pixmap = QPixmap('./images-light/info.png')
        self.logo_label.setPixmap(pixmap.scaled(self.logo_label_lb, self.logo_label_lb))



        # hostname 
        command = self.shell_cmd("hostname 2>/dev/null")
        if command == []:
            host_name = ["Unbekannt"]
        else:
            host_name = command[0].lstrip()
        label_hostname = QLabel("\n Hostname:")
        label_hostname.setStyleSheet(self.sslabelP1)

        label_hostname_status = QLabel(text="\n"+host_name)
        label_hostname_status.setFixedWidth(int(300*self.faktor))
        label_hostname_status.setStyleSheet(self.sslabelP2)


        hostname_layout = QHBoxLayout()
        hostname_layout.addStretch()
        hostname_layout.addWidget(label_hostname)
        hostname_layout.addWidget(label_hostname_status)

        # kernel
        command = self.shell_cmd("uname -r 2>/dev/null")
        if command == []:
            kernel_name = ["Unbekannt"]
        else:
            kernel_name = command[0].lstrip()
        label_kernel = QLabel("Linux-Kernel:")
        label_kernel.setStyleSheet(self.sslabelP1)

        label_kernel_status = QLabel(text=kernel_name)
        label_kernel_status.setFixedWidth(int(300*self.faktor))
        label_kernel_status.setStyleSheet(self.sslabelP2)


        kernel_layout = QHBoxLayout()
        kernel_layout.addStretch()
        kernel_layout.addWidget(label_kernel)
        kernel_layout.addWidget(label_kernel_status)


        # base
        command = self.shell_cmd("cat /etc/os-release | grep 'PRETTY_NAME' | cut -d= -f 2 ")
        if command == []:
            base_name = ["Unbekannt"]
        else:
            base_name = command[0].lstrip().replace('"',"")
        label_base = QLabel("Basis-OS:")
        label_base.setStyleSheet(self.sslabelP1)

        label_base_status = QLabel(text=base_name)
        label_base_status.setFixedWidth(int(300*self.faktor))
        label_base_status.setStyleSheet(self.sslabelP2)


        base_layout = QHBoxLayout()
        base_layout.addStretch()
        base_layout.addWidget(label_base)
        base_layout.addWidget(label_base_status)

        # Cpu
        command=self.shell_cmd_en("lscpu | grep 'Model name:'")
        
        if command == []:
            cpu_model = ["Unbekannt"]
        else:
            cpu_model = command[0].split(":")[1].lstrip().replace("@ ","\n")
        label_cpu = QLabel(" Prozessor:")
        label_cpu.setStyleSheet(self.sslabelP1)

        label_cpu_status = QLabel(text=cpu_model)
        label_cpu_status.setStyleSheet(self.sslabelP2)
        label_cpu_status.setFixedWidth(int(300*self.faktor))


        cpu_layout = QHBoxLayout()
        cpu_layout.addStretch()
        cpu_layout.addWidget(label_cpu, alignment=Qt.AlignTop)
        cpu_layout.addWidget(label_cpu_status)
        
        # Arbeitsspeicher
        ram = self.shell_cmd("free -h --si 2>/dev/null | tail -n +2| head -n -1")[0].split()
        ram_raw = self.shell_cmd("free --si 2>/dev/null | tail -n +2| head -n -1")[0].split()
        ram_pro = str(int(100/int(ram_raw[1])*int(ram_raw[2])))
        ram_text=ram_pro+"% verwendet ( " + ram[1] + "B / " + ram[2] + "B )"
        label_ram = QLabel(" Arbeitsspeicher:")
        label_ram.setStyleSheet(self.sslabelP1)

        label_ram_status = QLabel(text=ram_text)
        label_ram_status.setStyleSheet(self.sslabelP2)
        label_ram_status.setFixedWidth(int(300*self.faktor))


        ram_layout = QHBoxLayout()
        ram_layout.addStretch()
        ram_layout.addWidget(label_ram, alignment=Qt.AlignTop)
        ram_layout.addWidget(label_ram_status)



        # Grafikkarte 
        command = self.shell_cmd("hwinfo --gfxcard --short 2>/dev/null | tail -n +2 | head -n -1")
        if command[0] == "":
            gfxcard = ["Unbekannt"]
        else:
            gfxcard = command[0].lstrip().replace("[", "\n").replace("]", "")
        label_gfx = QLabel(" Grafikkarte:")
        label_gfx.setStyleSheet(self.sslabelP1)

        label_gfx_status = QLabel(text=gfxcard)
        label_gfx_status.setFixedWidth(int(300*self.faktor))
        label_gfx_status.setStyleSheet(self.sslabelP2)


        gfx_layout = QHBoxLayout()
        gfx_layout.addStretch()
        gfx_layout.addWidget(label_gfx, alignment=Qt.AlignTop)
        gfx_layout.addWidget(label_gfx_status)




        
        # Festplatten

        cmd="lsblk -n -d  -o NAME,SIZE,TRAN,TYPE,MODEL | grep -v 'loop' | grep -v 'usb' | grep 'disk'"
        #cmd = "lsblk | grep 'disk'"
        disks=self.shell_cmd(cmd)
        if disks == ['']:
            disks = ['1 0 3 4 Festplatten nicht erkannt']
        disk_text = ""
        for x in disks:
            disk = x.split()
            model = ' '.join(map(str, disk[4:]))
            disk_text = disk_text + disk[1] + "B   \t" + model + "\n"
        disk_text = disk_text[:-1]
        label_disks = QLabel(" Festplatten:")
        label_disks.setStyleSheet(self.sslabelP1)

        label_disks_status = QLabel(text=disk_text)
        label_disks_status.setStyleSheet(self.sslabelP2)
        label_disks_status.setFixedWidth(int(300*self.faktor))


        disks_layout = QHBoxLayout()
        disks_layout.addStretch()
        disks_layout.addWidget(label_disks, alignment=Qt.AlignTop)
        disks_layout.addWidget(label_disks_status)
 





        # Systeminfo overlay zusammenstellen
        layout = QVBoxLayout()
        layout.addLayout(hostname_layout)
        layout.addLayout(kernel_layout)
        layout.addLayout(base_layout)
        layout.addLayout(cpu_layout)
        layout.addLayout(ram_layout)
        layout.addLayout(gfx_layout)
        layout.addLayout(disks_layout)
        layout.addStretch()  # Elastischer Bereich am Ende des Inhalts
        layout.setSpacing(17)

        widget = QWidget()
        widget.setLayout(layout)
        widget.setStyleSheet(self.sscat)
        #widget.setFixedHeight(int(350*self.faktor))

        return widget
        
    def onCategoryClicked(self, category):
        self.akzent_color()
        for x in self.categoryButtons:
            x.setStyleSheet(self.ssbtn)

        contentCreator = self.contents.get(category)
        if contentCreator:
            contentWidget = contentCreator()
            if self.contentWidget:
                self.contentWidget.setParent(None)
                self.contentWidget.deleteLater()
            
            contentLayout = self.layout().itemAt(1).layout()

            if self.scrollArea is None:
                # Erstelle eine QScrollArea, wenn noch keine vorhanden ist
                self.scrollArea = QScrollArea()
                self.scrollArea.setWidgetResizable(True)
                # Setze die vertikale Scrollbar-Policy, um sie immer anzuzeigen
                self.scrollArea.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
                # Setze eine feste Höhe (z.B., 410 Pixel)
                self.scrollArea.setFixedHeight(int(455 * self.faktor))
                contentLayout.addWidget(self.scrollArea, alignment=Qt.AlignTop)
                contentLayout.addStretch(2)
            
            # Setze das contentWidget in die QScrollArea
            self.scrollArea.setWidget(contentWidget)
            
            self.contentWidget = contentWidget
            self.contentWidget.setStyleSheet(self.sscat)

    def shell_cmd(self, command):
        try:
            # Führe den übergebenen Befehl aus und erfasse die Ausgabe
            result = subprocess.check_output(command, shell=True,env=None, universal_newlines=True)
            
            # Teile die Ausgabe in Zeilen auf
            output_lines = result.splitlines()
            return output_lines
        except subprocess.CalledProcessError as e:
            return [""]

    def shell_cmd_en(self, command):
        env = {"LANG": "en_US.UTF-8", "LC_ALL": "en_US.UTF-8"}
        try:
            # Führe den übergebenen Befehl aus und erfasse die Ausgabe
            result = subprocess.check_output(command, shell=True,env=env, universal_newlines=True)
            
            # Teile die Ausgabe in Zeilen auf
            output_lines = result.splitlines()
            return output_lines
        except subprocess.CalledProcessError as e:
            return [""]
        
    def shell_cmd_ns(self, command):
        try:
            # Führe den übergebenen Befehl aus und erfasse die Ausgabe
            result = subprocess.check_output(command, shell=True)

            return result
        except subprocess.CalledProcessError as e:
            return ""

    def theme_select(self):
        # Diese Funktion wird aufgerufen, wenn eine Option ausgewählt wird
        selected_option = str(self.theme_list.currentText())
        self.shell_cmd("xfconf-query -c xsettings -p /Net/ThemeName -s " + selected_option)
        current_theme = str(self.shell_cmd("xfconf-query -c xsettings -p /Net/ThemeName")[0])

    def layout_change(self):
        self.shell_cmd("bash xfce4-panel-profiles load ./layouts/" + self.desktop_layout + ".tar.bz2")

    def layout_select(self,layout,btn):
        self.desktop_layout = layout
        icon = QIcon("./layouts/images/" + layout + ".png")
        self.lo1_btn.setStyleSheet(self.sscat_btn_xs)
        self.lo2_btn.setStyleSheet(self.sscat_btn_xs)
        self.lo3_btn.setStyleSheet(self.sscat_btn_xs)
        self.lo4_btn.setStyleSheet(self.sscat_btn_xs)
        btn.setStyleSheet(self.sscat_btn_xs_sel)
        self.lo_pixmap.setIcon(icon)
        #self.shell_cmd("bash xfce4-panel-profiles load ./layouts/" + layout+".tar.bz2")

    def icon_select(self):
        # Diese Funktion wird aufgerufen, wenn eine Option ausgewählt wird
        selected_option = str(self.icons_list.currentText())
        self.shell_cmd("xfconf-query -c xsettings -p /Net/IconThemeName -s " + selected_option)

    def crsr_select(self):
        self.shell_cmd("xfce4-mouse-settings")
        if self.categoryButtons:
            self.categoryButtons[0].click() 

    def open_cmd(self,cmd,cat):
        self.shell_cmd(cmd)
        if self.categoryButtons:
            self.categoryButtons[cat].click() 

    def dark_mode(self,color):
        # Diese Funktion wird aufgerufen, wenn eine Option ausgewählt wird
        modes=[
            '-Light',
            '-Dark',
            '-Darkest'
        ]
        theme="Flat-Remix"+modes[color]+"-XFWM"
        self.shell_cmd("xfconf-query -c xfwm4 -p /general/theme -s " + theme)

        current_theme = str(self.shell_cmd("xfconf-query -c xsettings -p /Net/ThemeName")[0]).replace("-Darkest","").replace("-Dark","").replace("-Light","")
        if not current_theme.startswith("Flat-Remix-GTK"):
            theme_color=self.check_flatremix_themes()[0][0]
            current_theme="Flat-Remix-GTK-"+theme_color
        theme=current_theme+modes[color]
        self.shell_cmd("xfconf-query -c xsettings -p /Net/ThemeName -s " + theme)
        current_theme = str(self.shell_cmd("xfconf-query -c xsettings -p /Net/ThemeName")[0])
        if self.categoryButtons:
            self.categoryButtons[0].click() 

    def light_mode(self):
        current_theme = str(self.shell_cmd("xfconf-query -c xsettings -p /Net/ThemeName")[0])
        mode = False
        if current_theme.endswith("-Light"):
            mode = True
        return mode
    
    def wallpaper_change(self):
        self.shell_cmd("xfdesktop-settings")
        if self.categoryButtons:
            self.categoryButtons[0].click() 
                
    def printer_settings(self):
        self.shell_cmd("system-config-printer")
        if self.categoryButtons:
            self.categoryButtons[1].click()
         
    def bt_settings(self):
        self.shell_cmd("blueman-manager")
        if self.categoryButtons:
            self.categoryButtons[1].click()

    def updates_pruefen(self):
        self.btn_update.setStyleSheet(self.sscat_btn)

        self.start_warten()
        # Diese Funktion wird aufgerufen, wenn eine Option ausgewählt wird
        x = self.shell_cmd("pkexec sudo /usr/bin/apt update 2>/dev/null")

        self.updates = self.shell_cmd(" apt list --upgradable 2>/dev/null | grep 'aktu'")
        self.updates_checked = 1
        count = 0
        updates_list = ""
        if self.updates != None :
            count = len(self.updates)
            for x in self.updates:
                updates_list = updates_list + x[0:x.find("/")] + "\n"

        self.kill_warten()
        self.label_updates_count.setText("Es sind " + str(count) + " Aktualisierungen verfügbar")


        msg = QMessageBox()
        msg.setStyleSheet(self.sscat)
        pixmap = QPixmap('./icons/update.png')
        pf = int(self.faktor * 36)
        icon = QIcon('./icons/update.png')
        msg.setWindowIcon(icon)
        msg.setIconPixmap(pixmap.scaled(pf, pf))
        msg.setText("Es sind " + str(count) + " Aktualisierungen verfügbar."+"\n"+updates_list)
        msg.setWindowTitle("Update")
        # msg.setStandardButtons(QMessageBox.Ok)
        msg.exec()
        if self.categoryButtons:
            self.categoryButtons[3].click()

    def install_app(self, app, cat):
        self.start_warten()
        # Diese Funktion wird aufgerufen, wenn eine Option ausgewählt wird
        self.shell_cmd("pkexec sudo apt install " + app + " -y")
        self.kill_warten()
        self.installed_apps=str(self.shell_cmd("apt list --installed 2>/dev/null"))
        self.categoryButtons[cat].click()
        
    def start_warten(self):
        subprocess.Popen("python3 ./bitte_warten.py", shell=True)

    def kill_warten(self):
        subprocess.Popen("pkill -f bitte_warten.py", shell=True)   

    def check_flatremix_themes(self):
        testlist= [
            ["Blue","2777ff","Blau","4777ff"],
            ["Brown","c37837","Braun","f37837"],
            ["Cyan","0ccfd9","Türkis","2ccfd9"],
            ["Green","06a284","Grün","26a284"],
            ["Grey","737680","Grau","937680"],
            ["Magenta","cd0245","Magenta","fd0245"],
            ["Orange","fd7d00","Orange","fd7d00"],
            ["Red","ec0101","Rot","fc0101"],
            ["Teal","0099a1","Smaragdgrün","2099a1"],
            ["Violet","962ac3","Lila","b62ac3"],
            ["Yellow","ffd86e","Gelb","ffd86e"]
        ]
        themelist=[]
        for x in testlist:
            dark="/usr/share/themes/" + "Flat-Remix-GTK-" + x[0] + "-Darkest"
            mix="/usr/share/themes/" + "Flat-Remix-GTK-" + x[0] + "-Dark"
            light="/usr/share/themes/" + "Flat-Remix-GTK-" + x[0] + "-Light"
            if os.path.exists(dark) & os.path.exists(mix) & os.path.exists(light):
                themelist.append(x)
        
        return themelist
    
    def check_flatremix_icons(self):
        testlist= [
            ["Black","000000","Schwarz"],
            ["Blue","2777ff","Blau"],
            ["Brown","c37837","Braun"],
            ["Cyan","0ccfd9","Türkis"],
            ["Green","06a284","Grün"],
            ["Grey","737680","Grau"],
            ["Magenta","cd0245","Magenta"],
            ["Orange","fd7d00","Orange"],
            ["Red","ec0101","Rot"],
            ["Teal","0099a1","Smaragdgrün"],
            ["Violet","962ac3","Lila"],
            ["Yellow","ffd86e","Gelb"]
        ]

        iconslist=[]
        for x in testlist:
            dark="/usr/share/icons/" + "Flat-Remix-" + x[0] + "-Light-darkPanel"
            mix="/usr/share/icons/" + "Flat-Remix-" + x[0] + "-Dark"
            light="/usr/share/icons/" + "Flat-Remix-" + x[0] + "-Light"
            if os.path.exists(dark) & os.path.exists(mix) & os.path.exists(light):
                iconslist.append(x)
        return iconslist
    
    def color_change(self,color):
        current_theme = str(self.shell_cmd("xfconf-query -c xsettings -p /Net/ThemeName")[0])
        suffix="-Darkest"
        if current_theme.endswith("Light"):
            suffix="-Light"
        if current_theme.endswith("Dark"):
            suffix="-Dark"
        theme="Flat-Remix-GTK-"+color+suffix
        self.shell_cmd("xfconf-query -c xsettings -p /Net/ThemeName -s " + theme)
        self.categoryButtons[0].click()

    def icon_change(self,color):
        current_theme = str(self.shell_cmd("xfconf-query -c xsettings -p /Net/ThemeName")[0])
        iconsuffix="-Dark"
        darkmode = "false"
        if current_theme.endswith("Light"):
            iconsuffix="-Light"
            if self.shell_cmd("xfconf-query -c xfce4-panel -p /panels/dark-mode") != None:
                darkmode= str(self.shell_cmd("xfconf-query -c xfce4-panel -p /panels/dark-mode")[0])
            if darkmode.startswith("true"):
                iconsuffix="-Light-darkPanel"
        icons="Flat-Remix-"+color+iconsuffix
        self.shell_cmd("xfconf-query -c xsettings -p /Net/IconThemeName -s " + icons)
        current_icon_theme = str(self.shell_cmd("xfconf-query -c xsettings -p /Net/IconThemeName")[0])
        self.categoryButtons[0].click()

    def memory_clean_checker(self):
        self.label_clean_status.setText(" wird geprüft ")
        gewinntest = self.shell_cmd("bleachbit --preview --all-but-warning 2>/dev/null | grep Gewonnen")
        if gewinntest == ['']:
            gewinnbar = "nicht ermittelbar."
        else:
            gewinnbar = str(gewinntest[0].split(":")[1])
        self.label_clean_status.setText("Gewinnbarer Speicherplatz: " + gewinnbar)

    def memory_clean_cleaner(self):
        self.start_warten()
        time.sleep(1)
        self.label_clean_status.setText(" wird geprüft ")
        gewinntest = self.shell_cmd("pkexec bleachbit --clean --all-but-warning 2>/dev/null | grep Gewonnen")
        if gewinntest == ['']:
            gewinnbar = "nicht ermittelbar."
            self.label_clean_status.setText("Es war keine Bereinigung möglich.")
        else:
            gewinnbar = str(gewinntest[0].split(":")[1])
            self.label_clean_status.setText("Es wurden " + gewinnbar + " bereinigt.")
        self.kill_warten()
       

    def akzent_color(self):
        themelist = self.check_flatremix_themes()
        current_theme = str(self.shell_cmd("xfconf-query -c xsettings -p /Net/ThemeName")[0])
        btn_sel_color = '1f8973'
        if current_theme.startswith("Flat-Remix-"):
            theme = current_theme.replace("Flat-Remix-GTK-","")
            for x in themelist:
                if theme.startswith(x[0]):
                    btn_sel_color=x[1]
                    btn_sel_color1=x[3]


        self.sscat_btn_xs_sel=str("""
            QWidget {
            background-color: #130343;
            }
            QPushButton {
            font-size: """ + str(int(self.sts*0.8)) + """px; 
            text-align: left;      
            border-radius: """+ str(int(8*self.faktor))+""";
            background-color: #""" + btn_sel_color + """;
            border: 2px solid #""" + btn_sel_color + """;
            padding-top: 2px;
            padding-left: 5px;
            padding-right: 5px;
            padding-bottom: 2px;
            color: white;
            }
            QPushButton:hover {
            font-size: """ + str(int(int(self.sts)*0.9)) + """px;  
            background-color: #111111;
            border: 0px solid #111111;
            }
            """)
        
        self.ssbtn1=str("""
            QWidget {
            background-color: #130343;
            }
            QPushButton {
            font-size: """ + str(self.sts) + """px; 
            text-align: left;      
            border-radius: """+ str(int(8*self.faktor))+""";
            background-color: #""" + btn_sel_color  + """;
            border: 2px solid #""" + btn_sel_color  + """;
            padding-top: 2px;
            padding-left: 5px;
            padding-right: 5px;
            padding-bottom: 2px;
            color: white;
            }
            QPushButton:hover {
            font-size: """ + str(int(int(self.sts)/14*15)) + """px;  
            background-color: #111111;
            border: 2px solid #111111;
            }
            """)

        self.sslabelU=str("""
            QPushButton {
            font-size: """ + str(int(self.sts*1.7)) + """px; 
            text-align: left;      
            border-radius: """+ str(int(8*self.faktor))+""";
            background-color: #1a1a1a;
            border: 2px solid #1a1a1a;
            padding-top: 2px;
            padding-left: 5px;
            padding-right: 5px;
            padding-bottom: 2px;
            color: #""" + btn_sel_color1 + """;
            }
            """)

        current_theme = str(self.shell_cmd("xfconf-query -c xsettings -p /Net/ThemeName")[0])
        if current_theme != None:
            if current_theme.endswith("Dark"):
                self.setStyleSheet("background: rgba(35,37, 46, 255);")
                self.sscat=str("""
                    QLabel {
                    font-size: """ + str(self.sts) + """px; 
                    text-align: left;      
                    border-radius: """+ str(int(8*self.faktor))+""";
                    background-color: #1a1a1a;
                    border: 0px solid #131313;
                    padding-top: 2px;
                    padding-left: 5px;
                    padding-right: 5px;
                    padding-bottom: 2px;
                    color: yellow;
                    }
                    QWidget {
                    font-size: """ + str(self.sts) + """px; 
                    text-align: left;      
                    border-radius: """+ str(int(8*self.faktor))+""";
                    background-color: #1a1a1a;
                    border: 0px solid #131313;
                    padding-top: 2px;
                    padding-left: 5px;
                    padding-right: 5px;
                    padding-bottom: 2px;
                    color: yellow;
                    }
                    QComboBox {
                    font-size: """ + str(int(self.sts/2*1.8)) + """px; 
                    text-align: left;      
                    border-radius: 0px;
                    background-color: #282828;
                    border: 2px solid #282828;
                    padding-top: 2px;
                    padding-left: 5px;
                    padding-right: 5px;
                    padding-bottom: 2px;
                    color: white;
                    }
                    QPushButton {
                    font-size: """ + str(self.sts) + """px; 
                    text-align: left;      
                    border-radius: """ + str(int(int(self.sts)/2)) + """px;
                    background-color: #232323;
                    border: 0px solid #030303;
                    padding-top: 2px;
                    padding-left: 5px;
                    padding-right: 5px;
                    padding-bottom: 2px;
                    color: white;
                    }
                    QPushButton:hover {
                    font-size: """ + str(int(int(self.sts)/14*15)) + """px;  
                    background-color: #2b2b2b;
                    border: 0px solid #2b2b2b;
                    padding-top: 0px;
                    padding-left: 5px;
                    padding-right: 5px;
                    padding-bottom: 0px;
                    }
                    QListWidget {
                    font-size: """ + str(self.sts) + """px; 
                    text-align: left;      
                    border-radius: """ + str(int(int(self.sts)/2)) + """px;
                    background-color: #232323;
                    border: 1px solid #636363;
                    padding-top: 2px;
                    padding-left: 5px;
                    padding-right: 5px;
                    padding-bottom: 2px;
                    color: white;
                    }
                    QLineEdit {
                    font-size: """ + str(self.sts) + """px; 
                    text-align: left;      
                    border-radius: """ + str(int(int(self.sts)/2)) + """px;
                    background-color: #232323;
                    border: 1px solid #636363;
                    padding-top: 2px;
                    padding-left: 5px;
                    padding-right: 5px;
                    padding-bottom: 2px;
                    color: white;
                    }
                    """)

                self.sslabel=str("""
                    QLabel {
                    font-size: """ + str(self.sts) + """px; 
                    text-align: left;      
                    padding-top: 2px;
                    padding-left: 5px;
                    padding-right: 5px;
                    padding-bottom: 2px;
                    color: white;
                    }
                    QPushButton {
                    font-size: """ + str(self.sts) + """px; 
                    text-align: left;      
                    border-radius: """+ str(int(8*self.faktor))+""";
                    background-color: #1a1a1a;
                    border: 2px solid #1a1a1a;
                    padding-top: 2px;
                    padding-left: 5px;
                    padding-right: 5px;
                    padding-bottom: 2px;
                    color: white;
                    }
                    QPushButton:hover {
                    font-size: """ + str(self.sts) + """px; 
                    text-align: left;      
                    border-radius: """+ str(int(8*self.faktor))+""";
                    background-color: #1a1a1a;
                    border: 2px solid #1a1a1a;
                    padding-top: 2px;
                    padding-left: 5px;
                    padding-right: 5px;
                    padding-bottom: 2px;
                    color: white;
                    }
                    """)

            elif current_theme.endswith("Light"):
                #self.setStyleSheet("background: rgba(246,246, 246, 245);")
                self.setStyleSheet("background: white;")
                self.sscat=str("""
                    QLabel {
                    font-size: """ + str(self.sts) + """px; 
                    text-align: left;      
                    border-radius: """+ str(int(8*self.faktor))+""";
                    background-color: #404040;
                    border: 0px solid #131313;
                    padding-top: 2px;
                    padding-left: 5px;
                    padding-right: 5px;
                    padding-bottom: 2px;
                    color: yellow;
                    }
                    QWidget {
                    font-size: """ + str(self.sts) + """px; 
                    text-align: left;      
                    border-radius: """+ str(int(8*self.faktor))+""";
                    background-color: #404040;
                    border: 0px solid #131313;
                    padding-top: 2px;
                    padding-left: 5px;
                    padding-right: 5px;
                    padding-bottom: 2px;
                    color: yellow;
                    }
                    QComboBox {
                    font-size: """ + str(int(self.sts/2*1.8)) + """px; 
                    text-align: left;      
                    border-radius: 0px;
                    background-color: #282828;
                    border: 2px solid #282828;
                    padding-top: 2px;
                    padding-left: 5px;
                    padding-right: 5px;
                    padding-bottom: 2px;
                    color: white;
                    }
                    QPushButton {
                    font-size: """ + str(self.sts) + """px; 
                    text-align: left;      
                    border-radius: """ + str(int(int(self.sts)/2)) + """px;
                    background-color: #838383;
                    border: 0px solid #030303;
                    padding-top: 2px;
                    padding-left: 5px;
                    padding-right: 5px;
                    padding-bottom: 2px;
                    color: white;
                    }
                    QPushButton:hover {
                    font-size: """ + str(int(int(self.sts)/14*15)) + """px;  
                    background-color: #2b2b2b;
                    border: 0px solid #2b2b2b;
                    padding-top: 0px;
                    padding-left: 5px;
                    padding-right: 5px;
                    padding-bottom: 0px;
                    }
                    QListWidget {
                    font-size: """ + str(self.sts) + """px; 
                    text-align: left;      
                    border-radius: """ + str(int(int(self.sts)/2)) + """px;
                    background-color: #232323;
                    border: 1px solid #636363;
                    padding-top: 2px;
                    padding-left: 5px;
                    padding-right: 5px;
                    padding-bottom: 2px;
                    color: white;
                    }
                    QLineEdit {
                    font-size: """ + str(self.sts) + """px; 
                    text-align: left;      
                    border-radius: """ + str(int(int(self.sts)/2)) + """px;
                    background-color: #232323;
                    border: 1px solid #636363;
                    padding-top: 2px;
                    padding-left: 5px;
                    padding-right: 5px;
                    padding-bottom: 2px;
                    color: white;
                    }
                    """)
                self.sslabel=str("""
                    QLabel {
                    font-size: """ + str(self.sts) + """px; 
                    text-align: left;      
                    padding-top: 2px;
                    padding-left: 5px;
                    padding-right: 5px;
                    padding-bottom: 2px;
                    color: white;
                    }
                    QPushButton {
                    font-size: """ + str(self.sts) + """px; 
                    text-align: left;      
                    border-radius: """+ str(int(8*self.faktor))+""";
                    background-color: #404040;
                    border: 2px solid #404040;
                    padding-top: 2px;
                    padding-left: 5px;
                    padding-right: 5px;
                    padding-bottom: 2px;
                    color: white;
                    }
                    QPushButton:hover {
                    font-size: """ + str(self.sts) + """px; 
                    text-align: left;      
                    border-radius: """+ str(int(8*self.faktor))+""";
                    background-color: #404040;
                    border: 2px solid #404040;
                    padding-top: 2px;
                    padding-left: 5px;
                    padding-right: 5px;
                    padding-bottom: 2px;
                    color: white;
                    }
                    """)
            else:
                #self.setStyleSheet("background: rgba( 20, 20, 20, 240);") 
                self.setStyleSheet("background: rgba( 13, 13, 13, 255);") 
                self.sscat=str("""
                    QLabel {
                    font-size: """ + str(self.sts) + """px; 
                    text-align: left;      
                    border-radius: """+ str(int(8*self.faktor))+""";
                    background-color: #1a1a1a;
                    border: 0px solid #131313;
                    padding-top: 2px;
                    padding-left: 5px;
                    padding-right: 5px;
                    padding-bottom: 2px;
                    color: yellow;
                    }
                    QWidget {
                    font-size: """ + str(self.sts) + """px; 
                    text-align: left;      
                    border-radius: """+ str(int(8*self.faktor))+""";
                    background-color: #1a1a1a;
                    border: 0px solid #131313;
                    padding-top: 2px;
                    padding-left: 5px;
                    padding-right: 5px;
                    padding-bottom: 2px;
                    color: yellow;
                    }
                    QComboBox {
                    font-size: """ + str(int(self.sts/2*1.8)) + """px; 
                    text-align: left;      
                    border-radius: 0px;
                    background-color: #282828;
                    border: 2px solid #282828;
                    padding-top: 2px;
                    padding-left: 5px;
                    padding-right: 5px;
                    padding-bottom: 2px;
                    color: white;
                    }
                    QPushButton {
                    font-size: """ + str(self.sts) + """px; 
                    text-align: left;      
                    border-radius: """ + str(int(int(self.sts)/2)) + """px;
                    background-color: #232323;
                    border: 0px solid #030303;
                    padding-top: 2px;
                    padding-left: 5px;
                    padding-right: 5px;
                    padding-bottom: 2px;
                    color: white;
                    }
                    QPushButton:hover {
                    font-size: """ + str(int(int(self.sts)/14*15)) + """px;  
                    background-color: #2b2b2b;
                    border: 0px solid #2b2b2b;
                    padding-top: 0px;
                    padding-left: 5px;
                    padding-right: 5px;
                    padding-bottom: 0px;
                    }
                    QListWidget {
                    font-size: """ + str(self.sts) + """px; 
                    text-align: left;      
                    border-radius: """ + str(int(int(self.sts)/2)) + """px;
                    background-color: #232323;
                    border: 1px solid #636363;
                    padding-top: 2px;
                    padding-left: 5px;
                    padding-right: 5px;
                    padding-bottom: 2px;
                    color: white;
                    }
                    QLineEdit {
                    font-size: """ + str(self.sts) + """px; 
                    text-align: left;      
                    border-radius: """ + str(int(int(self.sts)/2)) + """px;
                    background-color: #232323;
                    border: 1px solid #636363;
                    padding-top: 2px;
                    padding-left: 5px;
                    padding-right: 5px;
                    padding-bottom: 2px;
                    color: white;
                    }
                    """)

                self.sslabel=str("""
                    QLabel {
                    font-size: """ + str(self.sts) + """px; 
                    text-align: left;      
                    padding-top: 2px;
                    padding-left: 5px;
                    padding-right: 5px;
                    padding-bottom: 2px;
                    color: white;
                    }
                    QPushButton {
                    font-size: """ + str(self.sts) + """px; 
                    text-align: left;      
                    border-radius: """+ str(int(8*self.faktor))+""";
                    background-color: #1a1a1a;
                    border: 2px solid #1a1a1a;
                    padding-top: 2px;
                    padding-left: 5px;
                    padding-right: 5px;
                    padding-bottom: 2px;
                    color: white;
                    }
                    QPushButton:hover {
                    font-size: """ + str(self.sts) + """px; 
                    text-align: left;      
                    border-radius: """+ str(int(8*self.faktor))+""";
                    background-color: #1a1a1a;
                    border: 2px solid #1a1a1a;
                    padding-top: 2px;
                    padding-left: 5px;
                    padding-right: 5px;
                    padding-bottom: 2px;
                    color: white;
                    }
                    """)



if __name__ == '__main__':
    app = QApplication(sys.argv)
    widget = MyWidget()
    sys.exit(app.exec_())
