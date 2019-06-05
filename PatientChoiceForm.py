from PyQt4 import QtCore, QtGui
from Common_design import Common
from DbHelper import DbHelper
from AddPatientCardForm import AddPatientCard
from ActiveRecordPatientCard import ActiveRecordPatientCard
from ServiceLayer import Service


class PatientChoice(Common):
    def __init__(self, doctor, parent=None):
        super(PatientChoice, self).__init__(parent)
        self.setWindowFlags(QtCore.Qt.Dialog | QtCore.Qt.WindowSystemMenuHint)
        self.setWindowModality(QtCore.Qt.WindowModal)
        self.setFixedSize(800, 500)
        self.cur_doctor = doctor

        self.db_helper = DbHelper()

        self.res = ''

        self.patients_list = []

        self.lab_choice = QtGui.QLabel('Выберите пациента:')
        self.rw_choice = QtGui.QComboBox()
        self.but_assign_procedure = QtGui.QPushButton('Назначить процедуру')
        self.but_new_patient = QtGui.QPushButton('Новый пациент')

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
        self.label = QtGui.QLabel('Медицинская клиника')

        self.filling()
        self.but_new_patient.clicked.connect(self.open_new_patient_form)
        # self.but_assign_procedure.clicked.connect(lambda: self.cur_doctor.spec.assign_procedure(self.get_patient_object()))
        self.but_assign_procedure.clicked.connect(lambda: self.cur_doctor.spec.assign_procedure(self.transfer_param()))

    def filling(self):

        grid = QtGui.QGridLayout()
        grid.setSpacing(10)

        grid.addWidget(self.lab_choice, 1, 0)
        grid.addWidget(self.rw_choice, 2, 0)
        grid.addWidget((QtGui.QLabel("")), 3, 0)
        grid.addWidget(self.but_assign_procedure, 4, 0)
        grid.addWidget(self.but_new_patient, 5, 0)

        self.frame_full.setFrameShape(6)
        self.frame_full.setLayout(grid)
        self.frame_full.setMaximumSize(450, 250)
        self.fr_empty.setMaximumSize(450, 250)
        self.layout_2.addWidget(self.frame_full)
        self.layout_2.setStretch(1, 3)

        self.layout_3.addLayout(self.layout_2)

        self.setLayout(self.layout_3)
        self.setStyleSheet('QLabel {color: black; font-size: 20px; font-family: Proggy}'
                          'QLineEdit {font-size: 20px}'
                          'QPushButton {font-size: 20px; font-family: Proggy; border: 2px;'
                          'border-radius: 6px; background-color: white; min-height: 30px;}'
                          'QPushButton:hover {background-color: #cafcca}')

        # self.get_patients_list()
        self.filling_combobox()

    def open_new_patient_form(self):
        self.win = AddPatientCard()
        self.win.show()

    def filling_combobox(self):
        pat = Service()
        count = len(pat.get_patients_count())
        for i in range(count):
            self.rw_choice.addItem(pat.get_patients_list()[i])

    def transfer_param(self):
        pat = Service()
        return pat.get_patient_object(self.rw_choice)

    # Переписываю в сервис

    # def get_patients_list(self):
    #     # print(self.db_helper.get_doctors_ids())
    #     for i in self.db_helper.get_patients_ids():
    #         ar_patient = ActiveRecordPatientCard(i, "", "")
    #         self.patients_list.append(ar_patient)
    #         self.rw_choice.addItem(ar_patient.form_title_string())

    # Переписываю в сервис

    # def get_patient_object(self):
    #     line = self.rw_choice.currentText().split(' ')
    #     id = line[0]
    #     for i in self.patients_list:
    #         if int(id) == ActiveRecordPatientCard.get_id(i):
    #             self.current_patient = i
    #             self.record = self.current_patient.form_title_end()
    #     return self.record


# if __name__ == "__main__":
#     import sys
#     app = QtGui.QApplication(sys.argv)
#     window = PatientChoice(3)
#     window.show()
#     sys.exit(app.exec_())