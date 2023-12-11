from PyQt5.QtWidgets import QWidget, QLabel, QVBoxLayout, QComboBox, QPushButton
from PyQt5.QtGui import QFont
from PyQt5.QtCore import Qt

from .view import SortingVisualization 

class SortingPage(QWidget):
    def __init__(self, folder_selected, stacked_widget):
        super().__init__()
        self.folder_selected = folder_selected
        self.stacked_widget = stacked_widget

        folder_label = QLabel(f"선택된 폴더: {self.folder_selected}", self)
        folder_label.setAlignment(Qt.AlignCenter)

        sort_algorithm_label = QLabel("정렬 방법", self)
        sort_algorithm_label.setFont(QFont("Arial", 20))
        self.sort_algorithm_combo = QComboBox(self)
        self.sort_algorithm_combo.addItems(["버블 정렬", "선택 정렬", "삽입 정렬", "퀵 정렬", "머지 정렬", "전체 선택"])

        sort_criteria_label = QLabel("정렬 기준", self)
        sort_criteria_label.setFont(QFont("Arial", 20))

        self.sort_option_label = QLabel("정렬 옵션", self)
        self.sort_option_combo = QComboBox(self)
        self.sort_option_combo.addItems(["파일 이름", "파일 크기", "파일 생성 날짜"])

        sort_order_label = QLabel("차순 선택", self)
        sort_order_label.setFont(QFont("Arial", 20))
        self.sort_order_combo = QComboBox(self)
        self.sort_order_combo.addItems(["오름차순", "내림차순"])

        next_button = QPushButton("다음으로", self)
        next_button.clicked.connect(self.go_to_visualization)

        layout = QVBoxLayout()
        layout.addWidget(folder_label)

        layout.addWidget(sort_algorithm_label)
        layout.addWidget(self.sort_algorithm_combo)

        layout.addWidget(sort_criteria_label)

        layout.addWidget(self.sort_option_label)
        layout.addWidget(self.sort_option_combo)

        layout.addWidget(sort_order_label)
        layout.addWidget(self.sort_order_combo)

        layout.addWidget(next_button)

        self.setLayout(layout)

    def go_to_visualization(self):
        # 현재 선택된 값 가져오기
        selected_algorithm = self.sort_algorithm_combo.currentText()
        selected_option = self.sort_option_combo.currentText()
        selected_order = self.sort_order_combo.currentText()

        # 이 정보를 가지고 다음 페이지로 넘어가는 함수 호출
        visualization_page = SortingVisualization(
            self.folder_selected, selected_algorithm, selected_option, selected_order
        )
        self.stacked_widget.addWidget(visualization_page)  # 스택 위젯에 추가
        self.stacked_widget.setCurrentWidget(visualization_page)  # 현재 페이지로 설정


