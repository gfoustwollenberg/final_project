class Person:
    def __init__(self, f_name="John", l_name='Doe', dob='01/01/1900', ssn='999-99-9996'):
        self.f_name = f_name
        self.l_name = l_name
        self.dob = dob
        self.ssn = ssn

    def __str__(self):
        return (f'First Name: {self.f_name}, Last Name: {self.l_name}, Date of Birth: {self.dob}, '
                f'SSN: {self.ssn}')
