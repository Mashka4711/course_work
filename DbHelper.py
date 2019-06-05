import pymysql


class DbHelper:
    def __init__(self):
        self.conn = self.get_connection()

    def get_connection(self):
        return pymysql.connect(host="localhost", user="root",
                               passwd="root", db="db_clinic", charset="utf8")

    def insert_patient_card(self, id, name, surname):
        query = "INSERT INTO patient_card (id_card, name, surname) VALUES ('%s', '%s', '%s')" % (id, name, surname)
        try:
            curs_note = self.conn.cursor(pymysql.cursors.DictCursor)
            curs_note.execute(query)
        except pymysql.IntegrityError as err:
            print("Error: {}".format(err))
        self.conn.commit()

    def update_patient_card(self, id, name, surname):
        query = "UPDATE patient_card SET name = '%s', surname = '%s' WHERE id_card = '%s'" % (name, surname, id)
        try:
            curs_note = self.conn.cursor(pymysql.cursors.DictCursor)
            curs_note.execute(query)
        except pymysql.IntegrityError as err:
            print("Error: {}".format(err))
            self.conn.commit()

    def get_patient_card(self, id_cp):
        query = "SELECT * FROM patient_card WHERE id_card = '%s'" % (id_cp)
        curs_notes = self.conn.cursor(pymysql.cursors.DictCursor)
        curs_notes.execute(query)
        notes = curs_notes.fetchall()
        # print(notes)
        return notes

    def delete_patient_card(self, id):
        del_query = "DELETE FROM patient_card WHERE id_card = '%s'" % id
        curs_del = self.conn.cursor(pymysql.cursors.DictCursor)
        curs_del.execute(del_query)
        self.conn.commit()

    def insert_doctor(self, id, name, surname, prof):
        query = "INSERT INTO doctor (id_doctor, name, surname, specialization) VALUES ('%s', '%s', '%s', '%s')" % (id, name, surname, prof)
        try:
            curs_note = self.conn.cursor(pymysql.cursors.DictCursor)
            curs_note.execute(query)
        except pymysql.IntegrityError as err:
            print("Error: {}".format(err))
        self.conn.commit()

    def update_doctor(self, id, name, surname, prof):
        query = "UPDATE doctor SET name = '%s', surname = '%s', specialization = '%s' WHERE id_doctor = '%s'" % (name, surname, prof, id)
        try:
            curs_note = self.conn.cursor(pymysql.cursors.DictCursor)
            curs_note.execute(query)
        except pymysql.IntegrityError as err:
            print("Error: {}".format(err))
            self.conn.commit()

    def get_doctor(self, id):
        query = "SELECT * FROM doctor WHERE id_doctor = '%s'" % (id)
        curs_notes = self.conn.cursor(pymysql.cursors.DictCursor)
        curs_notes.execute(query)
        notes = curs_notes.fetchall()
        # print(notes)
        return notes

    def delete_doctor(self, id):
        del_query = "DELETE FROM doctor WHERE id_doctor = '%s'" % id
        curs_del = self.conn.cursor(pymysql.cursors.DictCursor)
        curs_del.execute(del_query)
        self.conn.commit()

    # def get_doctors_count(self):
    #     notes_query = "SELECT COUNT(*) FROM doctor"
    #     curs_notes = self.conn.cursor(pymysql.cursors.DictCursor)
    #     curs_notes.execute(notes_query)
    #     notes = curs_notes.fetchall()
    #     for item in notes:
    #         count_bd = dict(item)
    #         return count_bd['COUNT(*)']
    #
    # def get_patients_count(self):
    #     notes_query = "SELECT COUNT(*) FROM patient_card"
    #     curs_notes = self.conn.cursor(pymysql.cursors.DictCursor)
    #     curs_notes.execute(notes_query)
    #     notes = curs_notes.fetchall()
    #     for item in notes:
    #         count_bd = dict(item)
    #         return count_bd['COUNT(*)']

    def get_doctors_ids(self):
        notes_query = "SELECT id_doctor FROM doctor"
        curs_notes = self.conn.cursor(pymysql.cursors.DictCursor)
        curs_notes.execute(notes_query)
        notes = curs_notes.fetchall()
        ids = []
        for note in notes:
            str_id = note['id_doctor']
            ids.append(int(str_id))
            # print(str_id)
        return ids

    def get_patients_ids(self):
        notes_query = "SELECT id_card FROM patient_card"
        curs_notes = self.conn.cursor(pymysql.cursors.DictCursor)
        curs_notes.execute(notes_query)
        notes = curs_notes.fetchall()
        ids = []
        for note in notes:
            str_id = note['id_card']
            ids.append(int(str_id))
            # print(str_id)
        return ids