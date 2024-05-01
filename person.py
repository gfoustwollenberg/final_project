class Person:
    # constructor for person class which also validates input from all fields
    def __init__(self, f_name="John", l_name='Doe', dob='01/01/1900', ssn='999-99-9996'):
        name_characters = set("ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz'-")
        dob_characters = set("0123456789/")
        ssn_characters = set("0123456789-")
        if not (name_characters.issuperset(l_name) and name_characters.issuperset(f_name)):
            raise ValueError("Invalid Name Format, please try again!")
        if not (dob_characters.issuperset(dob)):
            raise ValueError("Invalid Date Format, please try again!")
        if not (ssn_characters.issuperset(ssn)):
            raise ValueError("Invalid Social Security Number, please try again!")
        self.f_name = f_name
        self.l_name = l_name
        self.dob = dob
        self.ssn = ssn

    # print function in case return of information is needed
    def __str__(self):
        return (f'First Name: {self.f_name}, Last Name: {self.l_name}, Date of Birth: {self.dob}, '
                f'SSN: {self.ssn}')

