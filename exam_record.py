# exam_record.py - Class 2
from student import Student

class ExamRecord:
    def __init__(self, rid, student, subject, score):
        self.rid = rid
        self.student = student # Object interaction
        self.subject = subject
        self.score = score
        self.grade = self.calc_grade()

    # Instance method
    def calc_grade(self):
        if self.score >= 70: return "A"
        elif self.score >= 60: return "B"
        elif self.score >= 50: return "C"
        elif self.score >= 40: return "D"
        else: return "F"

    def display_info(self):
        print(f" {self.rid}: {self.subject} - {self.score} Grade {self.grade}")

    # Class method
    @classmethod
    def grade_scale(cls):
        return {"A":"70-100 (Excellent)", "B":"60-69 (Good)", "C":"50-59 (Credit)", "D":"40-49 (Pass)", "F":"0-39 (Fail)"}

    # Static methods
    @staticmethod
    def get_grade_from_score(score):
        if score >= 70: return "A"
        elif score >= 60: return "B"
        elif score >= 50: return "C"
        elif score >= 40: return "D"
        else: return "F"

    @staticmethod
    def valid_score(s):
        return 0 <= s <= 100