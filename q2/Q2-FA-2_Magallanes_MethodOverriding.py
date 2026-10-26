class Patient:
    def __init__(self, name, bill_amount):
        self.__name = name
        self.__bill_amount = bill_amount

    def get_name(self):
        return self.__name

    def set_name(self, name):
        self.__name = name

    def get_bill_amount(self):
        return self.__bill_amount

    def set_bill_amount(self, bill_amount):
        if bill_amount >= 0:
            self.__bill_amount = bill_amount
        else:
            print("Bill amount cannot be negative.")

    def calculate_bill(self):
        return self.__bill_amount


class SeniorPatient(Patient):
    def calculate_bill(self):
        return self.get_bill_amount() * 0.80


class PhilHealthPatient(Patient):
    def calculate_bill(self):
        return self.get_bill_amount() * 0.85



patient1 = Patient("Juan Dela Cruz", 15000.00)
patient2 = SeniorPatient("Maria Santos", 15000.00)
patient3 = PhilHealthPatient("Pedro Reyes", 15000.00)

print("Hospital Billing System")
print("-----------------------")

print("\nPatient Name:", patient1.get_name())
print("Original Bill: ₱", format(patient1.get_bill_amount(), ",.2f"))
print("Final Bill: ₱", format(patient1.calculate_bill(), ",.2f"))

print("\nPatient Name:", patient2.get_name())
print("Original Bill: ₱", format(patient2.get_bill_amount(), ",.2f"))
print("Final Bill: ₱", format(patient2.calculate_bill(), ",.2f"))

print("\nPatient Name:", patient3.get_name())
print("Original Bill: ₱", format(patient3.get_bill_amount(), ",.2f"))
print("Final Bill: ₱", format(patient3.calculate_bill(), ",.2f"))