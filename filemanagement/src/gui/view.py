import os
import time

from ..bubble import BubbleSort
from ..insertion import InsertionSort
from ..merge import MergeSort
from ..quick import QuickSort
from ..selection import SelectionSort

from PyQt5.QtWidgets import QWidget, QVBoxLayout, QLabel, QScrollArea

class SortingVisualization(QWidget):
    def __init__(self, selected_folder, selected_algorithm, selected_option, selected_order, parent=None):
        super().__init__(parent)

        self.selected_folder = selected_folder
        self.selected_algorithm = selected_algorithm
        self.selected_option = selected_option
        self.selected_order = selected_order

        self.sorted_files = []
        self.steps_info = []

        self.elapsed_time = QLabel(self)
        self.time_complexity = QLabel(self)
        self.result_info_label = QLabel(self)
        self.procedure_info_label = QLabel(self)

        folder_label = QLabel(f"선택된 폴더: {self.selected_folder}", self)
        algorithm_label = QLabel(f"선택된 정렬 알고리즘: {self.selected_algorithm}", self)
        option_label = QLabel(f"선택된 정렬 옵션: {self.selected_option}", self)
        order_label = QLabel(f"선택된 정렬 차순: {self.selected_order}", self)
        result_label = QLabel("\n정렬 결과:", self)
        procedure_label = QLabel("정렬 과정:", self)
        time_label = QLabel(f"걸린 시간:", self)

        layout = QVBoxLayout()
        layout.addWidget(folder_label)
        layout.addWidget(algorithm_label)
        layout.addWidget(option_label)
        layout.addWidget(order_label)
        layout.addWidget(time_label)
        layout.addWidget(self.elapsed_time)
        layout.addWidget(self.time_complexity)
        layout.addWidget(result_label)
        layout.addWidget(self.result_info_label)
        layout.addWidget(procedure_label)
        layout.addWidget(self.procedure_info_label)

        scroll_area = QScrollArea()
        scroll_widget = QWidget()
        scroll_widget.setLayout(layout)

        scroll_area.setWidgetResizable(True)
        scroll_area.setWidget(scroll_widget)

        main_layout = QVBoxLayout()
        main_layout.addWidget(scroll_area)
        self.setLayout(main_layout)

        self.initialize_sorting()

        self.setLayout(layout)
        self.initialize_sorting()  

    def initialize_sorting(self):
        if os.path.isdir(self.selected_folder): 
            algorithm_dict = {"버블 정렬": BubbleSort(), "선택 정렬": SelectionSort(), "삽입 정렬": InsertionSort(), "퀵 정렬": QuickSort(), "머지 정렬": MergeSort(),}
            complexity_dict = {
                "버블 정렬": "시간 복잡도: O(n^2)",
                "선택 정렬": "시간 복잡도: O(n^2)",
                "삽입 정렬": "시간 복잡도: O(n^2)",
                "퀵 정렬": "최악 시간 복잡도: O(n^2), 평균/최선 시간 복잡도: O(n log n)",
                "머지 정렬": "시간 복잡도: O(n log n)"
            }
    
            files = os.listdir(self.selected_folder)  
            algorithm = algorithm_dict[self.selected_algorithm]
            option_dict = {"파일 이름": algorithm.sort_files, "파일 크기": algorithm.sort_sizes, "파일 생성 날짜": algorithm.sort_dates}
            self.time_complexity.setText(complexity_dict[self.selected_algorithm])

            start_time = time.time()
            sorted_files, steps_info = option_dict[self.selected_option](files, self.selected_folder, self.selected_order) 
            end_time = time.time()
            elapsed_time = end_time - start_time
            self.elapsed_time.setText(str(elapsed_time))

            self.sorted_files = sorted_files 
            result_text = self.get_result_text()
            self.result_info_label.setText(result_text)

            self.steps_info = steps_info 
            procedure_text = self.get_procedure_text()
            self.procedure_info_label.setText(procedure_text)
        else:
            print("유효하지 않은 폴더 경로입니다. 다시 확인해주세요.")

    def get_result_text(self):
        result_text = ""
        for step in self.sorted_files:
            file_path = os.path.join(self.selected_folder, step)
            file_name = step
            file_date = os.path.getctime(file_path)
            file_size = os.path.getsize(file_path)

            result_text += f"file_name: {file_name},\n"
            result_text += f"  - Size: {file_size}, Date: {time.ctime(file_date)}\n"
        return result_text
    
    def get_procedure_text(self):
        procedure_text = ""
        for index, step in enumerate(self.steps_info, start=1):
            procedure_text += f"{index}번째 정렬: {step},\n"
        return procedure_text
