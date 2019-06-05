from PyQt4 import QtCore, QtGui
from Common_design import Common
from ActiveRecordPatientCard import ActiveRecordPatientCard
from ServiceLayer import Service


class AddPatientCard(Common):
    def __init__(self, parent=None):
        super(AddPatientCard, self).__init__(parent)
        self.setWindowFlags(QtCore.Qt.Dialog | QtCore.Qt.WindowSystemMenuHint)
        self.setWindowModality(QtCore.Qt.WindowModal)
        self.setFixedSize(500, 500)

        self.rw_name = QtGui.QLineEdit()
        self.rw_surname = QtGui.QLineEdit()
        self.rw_card_number = QtGui.QLineEdit()

        self.save_patient_card = QtGui.QPushButton(' Сохранить ')
        self.save_patient_card.clicked.connect(self.save_new_patient_card)

        self.filling()

        # Содержимое окна

    def filling(self):
        lab_name = QtGui.QLabel(' Имя:   ')
        lab_name.setObjectName('lab_name')
        lab_surname = QtGui.QLabel(' Фамилия:  ')
        lab_surname.setObjectName('lab_surname')
        lab_card_number = QtGui.QLabel(' * Номер карты пациента: ')
        lab_card_number.setObjectName('lab_card_number')
        lab_note = QtGui.QLabel(' Примечание *\n\n Введите 6 цифр: ****** ')
        lab_note.setObjectName('lab_note')
        lab_title = QtGui.QLabel(' Заполните следующие поля: ')
        lab_title.setObjectName('lab_title')

        self.save_patient_card.setObjectName('save_dossier')

        frame = QtGui.QFrame()
        frame.setMaximumSize(480, 560)
        frame.setFrameShape(6)

        frame_in = QtGui.QFrame()
        frame_in_down = QtGui.QFrame()
        frame_in.setMaximumSize(460, 500)
        frame_in_down.setMaximumSize(460, 200)

        grid = QtGui.QGridLayout()
        grid_down = QtGui.QGridLayout()
        grid.addWidget(lab_name, 0, 0)
        grid.addWidget(self.rw_name, 0, 1)
        grid.addWidget(lab_surname, 1, 0)
        grid.addWidget(self.rw_surname, 1, 1)
        grid.addWidget(lab_card_number, 2, 0)
        grid.addWidget(self.rw_card_number, 2, 1)

        grid_down.addWidget(lab_note, 0, 0, 1, 3)
        grid_down.addWidget(QtGui.QLabel(''), 1, 0)
        grid_down.addWidget(QtGui.QLabel(''), 2, 0)
        grid_down.addWidget(self.save_patient_card, 3, 1, 1, 1)

        frame_in.setLayout(grid)
        frame_in_down.setLayout(grid_down)

        separator = QtGui.QFrame()
        separator.setFrameStyle(QtGui.QFrame.HLine | QtGui.QFrame.Raised)
        separator.setMaximumSize(460, 3)

        vertical = QtGui.QVBoxLayout()
        vertical.addStretch(1)
        vertical.addWidget(lab_title)
        vertical.addStretch(1)
        vertical.addWidget(frame_in)
        vertical.addWidget(separator)
        vertical.addWidget(frame_in_down)
        vertical.addStretch(2)
        frame.setLayout(vertical)

        layout_all = QtGui.QVBoxLayout()
        layout_all.addWidget(frame)

        self.setLayout(layout_all)
        self.setStyleSheet('QLabel#lab_name, #lab_surname, #lab_card_number, #lab_title, #lab_note {color: white;'
                           'font-size: 20px; font-family: Proggy}'
                           'QLineEdit {font-size: 20px}'
                           'QPushButton#save_dossier {font-size: 20px; font-family: Proggy; border: 2px;'
                           'border-radius: 6px; background-color: white; min-height: 30px;}'
                           'QPushButton#save_dossier:hover {background-color: #cafcca}')

        # Сохранение новой карты пациента

    # def save_new_patient_card(self):
    #     self.new_patient_card = ActiveRecordPatientCard(self.rw_card_number.text(), self.rw_name.text(), self.rw_surname.text())
    #     self.new_patient_card.insert_record()

    def save_new_patient_card(self):
        card = Service()
        card.save_card(self.rw_card_number.text(), self.rw_name.text(), self.rw_surname.text())


if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    window_main = AddPatientCard()
    window_main.show()
    sys.exit(app.exec_())
