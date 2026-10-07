# results_manager.py - Data Structure (Dictionary)
from student import Student
from exam_record import ExamRecord

class ResultsManager:
    def __init__(self):
        # Dictionary - ONE data structure for Task 2
        self.records_db = {} # key = student_id, value = list of ExamRecord
        self.students_db = {}

    def add_student(self, student):
        if Student.validate_id(student.sid):
            self.students_db[student.sid] = student
            if student.sid not in self.records_db:
                self.records_db[student.sid] = []
            print(f"Student added: {student.name}")
        else:
            print("Invalid ID!")

    def add_record(self, record):
        sid = record.student.sid
        if sid not in self.records_db:
            self.records_db[sid] = []
            self.students_db[sid] = record.student
        self.records_db[sid].append(record)
        print(f"Record {record.rid} added for {record.student.name}")

    def display_all_records(self):
        print("\n========== ALL EXAM RECORDS ==========")
        if not self.records_db:
            print("No records found.")
            return
        for sid, records in self.records_db.items():
            print(f"\n--- Student: {sid} ---")
            self.students_db[sid].display_info()
            for rec in records:
                rec.display_info()
            avg = self.calculate_average(sid)
            print(f"Average: {avg:.2f}")

    def calculate_average(self, sid):
        if sid not in self.records_db or not self.records_db[sid]:
            return 0.0
        scores = [r.score for r in self.records_db[sid]]
        return sum(scores) / len(scores)