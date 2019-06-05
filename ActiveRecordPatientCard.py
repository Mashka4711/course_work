import DbHelper


class ActiveRecordPatientCard():
    def __init__(self, x_card_number, x_name, x_surname):
        self.db_helper = DbHelper.DbHelper()
        self.card_number = x_card_number
        self.name = x_name
        self.surname = x_surname
        # self.insert_record()
        self.get_record(x_card_number)

    # def __del__(self):
    #     self.delete_record()
    #     self.get_record()

    def rename(self, x_id, x_name, x_surname):
        self.name = x_name
        self.surname = x_surname
        self.update_record(x_id)

    def get_record(self, x_id):
        notes = self.db_helper.get_patient_card(x_id)
        for note in notes:
            self.name = note['name']
            self.surname = note['surname']
        # print(self.name, self.surname)

    def insert_record(self):
        self.db_helper.insert_patient_card(self.card_number, self.name, self.surname)

    # def get_record(self):
    #     self.db_helper.get_patient_card()

    def update_record(self, x_id):
        self.db_helper.update_patient_card(self.card_number, self.name, self.surname)

    def delete_record(self):
        self.db_helper.delete_patient_card(self.card_number)

    def form_title_string(self):
        return str(self.card_number) + " " + self.name + " " + self.surname

    def get_id(self):
        return self.card_number

    def form_title_end(self):
        return self.name + " " + self.surname

# a = ActiveRecordPatientCard(7022516, 'Петя', 'Васечкин')
# a.rename(7022516, 'Петя', 'Пупкин')
# a.delete_record()
# a.get_record()

# db_helper.DB_helper.getConnection(a)
# db_helper.getConnection()
# db_helper = DbHelper.DbHelper()
# db_helper.test_select()