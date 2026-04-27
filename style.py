page_bg_color = "#130A00"
sidebar_bg_color = "#130A00"
sidebar_border_color = "#2B1700"
topbar_bg_color = "#291F15"
topbar_font_color = "#CAB295"
searchbar_bg_color = "#3D2F20"

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
                color: #c4a15b; 
                font-size: 17px;
                font-weight: bold;
            }}

            QLabel#myLibraryHeader {{
                font-family: "Cinzel", "Trajan Pro", "Times New Roman", serif;
                text-transform: uppercase;
                letter-spacing: 2px;
                color: #c4a15b; 
                font-size: 30px;
                font-weight: bold;

            }}

            QLabel#myLibrarySubHeader {{
                font-family: "Cinzel", "Trajan Pro", "Times New Roman", serif;
                letter-spacing: 2px;
                color: gray; 
                font-size: 16px;
                font-weight: bold;
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
                padding: 10px;
                font-size: 15px;
                border: 2px solid gray;
                background: None;
                font-weight: bold;
                color: white;
                border-radius: 10px;
                text-align: center;            
            }}

            QFrame#mlPage {{
                background-color: {page_bg_color};
            }}
                           
        """