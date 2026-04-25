style_sheet = """
            QFrame#sideBarFrame {
                padding: 10px;
                background-color: #333; 
                color: white;                
            
            }

            QFrame#titleFrame {
                padding: 20px;
                }               

            QLabel#mainHeader {
                font-family: "Cinzel", "Trajan Pro", "Times New Roman", serif;
                text-transform: uppercase;
                letter-spacing: 2px;
                color: #c4a15b; 
                font-size: 17px;
                font-weight: bold;

            }
                           
            QLineEdit {
                background-color: #f0f0f0;
                border: 1px solid #ccc;
                border-radius: 15px; /* Makes it look like a pill */
                padding: 5px 15px;
                font-size: 14px;
            }
            QLineEdit:focus {
                border: 1px solid #3498db; /* Change color when typing */
            }
                
            QPushButton {
                padding: 10px;
                font-size: 15px;
                border: 2px solid gray;
                background: None;
                font-weight: bold;
                color: white;            
            }
                           
        """