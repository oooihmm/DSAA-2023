import sys
from PyQt5.QtWidgets import (
    QApplication,
    QMainWindow,
    QWidget,
    QVBoxLayout,
    QHBoxLayout,
    QPushButton,
    QLineEdit,
    QLabel,
    QTextEdit,
    QMessageBox,  # 팝업 메시지를 사용하기 위해 추가
)
from .checker import BracketChecker  # 괄호 검사 알고리즘 모듈을 import


class BracketCheckerApp(QMainWindow):
    def __init__(self):
        super().__init__()

        self.initUI()

    def initUI(self):
        self.setWindowTitle("괄호 검사기")
        self.setGeometry(100, 100, 400, 300)

        self.central_widget = QWidget(self)
        self.setCentralWidget(self.central_widget)

        self.layout = QVBoxLayout()

        self.label = QLabel("수식을 입력해주세요:")
        self.layout.addWidget(self.label)

        self.input_line_edit = QLineEdit()
        self.input_line_edit.setPlaceholderText("숫자, 연산자, 괄호만 입력해주세요")
        self.layout.addWidget(self.input_line_edit)

        self.check_button = QPushButton("검사하기")
        self.check_button.clicked.connect(self.check_expression)
        self.layout.addWidget(self.check_button)

        self.result_label = QLabel("")
        self.layout.addWidget(self.result_label)

        self.stack_status_text_edit = QTextEdit()
        self.layout.addWidget(self.stack_status_text_edit)

        self.central_widget.setLayout(self.layout)

    def check_expression(self):
        expression = self.input_line_edit.text()

        if not expression:
            self.result_label.setText("Empty expression provided.")
            self.stack_status_text_edit.setText("")
            return

        # 입력값에서 숫자, 연산자, 괄호 이외의 문자를 찾습니다.
        invalid_chars = [
            char for char in expression if char not in "0123456789+-*/()[]{} "
        ]

        if invalid_chars:
            QMessageBox.critical(
                self,
                "오류!",
                "숫자, 연산자, 괄호만 사용해서 수식을 입력해주세요.",
                QMessageBox.Ok,
            )
            self.input_line_edit.setText("")
            self.result_label.setText("")
            self.stack_status_text_edit.setText("")
            return

        checker = BracketChecker()
        result, stack_status = checker.check_brackets(expression)

        if result:
            self.result_label.setText("Valid expression.")
        else:
            self.result_label.setText("Invalid expression.")

        self.stack_status_text_edit.setPlainText("\n".join(stack_status))
