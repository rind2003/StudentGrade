from StudentGrade import *

def main():
    app = QApplication([])
    window = StudentGrade()
    window.show()
    app.exec_()

if __name__ == '__main__':
    main()