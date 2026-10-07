# student.py - Class 1
class Student:
    total = 0

    def __init__(self, sid, name, prog, year):
        self.sid = sid
        self.name = name
        self.prog = prog
        self.year = year
        Student.total += 1

    # Instance method
    def display_info(self):
        print(f"ID: {self.sid} | Name: {self.name} | {self.prog} Year {self.year}")

    def update_record(self, name=None, prog=None, year=None):
        if name: self.name = name
        if prog: self.prog = prog
        if year: self.year = year
        print(f"Record updated for {self.sid}")

    # Class method
    @classmethod
    def get_total(cls):
        return cls.total

    @classmethod
    def from_string(cls, data_string):
        try:
            sid, name, prog, year = data_string.split(',')
            return cls(sid.strip(), name.strip(), prog.strip(), int(year.strip()))
        except:
            return None

    # Static method
    @staticmethod
    def validate_id(sid):
        return len(sid) >= 5