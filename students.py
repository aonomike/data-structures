class Student:
    def __init__(self, admision_number = None, name = ''):
        self.admision_number = admision_number
        self.name = name

a = [Student(10, 'Mike'), Student(11, 'Paul')]
new_a_list = sorted(a, key=lambda x: x.name, reverse=True)


print(a.sort(key = lambda x: x.admision_number))