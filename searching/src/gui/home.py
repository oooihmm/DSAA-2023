import os
import random
import string

from .sorting import SortingPage 
from .view import SortingVisualization

from PyQt5.QtWidgets import QMainWindow, QPushButton, QFileDialog, QVBoxLayout, QWidget, QStackedWidget

class FolderSelectApp(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("파일 정렬 매니저 프로젝트")
        self.resize(300,300)
        self.folder_selected = None

        # Create StackedWidget
        self.stacked_widget = QStackedWidget()
        self.setCentralWidget(self.stacked_widget)

        # Page 1: Folder Selection Page
        self.folder_select_page = QWidget()
        self.init_folder_select_page()
        self.stacked_widget.addWidget(self.folder_select_page)

        # Page 2: Sorting Page
        self.sorting_page = SortingPage(None, self.stacked_widget) 
        self.stacked_widget.addWidget(self.sorting_page)

        # Set initial page to Folder Selection Page
        self.stacked_widget.setCurrentWidget(self.folder_select_page)

    def init_folder_select_page(self):
        select_folder_button = QPushButton("폴더 선택", self)
        select_folder_button.clicked.connect(self.select_folder)

        create_files_button = QPushButton("파일 생성하기", self)
        create_files_button.clicked.connect(self.create_random_files)

        layout = QVBoxLayout()
        layout.addWidget(select_folder_button)
        layout.addWidget(create_files_button)

        self.folder_select_page.setLayout(layout)

    def create_sorting_page(self):
        self.sorting_page = SortingPage(self.folder_selected, self.stacked_widget)
        self.stacked_widget.addWidget(self.sorting_page)
        self.stacked_widget.setCurrentWidget(self.sorting_page)

    def create_random_files(self):
        generated_files_dir = "/Users/choijinseon/workspace/DSAA-2023/searching/generated_files"
        os.makedirs(generated_files_dir, exist_ok=True)

        # 임의의 파일을 100개 생성하여 generated_files 폴더에 저장
        for _ in range(100):
            file_name = ''.join(random.choices(string.ascii_lowercase, k=8)) + '.txt'
            with open(os.path.join(generated_files_dir, file_name), 'w') as file:
                file.write("This is a random file.")
        
        self.folder_selected = generated_files_dir
        print(f"../generated_files 폴더에 100개의 파일을 생성했습니다.")
        print(f"선택된 폴더: {self.folder_selected}")
        self.create_sorting_page()

    def select_folder(self):
        new_folder_selected = QFileDialog.getExistingDirectory(self, "폴더 선택")
        if new_folder_selected:
            self.folder_selected = new_folder_selected
            print(f"선택된 폴더: {self.folder_selected}")
            self.create_sorting_page()

    def closeEvent(self, event):
        generated_files_dir = "/Users/choijinseon/workspace/DSAA-2023/searching/generated_files"
        if os.path.exists(generated_files_dir):
            for filename in os.listdir(generated_files_dir):
                file_path = os.path.join(generated_files_dir, filename)
                os.remove(file_path)
            os.rmdir(generated_files_dir)
            print("폴더가 삭제되었습니다.")
        
        super().closeEvent(event)