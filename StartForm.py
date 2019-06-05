from PyQt4 import QtCore, QtGui
from Common_design import Common
from DbHelper import DbHelper
from ActiveRecordDoctor import ActiveRecordDoctor
from PatientChoiceForm import PatientChoice
from ServiceLayer import Service


class MainWind(Common):
    def __init__(self, parent=None):
        super(MainWind, self).__init__(parent)
        self.setWindowFlags(QtCore.Qt.Dialog | QtCore.Qt.WindowSystemMenuHint)
        self.setWindowModality(QtCore.Qt.WindowModal)
        self.setFixedSize(800, 500)

        self.db_helper = DbHelper()

        self.doctors_list = []
        self.code = str

        self.current_doctor = ActiveRecordDoctor(0, 0, " ", " ")

        self.but_enter = QtGui.QPushButton('Выбрать', self)
        self.rw_login = QtGui.QLineEdit()
        self.rw_pass = QtGui.QLineEdit()
        self.rw_doctor_name = QtGui.QComboBox()
        self.layout = QtGui.QVBoxLayout()
        self.frame_full = QtGui.QFrame()
        self.fr_empty = QtGui.QFrame()
        self.layout_2 = QtGui.QVBoxLayout()
        self.layout_3 = QtGui.QHBoxLayout()
        self.grid_start = QtGui.QGridLayout()
        self.frame_start = QtGui.QFrame()
        self.frame_start_empty = QtGui.QFrame()
        self.vlay_start = QtGui.QVBoxLayout()
        self.hlay_start = QtGui.QHBoxLayout()
        self.label = QtGui.QLabel('Криминалистическая лаборатория')

        self.filling()
        # self.get_spec_code()


    def filling(self):

        lab_account = QtGui.QLabel('  Выберите учетную запись:  ')
        lab_account.setObjectName('lab_login')

        grid = QtGui.QGridLayout()
        grid.setSpacing(10)

        grid.addWidget(lab_account, 1, 0)
        grid.addWidget(self.rw_doctor_name, 2, 0)
        grid.addWidget((QtGui.QLabel("")), 3, 0)
        grid.addWidget(self.but_enter, 4, 0)

        self.frame_full.setFrameShape(6)
        self.frame_full.setLayout(grid)
        self.frame_full.setMaximumSize(450, 250)
        self.fr_empty.setMaximumSize(450, 250)
        self.layout_2.addWidget(self.frame_full)
        self.layout_2.setStretch(1, 3)

        self.layout_3.addLayout(self.layout_2)

        self.setLayout(self.layout_3)
        self.setStyleSheet('QLabel {color: white; font-size: 20px; font-family: Proggy}'
                          'QLineEdit {font-size: 20px}'
                          'QPushButton {font-size: 20px; font-family: Proggy; border: 2px;'
                          'border-radius: 6px; background-color: white; min-height: 30px;}'
                          'QPushButton:hover {background-color: #cafcca}')

        # self.get_doctors_list()
        # self.but_enter.clicked.connect(lambda: self.open_patient_choice(self.get_doctor_object()))
        self.but_enter.clicked.connect(lambda: self.open_patient_choice(self.transfer_param()))
        self.filling_combobox()
        # self.obu()


        # for i in self.doctors_list:
        #     i.special_print()
        #     i.spec.assign_procedure()

    # Переписываю в сервис
    # def get_doctor_object(self):
    #     line = self.rw_doctor_name.currentText().split(' ')
    #     id = line[0]
    #     for i in self.doctors_list:
    #         if int(id) == ActiveRecordDoctor.get_id(i):
    #             self.current_doctor = i
    #     return self.current_doctor

    # def get_spec_code(self):
    #     line = self.rw_doctor_name.currentText().split(' ')
    #     spec_code = line[2]
    #     self.code = spec_code

    def open_patient_choice(self, a):
        self.win = PatientChoice(a)
        self.win.show()

    def filling_combobox(self):
        doc = Service()
        count = len(doc.get_doctors_count())
        for i in range(count):
            self.rw_doctor_name.addItem(doc.get_doctors_list()[i])

    def transfer_param(self):
        doc = Service()
        return doc.get_doctor_object(self.rw_doctor_name)

    # Переписываю в сервис
    # def get_doctors_list(self):
    #     for i in self.db_helper.get_doctors_ids():
    #         ar_doc = ActiveRecordDoctor(i, "", "", 0)
    #         self.doctors_list.append(ar_doc)
    #         self.rw_doctor_name.addItem(ar_doc.form_title_string())



if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    window_main = MainWind()
    # window_main.show()
    # main_window_contain(window_main, 2)
    window_main.show()
    sys.exit(app.exec_())
