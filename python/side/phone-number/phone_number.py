import re

class Phone(object):
    def __init__(self, phone_number):
        self.country_code = '1'
        self.validate_number(phone_number)

    def validate_number(self, number):
        pattern = re.compile(r'\+?([0-9])?[ .-]*\(?([0-9]{3})\)?[ -.]*([0-9]{3})[ -.]*([0-9]{4})')
        match = pattern.search(number)
        if not match:
            raise ValueError("Not a valid NANP number.")

        self.country_code = match.group(1)
        self.area_code = match.group(2)
        self.exchange_code = match.group(3)
        self.final_code = match.group(4)

        self.validate_country_code()
        self.validate_area_code()
        self.validate_exchange_code()
        self.number = f'{self.area_code}{self.exchange_code}{self.final_code}'

    def pretty(self):
        return f'({self.area_code}) {self.exchange_code}-{self.final_code}'

    def validate_exchange_code(self):
        if self.exchange_code[0] in ['0', '1']:
            raise ValueError("Exchange code must start with an number between 2 through 9")

    def validate_area_code(self):
        if self.area_code[0] in ['0', '1']:
            raise ValueError("Area code must start with an number between 2 through 9")

    def validate_country_code(self):
        if self.country_code and self.country_code != '1':
            raise ValueError("Country code must be 1 for EUA.")
