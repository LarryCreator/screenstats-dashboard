import sys
import os
from PySide6.QtCore import Qt
from PySide6.QtGui import QIcon
from PySide6.QtWidgets import QApplication, QWidget, QPushButton, QLabel, QScrollArea, QGridLayout, QFrame, QVBoxLayout, QHBoxLayout, QLineEdit, QStackedWidget, QComboBox, QSizePolicy
from style import style_sheet


class ScreenStats(QWidget):
    def __init__(self):
        super().__init__()
        self.title = 'ScreenStats'
        self.mode = 'dark'
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
        self.scroll_area = QScrollArea()
        self.scroll_area.setWidget(self.pages)
        self.scroll_area.setWidgetResizable(True)
        self.scroll_area.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.scroll_area.setFrameShape(QFrame.NoFrame)

        self.pages.addWidget(self.dashboard_page)
        self.pages.addWidget(self.my_library_page)
        self.pages.addWidget(self.add_title_page)
        self.pages.addWidget(self.recommendations_page)
        self.pages.addWidget(self.import_export_page)
        self.pages.addWidget(self.settings_page)
        self.pages.setCurrentIndex(1)
        self.pages.currentChanged.connect(self.update_scroll_area_size)



        self.layout = QGridLayout()
        self.setup_main_layout()

        self.setStyleSheet(style_sheet)

    def setup_main_layout(self):
        self.layout.setContentsMargins(0,0,0,0)
        self.layout.setColumnStretch(0, 0)

        # Sidebar: Row 0, Col 0, spans 2 rows, span 1 column
        self.layout.addWidget(self.sidebar_frame, 0, 0, 2, 1)

        self.layout.addWidget(self.top_bar, 0, 1)
        self.layout.addWidget(self.scroll_area, 1, 1)

        # MAGIC LINES: Tell the grid where to push the "empty" space
        self.layout.setColumnStretch(1, 1) # Column 1 (content) takes all extra width


        self.sidebar_frame.setMinimumWidth(180)
        self.sidebar_frame.setMaximumWidth(250)
        self.layout.setSpacing(0)
        self.setLayout(self.layout)

    def change_mode(self, button):
        self.mode = 'dark' if self.mode == 'light' else 'light'
        button.setText('Light mode' if self.mode == 'dark' else 'Dark mode') 

    def update_scroll_area_size(self, index):
        # Get the new page
        current_page = self.pages.widget(index)
        
        # Loop through all pages to ignore their size, except the current one
        for i in range(self.pages.count()):
            page = self.pages.widget(i)
            if i == index:
                # Current page should grow/shrink naturally
                page.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
            else:
                # Hidden pages should not influence the ScrollArea size
                page.setSizePolicy(QSizePolicy.Ignored, QSizePolicy.Ignored)
                
        # Force the stack and scroll area to recalculate layout
        current_page.adjustSize()
        self.page.adjustSize()
        # Reset scroll to top for the new page
        self.scroll_area.verticalScrollBar().setValue(0)

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
        base_dir = os.path.dirname(__file__)

        dashboard_button = QPushButton('Dashboard')
        dashboard_button.setObjectName('dashboardButton')
        dashboard_button.setCursor(Qt.PointingHandCursor)
        dashboard_icon_path = os.path.join(base_dir, "icons", "arrowOutwardIcon.png")
        dashboard_button.setIcon(QIcon(dashboard_icon_path))
        dashboard_button.clicked.connect(lambda: self.app.pages.setCurrentIndex(0))

        my_library_button = QPushButton('My Library')
        my_library_button.setObjectName('myLibraryButton')
        my_library_button.setCursor(Qt.PointingHandCursor)
        my_library_icon_path = os.path.join(base_dir, "icons", "smartDisplayIcon.png")
        my_library_button.setIcon(QIcon(my_library_icon_path))
        my_library_button.clicked.connect(lambda: self.app.pages.setCurrentIndex(1))

        add_title_button = QPushButton('Add Title')
        add_title_button.setObjectName('addTitleButton')
        add_title_button.setCursor(Qt.PointingHandCursor)
        add_title_icon_path = os.path.join(base_dir, "icons", "plusIcon.png")
        add_title_button.setIcon(QIcon(add_title_icon_path))
        add_title_button.clicked.connect(lambda: self.app.pages.setCurrentIndex(2))

        recommendations_button = QPushButton('Recommendations')
        recommendations_button.setObjectName('recommendationsButton')
        recommendations_button.setCursor(Qt.PointingHandCursor)
        recommendations_icon_path = os.path.join(base_dir, "icons", "starIcon.png")
        recommendations_button.setIcon(QIcon(recommendations_icon_path))
        recommendations_button.clicked.connect(lambda: self.app.pages.setCurrentIndex(3))

        import_export_button = QPushButton('Import / Export')
        import_export_button.setObjectName('importExportButton')
        import_export_button.setCursor(Qt.PointingHandCursor)
        import_export_icon_path = os.path.join(base_dir, "icons", "swapIcon.png")
        import_export_button.setIcon(QIcon(import_export_icon_path))
        import_export_button.clicked.connect(lambda: self.app.pages.setCurrentIndex(4))

        settings_button = QPushButton('Settings')
        settings_button.setObjectName('settingsButton')
        settings_icon_path = os.path.join(base_dir, "icons", "gearIcon.png")
        settings_button.setIcon(QIcon(settings_icon_path))
        settings_button.setCursor(Qt.PointingHandCursor)
        settings_button.clicked.connect(lambda: self.app.pages.setCurrentIndex(5))

        light_dark_button = QPushButton('Light mode' if self.app.mode == 'dark' else 'Dark mode')
        light_dark_button.setObjectName('lightDarkButton')
        light_dark_button.setCursor(Qt.PointingHandCursor)
        light_dark_button.clicked.connect(lambda: self.app.change_mode(light_dark_button))

        self.layout.addWidget(dashboard_button)
        self.layout.addWidget(my_library_button)
        self.layout.addWidget(add_title_button)
        self.layout.addWidget(recommendations_button)
        self.layout.addWidget(import_export_button)
        self.layout.addWidget(settings_button)
        self.layout.addWidget(light_dark_button)


