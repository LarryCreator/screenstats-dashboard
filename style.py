page_bg_color = "#130A00"
sidebar_bg_color = "#130A00"
sidebar_border_color = "#2B1700"
topbar_bg_color = "#291F15"
topbar_font_color = "#CAB295"
searchbar_bg_color = "#3D2F20"
scrollbar_bg_color = "#252525"
subcard_title_color = "#BDBDBD"
color = 'rgba(0, 0, 0, 0.57)'

x2 = "#381F02"
style_sheet = f"""
            QFrame#sideBarFrame {{
                padding: 10px;
                background-color: {sidebar_bg_color}; 
                color: white;
                min-width: 240px;
                max-width: 240px;                
                border: 1px solid {sidebar_border_color};
            }}

            QFrame#topBar {{
                background-color: {topbar_bg_color}; 

            }}

            QFrame#titleFrame {{
                padding: 20px;
                min-width: 240px;
                max-width: 240px;
                }}               

            QLabel#mainHeader {{
                font-family: "Cinzel", "Trajan Pro", "Times New Roman", serif;
                text-transform: uppercase;
                letter-spacing: 2px;
                color: {'#c4a15b'}; 
                font-size: 17px;
                font-weight: bold;
            }}

            QLabel#myLibraryHeader {{
                font-family: "Cinzel", "Trajan Pro", "Times New Roman", serif;
                text-transform: uppercase;
                letter-spacing: 2px;
                color: {'#c4a15b'}; 
                font-size: 30px;
                font-weight: bold;

            }}

            QLabel#myLibrarySubHeader {{
                font-family: "Cinzel", "Trajan Pro", "Times New Roman", serif;
                letter-spacing: 2px;
                color: {topbar_font_color}; 
                font-size: 16px;
            }}

            QPushButton#mlAddTitleButton {{
                padding: 15px;
                font-size: 15px;
                border: None;
                border-radius: 10px;
                background: None;
                background-color: {'#c4a15b'};
                color: black;
            }}

            QPushButton#mlAddTitleButton:hover {{
                background-color: {"#a38342"};
            }}
                           
            QLineEdit {{
                background-color: {searchbar_bg_color};
                border: None;
                border-radius: 15px; /* Makes it look like a pill */
                padding: 5px 15px;
                font-size: 16px;
                color: {topbar_font_color};
            }}
            QLineEdit:focus {{
                border: 1px solid {topbar_font_color}; /* Change color when typing */
            }}
                
            QPushButton {{
                padding: 10px;
                font-size: 15px;
                border: None;
                border-radius: 5px;
                background: None;
                font-weight: bold;
                color: white;
                text-align: left;            
            }}

            QPushButton:hover {{
                background-color: #381F02;
            }}

            QPushButton#mlFilterButton {{
                padding: 7px;
                font-size: 14px;
                border: 1px solid gray;
                background: None;
                color: white;
                border-radius: 10px;
                text-align: center;
                min-width: 100px;
                max-width: 100px;            
            }}

            QPushButton#mlFilterButton:hover {{
                border: 1px solid {topbar_font_color};
            }}

            QComboBox#mlSortButton {{
                padding: 7px;
                border: 1px solid gray;
                background: None;
                background-color: transparent;
                font-size: 14px;
                color: white;
                border-radius: 10px;
                text-align: center;
                min-width: 190px;
                max-width: 190px;            
            }}

            QComboBox#mlSortButton:hover {{
                border: 1px solid {topbar_font_color};
            }}

            QComboBox#mlSortButton:focus {{
                border: 1px solid {topbar_font_color};
            }}

            QFrame#mlPage {{
                background-color: {page_bg_color};
            }}

            /* The background of the scrollbar */
            QScrollBar:vertical {{
                background: {scrollbar_bg_color};
                width: 12px;
                margin: 0px 0px 0px 0px;
                border: none;
            }}

            /* The actual draggable handle */
            QScrollBar::handle:vertical {{
                background: #c0c0c0;
                min-height: 20px;
                border-radius: 15px; /* Makes it rounded */
                margin: 2px;
            }}

            /* Handle color when hovering */
            QScrollBar::handle:vertical:hover {{
                background: #a0a0a0;
            }}

            /* Removes the arrows at the top and bottom */
            QScrollBar::add-line:vertical, QScrollBar::sub-line:vertical {{
                height: 0px;
            }}

            /* Removes the background area above/below the handle */
            QScrollBar::add-page:vertical, QScrollBar::sub-page:vertical {{
                background: none;
            }}

            QFrame[class="mediaCard"] {{
                background-repeat: no-repeat;
                background-position: center;
                min-height: 430px;
                max-height: 430px;
                min-width: 280px;
                max-width: 280px;
                border-radius: 15px;
            }}

            QLabel[class="cardTitle"] {{
                color: white;
                font-size: 15px;
                padding: 5px 0 0 5px;
            }}

            QLabel[class="subCardTitle"] {{
                color: {subcard_title_color};
                font-size: 12px;
                padding: 0 0 0 5px;

            }}

            QPushButton[class="cardRating"] {{
                margin: 0 0 10px 0;
                color: white;
                font-size: 13px;
                border: None;
                background: None;
                text-align: left;
                background-color: {color};            
            }}

            QLabel[class="cardYear"] {{
                color: white;
                font-size: 13px;
                margin: 0 0 10px 0;
                padding: 5px;
                border: None;
                background: None;
                text-align: left;
                background-color: {color};
                font-weight: bold;            
            }}
                           
        """