# main.py - Main program
from student import Student
from exam_record import ExamRecord
from results_manager import ResultsManager

def main():
    print("=== Limkokwing - Digital Exam & Results Management System ===")
    print("=== DPG Compliant - Modular, Open Source, Privacy-Respecting ===\n")

    manager = ResultsManager()

    # Task 1: Object creation and interaction
    s1 = Student("LKU/CS/001", "Amadu Bah", "Software Engineering", 2)
    s2 = Student("LKU/CS/002", "Mariama Conteh", "Computer Science", 2)
    s3 = Student.from_string("LKU/CS/003, Fatmata Kamara, IT, 2")

    manager.add_student(s1)
    manager.add_student(s2)
    manager.add_student(s3)

    r1 = ExamRecord("REC001", s1, "OOP", 78)
    r2 = ExamRecord("REC002", s1, "Database", 65)
    r3 = ExamRecord("REC003", s2, "OOP", 82)
    r4 = ExamRecord("REC004", s2, "Web Dev", 58)
    r5 = ExamRecord("REC005", s3, "OOP", 45)

    manager.add_record(r1)
    manager.add_record(r2)
    manager.add_record(r3)
    manager.add_record(r4)
    manager.add_record(r5)

    # Task 2: Display from data structure
    manager.display_all_records()

    # Task 3: Methods Demo
    print("\n========== METHODS DEMO ==========")
    print(f"Total Students (class method): {Student.get_total()}")
    print(f"Grade Scale (class method): {ExamRecord.grade_scale()}")
    print(f"Valid score 85? (static): {ExamRecord.valid_score(85)}")
    print(f"Grade for 85 (static): {ExamRecord.get_grade_from_score(85)}")
    s1.display_info() # instance method

    print("\n=== SUCCESS - All 3 Tasks Done - Modular Version ===")

if __name__ == "__main__":
    main()
