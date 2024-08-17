from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel, QLineEdit, QPushButton, QTextEdit, QVBoxLayout, QWidget, QSizePolicy, QMessageBox
from PyQt5.QtGui import QFont, QIntValidator

def input_grades(scores):
    best_score = max(scores)
    grades = []
    for score in scores:
        if score >= best_score - 10:
            grades.append('A')
        elif score >= best_score - 20:
            grades.append('B')
        elif score >= best_score - 30:
            grades.append('C')
        elif score >= best_score - 40:
            grades.append('D')
        else:
            grades.append('F')
    return grades

class StudentGrade(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Student Grade")
        self.setGeometry(100, 100, 600, 600)  
        self.init_ui()

    def init_ui(self):
        font = QFont()
        font.setPointSize(10)

        self.student_count_label = QLabel("Total number of students:")
        self.student_count_label.setFont(font)
        self.student_count_entry = QLineEdit()
        self.student_count_entry.setFont(font)
        self.student_count_entry.setValidator(QIntValidator(1, 100, self))  

        self.scores_label = QLabel("Enter scores separated by space:")
        self.scores_label.setFont(font)
        self.scores_entry = QLineEdit()
        self.scores_entry.setFont(font)

        self.calculate_button = QPushButton("Calculate Grades")
        self.calculate_button.setFont(font)
        self.calculate_button.clicked.connect(self.calculate_grades)

        self.calculate_stats_button = QPushButton("Calculate Stats")
        self.calculate_stats_button.setFont(font)
        self.calculate_stats_button.clicked.connect(self.calculate_stats)

        self.reset_button = QPushButton("Reset")
        self.reset_button.setFont(font)
        self.reset_button.clicked.connect(self.reset_fields)

        self.result_text = QTextEdit()
        self.result_text.setFont(font)
        self.result_text.setReadOnly(True)
        self.result_text.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)

        layout = QVBoxLayout()
        layout.addWidget(self.student_count_label)
        layout.addWidget(self.student_count_entry)
        layout.addWidget(self.scores_label)
        layout.addWidget(self.scores_entry)
        layout.addWidget(self.calculate_button)
        layout.addWidget(self.calculate_stats_button)
        layout.addWidget(self.reset_button)
        layout.addWidget(self.result_text)

        container = QWidget()
        container.setLayout(layout)
        self.setCentralWidget(container)

    def calculate_grades(self):
        student_count_text = self.student_count_entry.text()
        scores_text = self.scores_entry.text()

        if not student_count_text or not scores_text:
            self.show_message("Error", "Please fill out all fields.")
            return

        try:
            student_count = int(student_count_text)
            scores = list(map(int, scores_text.split()))

            if len(scores) != student_count:
                self.display_result("Error: The number of scores doesn't match the number of students.")
                return

            grades = input_grades(scores)
            result = "\n".join([f"Student {i + 1} score is {scores[i]} and grade is {grades[i]}" for i in range(student_count)])
            self.display_result(result)

        except ValueError:
            self.show_message("Error", "Please enter valid numbers for both student count and scores.")

    def calculate_stats(self):
        scores_text = self.scores_entry.text()

        if not scores_text:
            self.show_message("Error", "Please enter scores.")
            return

        try:
            scores = list(map(int, scores_text.split()))
            average_score = sum(scores) / len(scores)
            highest_score = max(scores)
            lowest_score = min(scores)

            stats = (f"\nAverage Score: {average_score:.2f}"
                     f"\nHighest Score: {highest_score}"
                     f"\nLowest Score: {lowest_score}")

            self.result_text.append(stats)

        except ValueError:
            self.show_message("Error", "Please enter valid numbers for scores.")

    def display_result(self, result):
        self.result_text.setPlainText(result)

    def reset_fields(self):
        self.student_count_entry.clear()
        self.scores_entry.clear()
        self.result_text.clear()

    def show_message(self, title, message):
        QMessageBox.critical(self, title, message)

