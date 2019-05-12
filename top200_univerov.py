from PyQt5.QtWidgets import QApplication, QMainWindow, QGridLayout, QWidget, QTableWidget, QTableWidgetItem
from PyQt5.QtCore import QSize, Qt
import pandas as pd
import xlrd


# Наследуемся от QMainWindow
class MainWindow(QMainWindow):
    # Переопределяем конструктор класса
    def __init__(self):
        # Обязательно нужно вызвать метод супер класса
        QMainWindow.__init__(self)

        self.setMinimumSize(QSize(500, 400))  # Устанавливаем размеры
        self.setWindowTitle("Консолідований рейтинг вищів України 2018")  # Устанавливаем заголовок окна
        central_widget = QWidget(self)  # Создаём центральный виджет
        self.setCentralWidget(central_widget)  # Устанавливаем центральный виджет

        grid_layout = QGridLayout()  # Создаём QGridLayout
        central_widget.setLayout(grid_layout)  # Устанавливаем данное размещение в центральный виджет

        table = QTableWidget(self)  # Создаём таблицу
        table.setColumnCount(6)  # Устанавливаем колонки
        table.setRowCount(273)  # и строки в таблице

        # Устанавливаем заголовки таблицы
        table.setHorizontalHeaderLabels(["Назва навчального закладу", "Місце у загальному рейтингу", "ТОП 200 України", "Scopus", "Бал ЗНО на контракт", "Підсумковий бал"])

        rb = xlrd.open_workbook('топ университетов украины.xlsx')
        sheet = rb.sheet_by_index(0)

        val = sheet.col_values(0)
        for i, entry in enumerate(val):
            table.setRowCount(i + 1)
            item = QTableWidgetItem(0)
            item.setText(str(entry))
            table.setItem(i, 0, item)

        val2 = sheet.col_values(1)
        for q, entry in enumerate(val2):
            table.setRowCount(i + 1)
            item = QTableWidgetItem(0)
            item.setText(str(entry))
            table.setItem(q, 1, item)

        val3 = sheet.col_values(2)
        for w, entry in enumerate(val3):
            table.setRowCount(i + 1)
            item = QTableWidgetItem(0)
            item.setText(str(entry))
            table.setItem(w, 2, item)

        val4 = sheet.col_values(3)
        for a, entry in enumerate(val4):
            table.setRowCount(i + 1)
            item = QTableWidgetItem(0)
            item.setText(str(entry))
            table.setItem(a, 3, item)

        val5 = sheet.col_values(4)
        for s, entry in enumerate(val5):
            table.setRowCount(i + 1)
            item = QTableWidgetItem(0)
            item.setText(str(entry))
            table.setItem(s, 4, item)

        val6 = sheet.col_values(5)
        for v, entry in enumerate(val6):
            table.setRowCount(i + 1)
            item = QTableWidgetItem(0)
            item.setText(str(entry))
            table.setItem(v, 5, item)

        table.resizeColumnsToContents()
        grid_layout.addWidget(table, 0, 0)


if __name__ == "__main__":
    import sys

    app = QApplication(sys.argv)
    mw = MainWindow()
    mw.show()
    sys.exit(app.exec())