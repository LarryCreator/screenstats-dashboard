import sys
from PySide6.QtCore import Qt
from PySide6.QtWidgets import QApplication, QWidget, QPushButton, QLabel, QCheckBox, QGridLayout, QFrame, QVBoxLayout, QHBoxLayout, QLineEdit, QStackedWidget
from style import style_sheet


class ScreenStats(QWidget):
    def __init__(self):
        super().__init__()
        self.title = 'ScreenStats'
        self.setWindowTitle(self.title)

        self.dashboard_page = DashboardPage()
        self.my_library_page = MyLibraryPage()
        self.add_title_page = AddTitlePage()
        self.recommendations_page = RecommendationsPage()
        self.import_export_page = ImportExportPage()
        self.settings_page = SettingsPage()
        self.pages = QStackedWidget()
        self.top_bar = TopBar()
        self.sidebar_frame = SideBar(self)

        self.pages.addWidget(self.dashboard_page)
        self.pages.addWidget(self.my_library_page)
        self.pages.addWidget(self.add_title_page)
        self.pages.addWidget(self.recommendations_page)
        self.pages.addWidget(self.import_export_page)
        self.pages.addWidget(self.settings_page)
        self.pages.setCurrentIndex(1)


        self.layout = QGridLayout()
        self.setup_main_layout()

        self.setStyleSheet(style_sheet)

    def setup_main_layout(self):
        self.layout.setContentsMargins(0,0,0,0)
        self.layout.setColumnStretch(0, 0)
        self.layout.setColumnStretch(1, 1)

        # Sidebar: Row 0, Col 0, spans 2 rows, span 1 column
        self.layout.addWidget(self.sidebar_frame, 0, 0, 2, 1)

        self.layout.addWidget(self.top_bar, 0, 1)
        self.layout.addWidget(self.pages, 1, 1)

        # MAGIC LINES: Tell the grid where to push the "empty" space
        self.layout.setColumnStretch(1, 1) # Column 1 (content) takes all extra width
        self.layout.setRowStretch(1, 1)    # Row 1 (bottom) takes all extra height


        self.sidebar_frame.setMinimumWidth(180)
        self.sidebar_frame.setMaximumWidth(250)

        self.setLayout(self.layout)

class SideBar(QFrame):
    def __init__(self, app):
        super().__init__()
        self.app = app
        self.layout = QVBoxLayout(self)
        self.setObjectName('sideBarFrame')

        title_frame = QFrame()
        title_frame_layout = QVBoxLayout(title_frame)
        self.title_label = QLabel('ScreenStats')

        title_frame.setObjectName('titleFrame')
        self.title_label.setObjectName('mainHeader')

        title_frame_layout.addWidget(self.title_label)
        self.layout.addWidget(title_frame)
        self.setup_buttons()

        self.layout.addStretch() #throws everyhing to the top
        self.layout.setSpacing(15)

    def setup_buttons(self):
        dashboard_button = QPushButton('Dashboard')
        dashboard_button.setObjectName('dashboardButton')
        dashboard_button.setCursor(Qt.PointingHandCursor)
        dashboard_button.clicked.connect(lambda: self.app.pages.setCurrentIndex(0))

        my_library_button = QPushButton('My Library')
        my_library_button.setObjectName('myLibraryButton')
        my_library_button.setCursor(Qt.PointingHandCursor)
        my_library_button.clicked.connect(lambda: self.app.pages.setCurrentIndex(1))

        add_title_button = QPushButton('Add Title')
        add_title_button.setObjectName('addTitleButton')
        add_title_button.setCursor(Qt.PointingHandCursor)
        add_title_button.clicked.connect(lambda: self.app.pages.setCurrentIndex(2))

        recommendations_button = QPushButton('Recommendations')
        recommendations_button.setObjectName('recommendationsButton')
        recommendations_button.setCursor(Qt.PointingHandCursor)
        recommendations_button.clicked.connect(lambda: self.app.pages.setCurrentIndex(3))

        import_export_button = QPushButton('Import / Export')
        import_export_button.setObjectName('importExportButton')
        import_export_button.setCursor(Qt.PointingHandCursor)
        import_export_button.clicked.connect(lambda: self.app.pages.setCurrentIndex(4))

        settings_button = QPushButton('Settings')
        settings_button.setObjectName('settingsButton')
        settings_button.setCursor(Qt.PointingHandCursor)
        settings_button.clicked.connect(lambda: self.app.pages.setCurrentIndex(5))


        self.layout.addWidget(dashboard_button)
        self.layout.addWidget(my_library_button)
        self.layout.addWidget(add_title_button)
        self.layout.addWidget(recommendations_button)
        self.layout.addWidget(import_export_button)
        self.layout.addWidget(settings_button)

class TopBar(QFrame):
    def __init__(self):
        super().__init__()
        self.layout = QHBoxLayout(self)
        self.setObjectName('topBar')
        self.search_bar = QLineEdit()
        self.search_bar.setPlaceholderText('Search movies & series...')
        self.layout.addWidget(self.search_bar)
        self.setFixedHeight(60)

class DashboardPage(QWidget):
    def __init__(self):
        super().__init__()
        self.layout = QGridLayout()
        test_label = QLabel('Dashboard Page')
        self.layout.addWidget(test_label, 0, 0)
        self.setLayout(self.layout)

class MyLibraryPage(QWidget):
    def __init__(self):
        super().__init__()
        self.layout = QGridLayout()
        test_label = QLabel('My Library Page')
        self.layout.addWidget(test_label, 0, 0)
        self.setLayout(self.layout)

class AddTitlePage(QWidget):
    def __init__(self):
        super().__init__()
        self.layout = QGridLayout()
        test_label = QLabel('Add Title Page')
        self.layout.addWidget(test_label, 0, 0)
        self.setLayout(self.layout)

class RecommendationsPage(QWidget):
    def __init__(self):
        super().__init__()
        self.layout = QGridLayout()
        test_label = QLabel('Recommendations Page')
        self.layout.addWidget(test_label, 0, 0)
        self.setLayout(self.layout)

class ImportExportPage(QWidget):
    def __init__(self):
        super().__init__()
        self.layout = QGridLayout()
        test_label = QLabel('Import / Export Page')
        self.layout.addWidget(test_label, 0, 0)
        self.setLayout(self.layout)

class SettingsPage(QWidget):
    def __init__(self):
        super().__init__()
        self.layout = QGridLayout()
        test_label = QLabel('Settings Page')
        self.layout.addWidget(test_label, 0, 0)
        self.setLayout(self.layout)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    screenstats = ScreenStats()
    screenstats.showFullScreen()
    app.exec()