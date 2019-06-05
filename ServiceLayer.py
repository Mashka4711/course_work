from DbHelper import DbHelper
from ActiveRecordDoctor import ActiveRecordDoctor
from ActiveRecordPatientCard import ActiveRecordPatientCard


class Service():
    def __init__(self):
        self.db_helper = DbHelper()
        self.doctors_list = []
        self.patients_list = []

    def get_doctors_list(self):
        mas = []
        for i in self.db_helper.get_doctors_ids():
            ar_doc = ActiveRecordDoctor(i, "", "", 0)
            mas.append(ar_doc.form_title_string())
        return mas

    def get_patients_list(self):
        mas = []
        for i in self.db_helper.get_patients_ids():
            ar_doc = ActiveRecordPatientCard(i, "", "")
            mas.append(ar_doc.form_title_string())
        return mas

    def get_doctors_count(self):
        ar_doc = ActiveRecordDoctor(0, '', '', 0)
        for i in self.db_helper.get_doctors_ids():
            ar_doc = ActiveRecordDoctor(i, "", "", 0)
            self.doctors_list.append(ar_doc)
        return self.doctors_list

    def get_patients_count(self):
        ar_doc = ActiveRecordPatientCard(0, '', '')
        for i in self.db_helper.get_patients_ids():
            ar_doc = ActiveRecordPatientCard(i, "", "")
            self.patients_list.append(ar_doc)
        return self.patients_list

    def get_doctor_object(self, q):
        line = q.currentText().split(' ')
        id = line[0]
        current_doctor = ActiveRecordDoctor(0, '', '', 0)
        qq = self.get_doctors_count()
        for i in qq:
            if int(id) == ActiveRecordDoctor.get_id(i):
                current_doctor = i
        return current_doctor

    def get_patient_object(self, q):
        line = q.currentText().split(' ')
        id = line[0]
        current_patient = ActiveRecordPatientCard(0, '', '')
        qq = self.get_patients_count()
        for i in qq:
            if int(id) == ActiveRecordPatientCard.get_id(i):
                current_patient = i
                # current_patient
        return current_patient.form_title_end()

    def save_card(self, card_number, name, surname):
        new_card = ActiveRecordPatientCard(card_number, name, surname)
        new_card.insert_record()