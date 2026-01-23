import re
from PyQt6 import QtGui
from PyQt6 import QtWidgets
from PyQt6.QtWidgets import QMainWindow, QMessageBox, QTableWidgetItem
from music_ui import Ui_MainWindow
from music_db import MusicManagementDB
from PyQt6.QtWidgets import QColorDialog
from PyQt6.QtCore import QSettings
import matplotlib.pyplot as plt
from collections import Counter
import random
from PyQt6.QtCore import QVariantAnimation
from PyQt6.QtGui import QColor

class MusicApp(QMainWindow):

    #INITIALIZATION
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.settings = QSettings("YourApp", "MusicManagementSystem")
        self.load_last_theme() 
        self.ui.tabWidget.tabBar().hide()
        self.db = MusicManagementDB()
        self.current_song_id = None
        self.setup_connections()
        self.setup_shortcuts()
        self.ui.tabWidget.setCurrentIndex(0)
        self.load_table()

    def setup_connections(self):

        # Page Buttons
        self.ui.signB.clicked.connect(self.show_log_page)
        self.ui.viewB.clicked.connect(self.show_view_page)
        self.ui.addB.clicked.connect(self.show_add_page)
        self.ui.editB.clicked.connect(self.show_edit_page)
        self.ui.playlistB.clicked.connect(self.show_playlist_page)
        self.ui.profileB.clicked.connect(self.show_profile_page)
        self.ui.profile_table.itemSelectionChanged.connect(self.handle_profile_selection)
        self.ui.forgotB.clicked.connect(self.show_reset_password_dialog)
        self.ui.saveB_1.clicked.connect(self.save_song)
        self.ui.searchB.clicked.connect(self.search_song)
        self.ui.saveB_2.clicked.connect(self.update_song)
        self.ui.deleteB.clicked.connect(self.delete_song)
        self.ui.genB.clicked.connect(self.generate_list)
        self.ui.edit_photoB.clicked.connect(self.show_trash_popup)  # NEW
        self.ui.removeB.clicked.connect(self.remove)
        self.ui.logoutB.clicked.connect(self.log_out)
        self.ui.delete_acB.clicked.connect(self.delete_account)
        self.ui.enterB.clicked.connect(self.log)
        # menu bar
        self.ui.actionAbout.triggered.connect(self.show_about_dialog)
        self.ui.actionHelp.triggered.connect(self.show_help_dialog)
        self.ui.actionExit.triggered.connect(self.close_app)
        
        self.ui.actionDefault.triggered.connect(lambda: self.apply_theme("default"))
        self.ui.actionGlass.triggered.connect(lambda: self.apply_theme("glass"))
        self.ui.actionSunset.triggered.connect(lambda: self.apply_theme("sunset"))
        self.ui.actionSimple.triggered.connect(lambda: self.apply_theme("simple"))
        self.ui.actionDark.triggered.connect(lambda: self.apply_theme("dark"))
        self.ui.actionLight.triggered.connect(lambda: self.apply_theme("light"))
        self.ui.actionCoffee.triggered.connect(lambda: self.apply_theme("coffee"))
        self.ui.actionCustom.triggered.connect(self.set_custom_theme)
        self.ui.view_filter_button.clicked.connect(self.apply_view_filters)
        self.ui.viewLyricsB.clicked.connect(self.view_lyrics_popup)
        self.ui.statsB.clicked.connect(self.show_stats_popup)
        self.ui.password_in.textChanged.connect(self.check_password_strength)



    # UI Setup and Themes
    def setup_shortcuts(self):
        shortcut_dark = QtGui.QShortcut(QtGui.QKeySequence("Ctrl+Shift+D"), self)
        shortcut_dark.activated.connect(lambda: self.apply_theme("dark"))

        shortcut_light = QtGui.QShortcut(QtGui.QKeySequence("Ctrl+Shift+L"), self)
        shortcut_light.activated.connect(lambda: self.apply_theme("light"))

        shortcut_default = QtGui.QShortcut(QtGui.QKeySequence('Ctrl+Shift+B'), self)
        shortcut_default.activated.connect(lambda: self.apply_theme('default'))

    def load_last_theme(self):
        theme_name = self.settings.value("theme_name", "default")
        if theme_name == "custom":
            colors = self.settings.value("custom_colors", [])
            if colors and isinstance(colors, list) and len(colors) == 3:
                self.set_label_colors(colors)
        else:
            self.apply_theme(theme_name)

    def apply_theme(self, theme_name):
        themes = {
            "default": ["#0A1828", "#178582", "#6C757D"],
            "simple": ["#f0f0f0", "#e0e0e0", "#d0d0d0"],
            "dark": ["#2b2b2b", "#3c3c3c", "#4d4d4d"],
            "light": ["#ffffff", "#eeeeee", "#dddddd"],
            "coffee": ["#cba987", "#a67c52", "#6f4e37"],
            "glass": ["#e0f7fa", "#b2ebf2", "#80deea"],
            "sunset": ["#ffccbc", "#ffab91", "#ff8a65"]
        }

        if theme_name in themes:
            self.set_label_colors(themes[theme_name])
            self.settings.setValue("theme_name")