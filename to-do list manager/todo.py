import sys
from PyQt6.QtWidgets import QApplication, QWidget, QPushButton, QVBoxLayout, QLabel, QMessageBox, QTableWidget, QTableWidgetItem
from PyQt6.QtGui import QFont


version = str(3.1)

class lobbyMenu(QWidget):
    def __init__(self):
        super().__init__()
        self.init_ui()

    def init_ui(self):
        self.setWindowTitle('To-Do List Menu V' + version)
        self.setFixedSize(500, 100)

        font = QFont('Arial', 10)
        labelFont = QFont('Arial', 8)

        self.layout = QVBoxLayout()

        # credit label
        self.label1 = QLabel('Coded by Ayrik Nabirahni, July 29 2024', self)
        self.label1.setFont(labelFont)

        # add task
        self.addTaskButton = QPushButton('Add Task', self)
        self.addTaskButton.setFont(font)

        # remove task
        self.removeTaskButton = QPushButton('Reset Tasks', self)
        self.removeTaskButton.setFont(font)

        self.layout.addWidget(self.label1)
        self.layout.addWidget(self.addTaskButton)
        self.layout.addWidget(self.removeTaskButton)

        self.setLayout(self.layout)

        self.addTaskButton.clicked.connect(self.on_add_click)
        self.removeTaskButton.clicked.connect(self.on_remove_click)


    def on_add_click(self): # opens window and parses table data from savedTasks.txt

        with open('savedTasks.txt', 'r') as rawInput:
            data_list = rawInput.readlines()
        filtered_list = [item.strip() for item in data_list]


        def data_parser(): # function parses savedTasks.txt and fills in cells
            x = 0  # column
            y = 0  # row
            z = 0  # current line in filtered list


            while z != 12:
                if z == 12:
                    return None
                if y >= 6:
                    x += 1
                    y = 0
                active_cell = addTask.tableWidget.item(y, x)

                if filtered_list[z] is None or filtered_list[z] == '':
                    print('Empty String')
                    data = 'Empty'
                else:
                    data = filtered_list[z]
                if active_cell is None:
                    # Create a new cell if it doesn't exist
                    new_item = QTableWidgetItem(data)
                    addTask.tableWidget.setItem(y, x, new_item)
                else:
                    active_cell.setText(data)
                z += 1
                y += 1
            return None

        data_parser()
        addTask.show()

    def on_remove_click(self):
        self.resetComplete = QMessageBox()
        self.resetComplete.setWindowTitle('Tasks Reset')
        self.resetComplete.resize(150, 150)
        self.resetComplete.setText('Tasks Reset!')
        self.resetComplete.show()
        with open('savedTasks.txt', 'w') as input:
            for x in range(12):
                input.write('Empty' + '\n')
        print('Tasks Reset!')

class addTask(QWidget):
    def __init__(self):
        super().__init__()
        self.addTaskWidget()


    def addTaskWidget(self):
        self.setWindowTitle('Task Menu')
        self.setFixedSize(240, 260)
        self.layout = QVBoxLayout()

        self.tableWidget = QTableWidget(6, 2)
        self.saveButton = QPushButton('Save', self)

        self.layout.addWidget(self.tableWidget)
        self.layout.addWidget(self.saveButton)

        self.setLayout(self.layout)

        self.saveButton.clicked.connect(self.saveTasks)


    def saveTasks(self): # function reads all cells and writes to SavedTasks.txt
        column = 0
        with open('SavedTasks.txt', 'w') as output:

            def sweepSave(column):
                for y in range(6):
                    item = (self.tableWidget.item(y, column))
                    if item is None:
                        print('none!')
                        text = ''
                    else:
                        text = item.text()
                    print(text)
                    output.write(text + '\n')

            for x in range(2):
                if x == 1:
                    column += 1
                sweepSave(column)

        print('Tasks Saved Successfully!')
        self.saveComplete = QMessageBox()
        self.saveComplete.resize(150, 150)
        self.saveComplete.setWindowTitle('Save Complete!')
        self.saveComplete.setText('List Saved')
        self.saveComplete.show()
        addTask.close()



app = QApplication([])
window = lobbyMenu()
addTask = addTask()

print('Program Version ' + version)
window.show()
app.exec()
