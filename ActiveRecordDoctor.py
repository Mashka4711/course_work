import DbHelper
from Doctor import Doctor
from Doctor import Oculist
from Doctor import Traumatologist
from Doctor import Dentist


class ActiveRecordDoctor():
    def __init__(self, x_doctor_id, x_name, x_surname, x_prof):
        self.db_helper = DbHelper.DbHelper()
        self.doctor_id = x_doctor_id
        self.name = x_name
        self.surname = x_surname
        self.prof = x_prof
        self.spec = Doctor()
        # self.insert_record()
        self.get_record(x_doctor_id)

    # def __del__(self):
    #     self.delete_record()
    #     self.get_record()

    def insert_record(self):
        self.db_helper.insert_doctor(self.doctor_id, self.name, self.surname, self.prof)

    def get_record(self, x_id):
        notes = self.db_helper.get_doctor(x_id)
        for note in notes:
            self.doctor_id = note['id_doctor']
            self.name = note['name']
            self.surname = note['surname']
            self.prof = note['specialization']
            if self.prof == 1:
                self.spec = Oculist()
            if self.prof == 2:
                self.spec = Traumatologist()
            if self.prof == 3:
                self.spec = Dentist()
        # print(self.name, self.surname, self.prof)

    def update_record(self, x_id):
        self.db_helper.update_doctor(self.doctor_id, self.name, self.surname, self.prof)

    def delete_record(self):
        self.db_helper.delete_doctor(self.doctor_id)

    def form_title_string(self):
        return str(self.doctor_id) + " " + self.name + " " + self.surname + " (" + str(self.prof) + ")"

    def special_print(self):
        print(str(self.doctor_id) + " " + self.name + " " + self.surname + " (" + str(self.prof) + ")")

    def get_id(self):
        return self.doctor_id