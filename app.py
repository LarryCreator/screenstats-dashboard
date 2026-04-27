import sys
import os
from PySide6.QtCore import Qt
from PySide6.QtGui import QIcon
from PySide6.QtWidgets import QApplication, QWidget, QPushButton, QLabel, QScrollArea, QGridLayout, QFrame, QVBoxLayout, QHBoxLayout, QLineEdit, QStackedWidget, QComboBox, QSizePolicy
from style import style_sheet

base_dir = os.path.dirname(__file__)

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
        self.layout.setColumnStretch(1, 1)
        self.layout.setSpacing(0)

        # Sidebar: Row 0, Col 0, spans 2 rows, span 1 column
        self.layout.addWidget(self.sidebar_frame, 0, 0, 2, 1)

        self.layout.addWidget(self.top_bar, 0, 1)
        self.layout.addWidget(self.scroll_area, 1, 1)

        self.sidebar_frame.setMinimumWidth(180)
        self.sidebar_frame.setMaximumWidth(250)
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
        self.pages.adjustSize()
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

    def create_new_button(self, display_text, obj_name, icon_path=None, page_index=None):
        button = QPushButton(display_text)
        button.setObjectName(obj_name)
        button.setCursor(Qt.PointingHandCursor)
        if icon_path is not None:
            button.setIcon(QIcon(icon_path))
        if page_index is not None:
            button.clicked.connect(lambda: self.app.pages.setCurrentIndex(page_index))
        return button

    def setup_buttons(self):
        icons_folder = 'icons'
        buttons = [
            {
                'icon': 'arrowOutwardIcon.png',
                'display_text': 'Dashboard',
                'obj_name': 'dashboardButton',
                'page_index': 0
            },
            {
                'icon': 'smartDisplayIcon.png',
                'display_text': 'My Library',
                'obj_name': 'myLibraryButton',
                'page_index': 1
            },
            {
                'icon': 'plusIcon.png',
                'display_text': 'Add Title',
                'obj_name': 'addTitleButton',
                'page_index': 2
            },
            {
                'icon': 'starIcon.png',
                'display_text': 'Recommendations',
                'obj_name': 'recommendationsButton',
                'page_index': 3
            },
            {
                'icon': 'swapIcon.png',
                'display_text': 'Import / Export',
                'obj_name': 'importExportButton',
                'page_index': 4
            },
            {
                'icon': 'gearIcon.png',
                'display_text': 'Settings',
                'obj_name': 'settingsButton',
                'page_index': 5
            },
            {
                'icon': None,
                'display_text': 'Light mode' if self.app.mode == 'dark' else 'Dark mode',
                'obj_name': 'lightDarkButton',
                'page_index': None
            }
        ]
    
        for button in buttons:
            if button['icon'] is not None:
                icon_path = os.path.join(base_dir, icons_folder, button['icon'])
            else:
                icon_path = None
            new_button = self.create_new_button(button['display_text'], button['obj_name'], icon_path, button['page_index'])
            if button['obj_name'] == 'lightDarkButton':
                new_button.clicked.connect(lambda: self.app.change_mode(new_button))
            self.layout.addWidget(new_button)


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
    
    def setup_cards(self):
        cards = [
            {'title': 'The Scream',
             'genre': 'Horror',
             'rating': 10,
             'year': 2004
             },
             {'title': 'Spider-Man',
             'genre': 'Action',
             'rating': 9,
             'year': 2009
             }
        ]
        
        column_number = 0
        row_number = 4
        for card in cards:
            new_card = MediaCard(card['title'], card['genre'], card['rating'], card['year'], f"card{row_number}-{column_number}")
            self.layout.addWidget(new_card, row_number, column_number)
            column_number += 1
            if column_number > 4:
                column_number = 0
                row_number += 1

        if len(cards) < 4:
            self.layout.setColumnStretch(column_number, 1)
        if len(cards) <= 5:
            self.layout.setRowStretch(5, 1)


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

class MediaCard(QFrame):
    def __init__(self, title, genre, rating, year, card_id):
        super().__init__()

        #temporary poster hardcoded path
        self.poster_path = os.path.join(base_dir, "images", "card.png").replace('\\', '/')

        self.setObjectName(str(card_id))
        self.setProperty('class', 'mediaCard')
        self.setStyleSheet(f"""
            QFrame#{str(card_id)} {{
                background-image: url("{self.poster_path}");
            }}
        """)

        self.layout = QGridLayout(self)
        self.layout.setRowStretch(0, 1)
        self.layout.setColumnStretch(4, 1)

        self.title_label = QLabel(title)
        self.title_label.setProperty('class', 'cardTitle')

        self.genre_label = QLabel(genre)
        self.genre_label.setProperty('class', 'subCardTitle')

        self.rating_badge = QPushButton(str(rating))
        self.rating_badge.setProperty('class', 'cardRating')
        icon_path = os.path.join(base_dir, 'icons', 'starIcon.png')
        safe_icon_path = icon_path.replace('\\', '/')
        self.rating_badge.setIcon(QIcon(safe_icon_path))

        self.year_badge = QLabel(str(year))
        self.year_badge.setProperty('class', 'cardYear')

        self.layout.setContentsMargins(15, 15, 15, 15)
        self.layout.addWidget(self.rating_badge, 1, 3, 1, 1)
        self.layout.addWidget(self.year_badge, 1, 0, 1, 1)
        self.layout.addWidget(self.title_label, 2, 0, 1, -1)
        self.layout.addWidget(self.genre_label, 3, 0, 1, -1)

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