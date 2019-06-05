from abc import abstractmethod
from Procedure import GlassesSelection, MakeRoentgen, DentalTreatment


class Doctor():
    @abstractmethod
    def create_procedure(self):
        """создать процедуру"""

    """назначить процедуру"""
    def assign_procedure(self, patient):
        procedure = self.create_procedure()
        # print(patient)
        time = ['10:00', '12:00', '14:00']
        cabine = ['101', '102', '103', '104']
        procedure.assign_procedure(time, patient, cabine)


class Oculist(Doctor):
    def create_procedure(self):
        return GlassesSelection()


class Traumatologist(Doctor):
    def create_procedure(self):
        return MakeRoentgen()


class Dentist(Doctor):
    def create_procedure(self):
        return DentalTreatment()


# a = Oculist()
# b = Traumatologist()
# c = Oculist()
# d = Dentist()
# e = Traumatologist()
#
# ar = [a, b, c, d, e]
# for i in ar:
#     # i.create_procedure()
#     i.assign_procedure()