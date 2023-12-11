from PyQt5.QtWidgets import (
    QMainWindow,
    QPushButton,
    QLabel,
    QVBoxLayout,
    QHBoxLayout,
    QMessageBox,
    QWidget,
    QFileDialog,
    QErrorMessage,
)
from PyQt5.QtGui import QPixmap
from PyQt5.QtCore import Qt
from .linked_list import LinkedList
import os


class ImageSlideshow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.image_list = LinkedList()
        self.current_image_node = None

        self.initUI()

    def initUI(self):
        self.setWindowTitle("양방향 링크 리스트 슬라이드쇼")
        self.resize(300, 100)

        # 이미지 레이블 설정
        self.imageLabel = QLabel(self)
        self.pixmap = QPixmap()
        self.imageLabel.setPixmap(self.pixmap)
        self.imageLabel.setFixedSize(500, 500)
        self.imageLabel.setAlignment(Qt.AlignCenter)

        # 버튼 설정
        self.loadButton = QPushButton("새로운 이미지 불러오기", self)
        self.loadButton.clicked.connect(self.loadImage)

        self.loadFolderButton = QPushButton("새로운 폴더 불러오기", self)
        self.loadFolderButton.clicked.connect(self.loadFolder)

        self.addButton = QPushButton("현재 슬라이드에 이미지 추가하기", self)
        self.addButton.clicked.connect(self.addImage)

        self.addFolderButton = QPushButton("현재 슬라이드에 폴더 추가하기", self)
        self.addFolderButton.clicked.connect(self.addFolder)

        self.prevButton = QPushButton("<", self)  # '<' 버튼
        self.prevButton.clicked.connect(self.showPreviousImage)

        self.nextButton = QPushButton(">", self)  # '>' 버튼
        self.nextButton.clicked.connect(self.showNextImage)

        self.deleteButton = QPushButton("현재 이미지 삭제", self)
        self.deleteButton.clicked.connect(self.deleteImage)

        # 이미지와 '<', '>' 버튼을 위한 레이아웃 설정
        hbox = QHBoxLayout()
        hbox.addWidget(self.prevButton)
        hbox.addWidget(self.imageLabel)
        hbox.addWidget(self.nextButton)

        # 주 레이아웃 설정
        vbox = QVBoxLayout()
        vbox.addLayout(hbox)
        vbox.addWidget(self.loadButton)
        vbox.addWidget(self.loadFolderButton)
        vbox.addWidget(self.addButton)
        vbox.addWidget(self.addFolderButton)
        vbox.addWidget(self.deleteButton)

        centralWidget = QWidget(self)
        centralWidget.setLayout(vbox)
        self.setCentralWidget(centralWidget)

    def loadImage(self):
        # LinkedList 초기화
        self.image_list = LinkedList()
        self.current_image_node = None

        fname, _ = QFileDialog.getOpenFileName(
            self, "Open Image", ".", "Image Files (*.png *.jpg *.jpeg *.bmp)"
        )
        if fname:
            image_name = os.path.basename(fname)
            self.image_list.append(image_name, fname)

            # LinkedList의 마지막 노드 (새로 추가된 노드)를 current_image_node로 설정
            self.current_image_node = self.image_list.tail

            self.displayImage(fname)

    def loadFolder(self):
        # LinkedList 초기화
        self.image_list = LinkedList()
        self.current_image_node = None

        dir_name = QFileDialog.getExistingDirectory(
            self, "Open Directory", ".", QFileDialog.ShowDirsOnly
        )
        if dir_name:
            first_image_node = None

            for root, dirs, files in os.walk(dir_name):
                for file in files:
                    if file.lower().endswith((".png", ".jpg", ".jpeg", ".bmp")):
                        full_path = os.path.join(root, file)
                        self.image_list.append(file, full_path)

                        # 폴더의 첫 번째 이미지 노드를 기억
                        if not first_image_node:
                            first_image_node = self.image_list.tail

            # 폴더의 첫 번째 이미지 노드를 current_image_node로 설정
            self.current_image_node = first_image_node
            if self.current_image_node:
                self.displayImage(self.current_image_node.image_path)


    def addImage(self):
        fname, _ = QFileDialog.getOpenFileName(
            self, "Open Image", ".", "Image Files (*.png *.jpg *.jpeg *.bmp)"
        )
        if fname:
            image_name = os.path.basename(fname)
            self.image_list.append(image_name, fname)

            # LinkedList의 마지막 노드 (새로 추가된 노드)를 current_image_node로 설정
            self.current_image_node = self.image_list.tail

            self.displayImage(fname)

    def addFolder(self):
        dir_name = QFileDialog.getExistingDirectory(
            self, "Open Directory", ".", QFileDialog.ShowDirsOnly
        )
        if dir_name:
            first_image_node = None

            for root, dirs, files in os.walk(dir_name):
                for file in files:
                    if file.lower().endswith((".png", ".jpg", ".jpeg", ".bmp")):
                        full_path = os.path.join(root, file)
                        self.image_list.append(file, full_path)

                        # 폴더의 첫 번째 이미지 노드를 기억
                        if not first_image_node:
                            first_image_node = self.image_list.tail

            # 폴더의 첫 번째 이미지 노드를 current_image_node로 설정
            self.current_image_node = first_image_node
            if self.current_image_node:
                self.displayImage(self.current_image_node.image_path)

    def displayImage(self, image_path):
        self.pixmap = QPixmap(image_path)
        # QLabel의 크기로 이미지 크기 조정
        scaled_pixmap = self.pixmap.scaled(
            self.imageLabel.width(), self.imageLabel.height(), Qt.KeepAspectRatio
        )
        self.imageLabel.setPixmap(scaled_pixmap)

    def showNextImage(self):
        if self.current_image_node:
            if self.current_image_node.next_node:
                self.current_image_node = self.current_image_node.next_node
            else:  # 슬라이드쇼의 끝에 도달한 경우
                self.current_image_node = self.image_list.head  # 첫 번째 이미지로 돌아갑니다.
            self.displayImage(self.current_image_node.image_path)

    def showPreviousImage(self):
        if self.current_image_node:
            if self.current_image_node.prev_node:
                self.current_image_node = self.current_image_node.prev_node
            else:  # 슬라이드쇼의 시작에 도달한 경우
                self.current_image_node = self.image_list.tail  # 마지막 이미지로 이동합니다.
            self.displayImage(self.current_image_node.image_path)

    def deleteImage(self):
        if not self.current_image_node:
            error_dialog = QErrorMessage(self)
            error_dialog.showMessage("삭제할 이미지가 없습니다.")
            return

        reply = QMessageBox.question(
            self,
            "이미지 삭제",
            f"정말로 {self.current_image_node.image_name}을 삭제하시겠습니까?",
            QMessageBox.Yes | QMessageBox.No,
            QMessageBox.No,
        )

        if reply == QMessageBox.Yes:
            prev_node = self.current_image_node.prev_node
            next_node = self.current_image_node.next_node

            # 링크드리스트에서 해당 노드 삭제
            self.image_list.remove(self.current_image_node.image_name)

            # 삭제한 노드의 앞 노드와 뒤 노드 연결
            if prev_node:
                prev_node.next_node = next_node
            if next_node:
                next_node.prev_node = prev_node

            # 화면에 표시되는 이미지 변경
            self.current_image_node = prev_node if prev_node else next_node

            if self.current_image_node:
                self.displayImage(self.current_image_node.image_path)
            else:  # 모든 이미지가 삭제된 경우
                self.imageLabel.clear()
