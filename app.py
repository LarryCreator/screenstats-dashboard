import sys
from PySide6.QtCore import Qt
from PySide6.QtWidgets import QApplication, QWidget, QPushButton, QLabel, QCheckBox, QGridLayout, QFrame, QVBoxLayout, QHBoxLayout, QLineEdit


class ScreenStats(QWidget):
    def __init__(self):
        super().__init__()
        self.title = 'ScreenStats'
        self.setWindowTitle(self.title)
        self.search_bar = QLineEdit()

        self.top_bar = QFrame()
        self.sidebar_frame = QFrame()
        self.sidebar_layout = QVBoxLayout(self.sidebar_frame)
        self.top_bar_layout = QHBoxLayout(self.top_bar)
        self.main_content = QLabel("Main Dashboard Content Goes Here")

        self.layout = QGridLayout()

        self.setup_sidebar()
        self.setup_top_bar()
        self.setup_main_layout()

        self.setStyleSheet("""
            QFrame#sideBarFrame {
                padding: 10px;               
            
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
                
            QPushButton#dashboardButton {
                padding: 10px;
                font-size: 15px;
                border: 2px solid gray;
                background: None;
                font-weight: bold;            
            }
        """)

    def setup_main_layout(self):
        self.layout.setContentsMargins(0,0,0,0)
        self.layout.setColumnStretch(0, 0)
        self.layout.setColumnStretch(1, 1)

        # Sidebar: Row 0, Col 0, spans 2 rows, span 1 column
        self.layout.addWidget(self.sidebar_frame, 0, 0, 2, 1)

        self.layout.addWidget(self.top_bar, 0, 1)
        self.layout.addWidget(self.main_content, 1, 1)

        # MAGIC LINES: Tell the grid where to push the "empty" space
        self.layout.setColumnStretch(1, 1) # Column 1 (content) takes all extra width
        self.layout.setRowStretch(1, 1)    # Row 1 (bottom) takes all extra height


        self.sidebar_frame.setMinimumWidth(180)
        self.sidebar_frame.setMaximumWidth(250)

        self.setLayout(self.layout)
    
    def setup_sidebar(self):
        self.sidebar_frame.setObjectName('sideBarFrame')
        title_frame = QFrame()
        title_frame.setObjectName('titleFrame')
        title_frame_layout = QVBoxLayout(title_frame)
        self.title_label = QLabel('ScreenStats')
        self.title_label.setObjectName('mainHeader')
        sidebar_DashboardButton = QPushButton('Dashboard')
        sidebar_DashboardButton.setObjectName('dashboardButton')
        sidebar_DashboardButton.setCursor(Qt.PointingHandCursor)
        title_frame_layout.addWidget(self.title_label)
        self.sidebar_layout.addWidget(title_frame)
        self.sidebar_layout.addWidget(sidebar_DashboardButton)

        self.sidebar_layout.addStretch() #throws everyhing to the top
        self.sidebar_layout.setSpacing(15)
        self.sidebar_frame.setStyleSheet("background-color: #333; color: white;")
    
    def setup_top_bar(self):
        self.top_bar.setObjectName('topBar')
        self.search_bar.setPlaceholderText('Search movies & series...')
        self.top_bar_layout.addWidget(self.search_bar)
        self.top_bar.setFixedHeight(60)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    screenstats = ScreenStats()
    screenstats.showFullScreen()
    app.exec()