class TopBar(QFrame):
    def __init__(self):
        super().__init__()
        self.layout = QHBoxLayout(self)
        self.setObjectName('topBar')
        self.search_bar = QLineEdit()
        self.search_bar.setPlaceholderText('Search movies & series...')
        self.layout.addWidget(self.search_bar)
        self.setFixedHeight(60)

class DashboardPage(QFrame):
    def __init__(self):
        super().__init__()
        self.layout = QGridLayout()
        test_label = QLabel('Dashboard Page')
        self.layout.addWidget(test_label, 0, 0)
        self.setLayout(self.layout)

class MyLibraryPage(QFrame):
    def __init__(self):
        super().__init__()
        self.setObjectName('mlPage')
        self.layout = QGridLayout()
        self.main_header = QLabel('My Library')
        self.main_header.setObjectName('myLibraryHeader')
        self.sub_header = QLabel('You have 8 titles in your collection')
        self.sub_header.setObjectName('myLibrarySubHeader')

        self.setup_buttons()
        self.setup_cards()
        
        self.layout.addWidget(self.main_header, 0, 0)
        self.layout.addWidget(self.sub_header, 1, 0)
        

        self.layout.setSpacing(25)
        self.layout.setContentsMargins(30, 30, 30, 30)
        self.setLayout(self.layout)

    def new_movie_card(self, title,  genre, rating, year):
        base_dir = os.path.dirname(__file__)
        card_path = os.path.join(base_dir, "images", "card.png")
        safe_path = card_path.replace('\\', '/')
        movie_image = QFrame()
        card_layout = QGridLayout(movie_image)
        movie_image.setObjectName('test')
        movie_image.setStyleSheet(f"""
            QFrame#test {{
                background-image: url("{safe_path}");
                background-repeat: no-repeat;
                background-position: center;
                min-height: 430px;
                max-height: 430px;
                min-width: 300px;
                max-width: 300px;
            }}
        """)
        return movie_image
    
    def setup_cards(self):
        self.layout.addWidget(self.new_movie_card('The Scream', '', 10, 2020), 4, 0)
        self.layout.addWidget(self.new_movie_card('The Scream', '', 10, 2020), 4, 1)
        self.layout.addWidget(self.new_movie_card('The Scream', '', 10, 2020), 4, 2)
        self.layout.addWidget(self.new_movie_card('The Scream', '', 10, 2020), 4, 3)
        self.layout.addWidget(self.new_movie_card('The Scream', '', 10, 2020), 4, 4)
        self.layout.addWidget(self.new_movie_card('The Scream', '', 10, 2020), 5, 0)

    def setup_buttons(self):
        filter_button = QPushButton('Filters')
        filter_button.setObjectName('mlFilterButton')
        filter_button.setCursor(Qt.PointingHandCursor)

        sort_button = QComboBox()
        options = ['Sort by: Title', 'Sort by: Date Added', 'Sort by: Rating', 'Sort by: Year']
        sort_button.insertItems(0, options)
        sort_button.setObjectName('mlSortButton')
        sort_button.setCursor(Qt.PointingHandCursor)

        self.layout.addWidget(filter_button, 3, 0)
        self.layout.addWidget(sort_button, 3, 1)

class AddTitlePage(QFrame):
    def __init__(self):
        super().__init__()
        self.layout = QGridLayout()
        test_label = QLabel('Add Title Page')
        self.layout.addWidget(test_label, 0, 0)
        self.setLayout(self.layout)

class RecommendationsPage(QFrame):
    def __init__(self):
        super().__init__()
        self.layout = QGridLayout()
        test_label = QLabel('Recommendations Page')
        self.layout.addWidget(test_label, 0, 0)
        self.setLayout(self.layout)

class ImportExportPage(QFrame):
    def __init__(self):
        super().__init__()
        self.layout = QGridLayout()
        test_label = QLabel('Import / Export Page')
        self.layout.addWidget(test_label, 0, 0)
        self.setLayout(self.layout)

class SettingsPage(QFrame):
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