class Person:
    def __init__(self, name=None, age=None):
        self.name = name
        self.age = age

    def set_name(self, name):
        self.name = name
        return self  

    def set_age(self, age):
        self.age = age
        return self  

    def get_person_info(self):
        return f"Name: {self.name}, Age: {self.age}"