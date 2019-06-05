from abc import abstractmethod
import random


class Procedure():
    @abstractmethod
    def assign_procedure(self, time, p, cab):
        """назначить процедуру"""


class GlassesSelection(Procedure):
    def assign_procedure(self, time, p, cab):
        print("Окулист назначил пациенту: " + p + "\nПроцедуру в " + random.choice(time) + " в кабинете " +
              random.choice(cab))


class MakeRoentgen(Procedure):
    def assign_procedure(self, time, p, cab):
        print("Травматолог назначил пациенту: " + p + "\nПроцедуру в " + random.choice(time) + " в кабинете " +
              random.choice(cab))


class DentalTreatment(Procedure):
    def assign_procedure(self, time, p, cab):
        print("Стоматолог назначил пациенту: " + p + "\nПроцедуру в " + random.choice(time) + " в кабинете " +
              random.choice(cab))


# a = GlassesSelection()
# b = MakeRoentgen()
# c = GlassesSelection()
# d = DentalTreatment()
# e = MakeRoentgen()

# ar = [a, b, c, d, e]
# for i in ar:
#     i.assign_procedure()