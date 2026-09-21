class AssignmentSubmission:


    def __init__(self, student_name: str, student_id: str, assignment_title: str, due_date: str):
        self.student_name = student_name
        self.student_id = student_id
        self._assignment_title = assignment_title
        self._due_date = due_date
        self.__is_submitted = False
        self.__grade = -1.0 
        self.__submitted_files = []

    def __validate_grade(self, score: float) -> bool:
        return 0.0 <= score <= 100.0

    def __check_submission_status(self) -> bool:
  
        return self.__grade != -1.0

    def __is_duplicate(self, filename: str) -> bool:
        return filename in self.__submitted_files
  
    def add_file(self, filename: str) -> None:
        if self.__check_submission_status():
            print(f"[Warning] Cannot add files. Assignment already graded.")
            return
        if self.__is_duplicate(filename):
            print(f"[Warning] '{filename}' is already attached!")
            return
        self.__submitted_files.append(filename)
        self.__is_submitted = True
        print(f"[Success] {self.student_name} attached '{filename}'. Total files: {len(self.__submitted_files)}")

    def remove_file(self, filename: str) -> None:
        if self.__check_submission_status():
            print(f"[Warning] {self.student_name} Cannot delete files. Assignment already graded")
            return
        if filename in self.__submitted_files:
            self.__submitted_files.remove(filename)
            print(f"Success] {self.student_name} removed '{filename}'.")
           
            if len(self.__submitted_files) == 0:
                self.__is_submitted = False
        else:
            print(f"[Warning] '{filename}' not found.")

    def assign_grade(self, score: float) -> None:
        if not self.__is_submitted or len(self.__submitted_files) == 0:
            print(f"[Error] Cannot grade. No files submitted for {self.student_name}.")
            return
        if not self.__validate_grade(score):
            print(f"[Error] Invalid grade: {score}. Must be 0–100.")
            return
        self.__grade = score
        print(f"[Success] Grade {score} officially assigned to {self.student_name}.")

    def get_grade(self) -> str:
        return "Not Graded" if self.__grade == -1.0 else str(self.__grade)

    def view_files(self) -> str:
        return ", ".join(self.__submitted_files) if self.__submitted_files else ""

    def get_status_report(self) -> str:
        if self.__is_submitted and len(self.__submitted_files) > 0:
            status = f"Submitted ({len(self.__submitted_files)} files)"
        else:
            status = "Missing"
        return f"ID: {self.student_id} | Name: {self.student_name} | Status: {status} | Grade: {self.get_grade()}"


print("--- INITIALIZING DROPBOX FOR STUDENTS ---")
student1 = AssignmentSubmission("Alex Gonzaga", "pshs-1090-x", "CS-101", "2026-10-01")
student2 = AssignmentSubmission("Adelle", "pshs-1920-x", "CS-103", "2026-10-01")
student3 = AssignmentSubmission("Juan dela Cruz", "pshs-1033-x", "CS-101", "2026-10-01")
student4 = AssignmentSubmission("Maria Santos", "pshs-1044-x", "CS-101", "2026-10-01")
student5 = AssignmentSubmission("Jose Reyes", "pshs-1055-x", "CS-101", "2026-10-01")
print()

print("--- TEST SCENARIO 1: Multiple Files via List ---")
student1.add_file("main.py")
student1.add_file("report.pdf")
student1.assign_grade(95)
print(f"Alex's Files: {student1.view_files()}\n")

print("--- TEST SCENARIO 2: Removing Files from List ---")
student2.add_file("wrong_homework.docx")
student2.remove_file("wrong_homework.docx")
student2.add_file("correct_project.py")
student2.assign_grade(88)
print(f"Adelle's Files: {student2.view_files()}\n")

print("--- TEST SCENARIO 3: Preventing Duplicate Files ---")
student3.add_file("script.py")
student3.add_file("script.py")
print(f"Juan's Files: {student3.view_files()}\n")

print("--- TEST SCENARIO 4: Removing file after being graded ---")
student4.add_file("exam_answers.pdf")
student4.assign_grade(75)
student4.remove_file("exam_answers.pdf")
print()

print("--- TEST SCENARIO 5: Empty List Handling ---")
student5.add_file("draft.txt")
student5.remove_file("draft.txt")
student5.assign_grade(100)
print()

print("--- FINAL SYSTEM REPORT ---")
print(student1.get_status_report())
print(student2.get_status_report())
print(student3.get_status_report())
print(student4.get_status_report())
print(student5.get_status_report())

