from PySide6.QtWidgets import QPushButton, QLabel, QGridLayout, QFrame, QComboBox
from PySide6.QtCore import Qt
from PySide6.QtGui import QIcon
import os

base_dir = os.path.dirname(__file__)
icons_folder = 'icons'

class MyLibraryPage(QFrame):
    def __init__(self, app):
        super().__init__()
        self.app = app
        self.setObjectName('myLibraryPage')
        self.layout = QGridLayout()
        self.buttons_frame = QFrame()
        self.buttons_frame_layout = QGridLayout(self.buttons_frame)
        self.cards = []
        self.setup_buttons()
        self.setup_cards()
        self.main_header = QLabel('My Library')
        self.main_header.setObjectName('myLibraryHeader')
        self.sub_header = QLabel(f'{len(self.cards)} titles in your collection')
        self.sub_header.setObjectName('myLibrarySubHeader')
        self.setup_layout()
        
    def setup_buttons_frame_layout(self):
        self.buttons_frame_layout.setColumnStretch(2, 1)
        self.buttons_frame_layout.setSpacing(20)
        self.buttons_frame_layout.setContentsMargins(0, 0, 0, 0)


    def setup_layout(self):
        self.setup_buttons_frame_layout()
        self.layout.addWidget(self.main_header, 0, 0)
        self.layout.addWidget(self.sub_header, 1, 0)
        self.layout.addWidget(self.buttons_frame, 2, 0, 1, -1)


        self.layout.setSpacing(25)
        self.layout.setContentsMargins(30, 30, 30, 30)

        my_cards_length = len(self.cards)

        if my_cards_length < 4 and my_cards_length >= 2:
            self.layout.setColumnStretch(len(self.cards), 1)
        elif my_cards_length == 1 or my_cards_length == 0:
            self.layout.setColumnStretch(2, 1)

        if len(self.cards) <= 5:
            self.layout.setRowStretch(5, 1)

        self.setLayout(self.layout)
    
    def setup_cards(self):
        self.cards = [
            {'title': 'The Scream',
             'genre': 'Horror',
             'rating': 10,
             'year': 2004
             },
             {'title': 'The Scream',
             'genre': 'Horror',
             'rating': 10,
             'year': 2004
             },
             {'title': 'The Scream',
             'genre': 'Horror',
             'rating': 10,
             'year': 2004
             },
             {'title': 'The Scream',
             'genre': 'Horror',
             'rating': 10,
             'year': 2004
             },
             {'title': 'The Scream',
             'genre': 'Horror',
             'rating': 10,
             'year': 2004
             },
        ]
        
        column_number = 0
        row_number = 4
        for card in self.cards:
            new_card = MediaCard(card['title'], card['genre'], card['rating'], card['year'], f"card{row_number}-{column_number}")
            self.layout.addWidget(new_card, row_number, column_number)
            column_number += 1
            if column_number > 4:
                column_number = 0
                row_number += 1

    def setup_buttons(self):
        add_title_button_icon_path = os.path.join(base_dir, "..", icons_folder, 'plusBlackIcon.png')
        add_title_button = self.app.create_new_button('Add Title', 'mlAddTitleButton', add_title_button_icon_path, 2)

        filter_button_icon_path = os.path.join(base_dir, "..", icons_folder, 'filterIcon.png')
        filter_button = self.app.create_new_button('Filters', 'mlFilterButton', filter_button_icon_path, None)

        self.setup_sort_button()
        
        self.buttons_frame_layout.addWidget(filter_button, 0, 0)
        self.buttons_frame_layout.addWidget(self.sort_button, 0, 1)
        self.buttons_frame_layout.addWidget(add_title_button, 0, 3)
    
    def setup_sort_button(self):
        self.sort_button = QComboBox()

        options = ['Sort by: Title', 'Sort by: Date Added', 'Sort by: Rating', 'Sort by: Year']

        self.sort_button.insertItems(0, options)
        self.sort_button.setObjectName('mlSortButton')

        self.sort_button.setEditable(True)
        self.sort_button.lineEdit().setReadOnly(True)
        self.sort_button.lineEdit().setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.sort_button.lineEdit().installEventFilter(self)
        self.sort_button.installEventFilter(self)
        self.sort_button.setCursor(Qt.CursorShape.PointingHandCursor)
        self.sort_button.lineEdit().setCursor(Qt.CursorShape.PointingHandCursor)
        self.sort_button.lineEdit().setFocusPolicy(Qt.FocusPolicy.NoFocus)

    #this even is necessary for the comboBox to be clickable anywhere on itself
    def eventFilter(self, obj, event):
        if obj == self.sort_button.lineEdit() or obj == self.sort_button:
            # Trigger popup on MouseButtonRelease (standard click behavior)
            if event.type() == event.Type.MouseButtonRelease:
                if event.button() == Qt.MouseButton.LeftButton:
                    self.sort_button.showPopup()
                    self.sort_button.setFocus()
                    return True
        return super().eventFilter(obj, event)  

class MediaCard(QFrame):
    def __init__(self, title, genre, rating, year, card_id):
        super().__init__()

        #temporary poster hardcoded path
        self.poster_path = os.path.join(base_dir, "..", "images", "card.png").replace('\\', '/')

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