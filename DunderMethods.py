class Employee:

    annualincrement = 1.04
    noofemp = 0

    def __init__(self,id , fname, lname, email, sal):
        self.id =id
        self.fname = fname
        self.lname = lname
        self.email = email
        self.sal = sal
        Employee.noofemp += 1

    def fullname(self):
        return self.fname + " " + self.lname

    def applysalraise(self):
        # self.sal = self.sal * Employee.annualincrement
        self.sal = self.sal * self.annualincrement

    @classmethod
    def setraise(cls, amount):
        cls.annualincrement = amount

    @classmethod
    def from_string(cls, empstr):
       id, fname, lname, email, sal = empstr.split('-')
        return cls(id,fname, lname, email, sal)

    @staticmethod
    def isworkday(day):
        if day.weekday() == 5 or day.weekday() == 6:
            return False
        return True

    def __repr__(self):
        # This returns the tuple of  instance form itsself
        return "Employee('{}','{}','{}',{})" .format(self.id,self.fname, self.lname, self.email, self.sal)

    def __str__(self):
        return "EmployeeInfo('{}','{}','{}',{})" .format(self.id,self.fname, self.lname, self.email, self.sal)

    def __add__(self, other):
        return self.sal + other.sal

    def __len__(self):
        return len(self.fname)


emp1 = Employee(101,"kasis", "Lakme", "kasis@comp.com", 5)
emp2 = Employee(102,"Benan", "Trout", "Benan@comp.com", 8)

# now print method will check for either repr or str dunder methods
print(emp1)

print(emp1.__repr__())

print(emp2.__str__())

print(repr(emp2))
print(str(emp1))


print(emp1+emp2)  # calls the add dunder

print(len(emp1))
