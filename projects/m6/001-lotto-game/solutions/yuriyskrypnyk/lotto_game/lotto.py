from .typebill import TypeBill
from .city_bill import CityBill
from .generate_number import GenerateNumber
from .choose_number import ChooseNumber
from .print_bill import PrintBIll


class Lotto:

    def __init__(self, bill):
        self.bill = bill
        self.list_print = []

        for i in range(self.bill):
            print(f"The bill {i+1}")
            type_bill = TypeBill.type_of_bill()

            choose_number = ChooseNumber.chose_of_number(type_bill)

            choose_city = CityBill.choose_city()

            number_generate = GenerateNumber.generate_number(choose_number)

            self.list_print.append([type_bill, choose_city, number_generate])

        for bill_item in self.list_print:
            PrintBIll.printer_ticker(bill_item)

