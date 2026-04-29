import sys
import os
from PySide6.QtCore import Qt
from PySide6.QtGui import QIcon
from PySide6.QtWidgets import QApplication, QWidget, QPushButton, QLabel, QScrollArea, QGridLayout, QFrame, QVBoxLayout, QHBoxLayout, QLineEdit, QStackedWidget, QComboBox, QSizePolicy
from style import style_sheet
from pages.my_library_page import MyLibraryPage

base_dir = os.path.dirname(__file__)
icons_folder = 'icons'

class ScreenStats(QWidget):
    def __init__(self):
        super().__init__()
        self.title = 'ScreenStats'
        self.mode = 'dark'
        self.setWindowTitle(self.title)

        self.dashboard_page = DashboardPage()
        self.my_library_page = MyLibraryPage(self)
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
        self.pages.setCurrentIndex(2)
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

    def create_new_button(self, display_text, obj_name, icon_path=None, page_index=None):
        button = QPushButton(display_text)
        button.setObjectName(obj_name)
        button.setCursor(Qt.PointingHandCursor)
        if icon_path is not None:
            button.setIcon(QIcon(icon_path))
        if page_index is not None:
            button.clicked.connect(lambda: self.pages.setCurrentIndex(page_index))
        return button

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
            new_button = self.app.create_new_button(button['display_text'], button['obj_name'], icon_path, button['page_index'])
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

class AddTitlePage(QFrame):
    def __init__(self):
        super().__init__()
        self.setObjectName('addTitlePage')
        self.layout = QGridLayout()
        self.main_header = QLabel('Add Title Page')
        # For the Main Header
        self.main_header.setAlignment(Qt.AlignmentFlag.AlignLeft | Qt.AlignmentFlag.AlignVCenter)
        self.sub_header = QLabel('Search and add a new movie or series to your library')
        self.sub_header.setAlignment(Qt.AlignmentFlag.AlignLeft | Qt.AlignmentFlag.AlignVCenter)

        self.main_header.setObjectName('addTitleMainHeader')
        self.sub_header.setObjectName('addTitleSubHeader')
        self.setContentsMargins(0, 30, 0, 0)
        self.setup_layout()

    def setup_layout(self):
        self.layout.addWidget(self.main_header, 0, 1)
        self.layout.addWidget(self.sub_header, 1, 1)

        self.layout.setColumnStretch(0, 1)
        self.layout.setColumnStretch(2, 1)
        self.layout.setRowStretch(2, 1)

        self.layout.setSpacing(11)
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