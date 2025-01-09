# Student Record System pyhon first project
class StudentRecordSystem:
    def __init__(self):
        self.student_records = {}

    def add_student(self, student_id, subjects_marks):
       
        if student_id not in self.student_records:
            self.student_records[student_id] = subjects_marks
            print(f"Student with ID {student_id} added successfully.")
        else:
            print(f"Student with ID {student_id} already exists.")

    def update_student(self, student_id, subject, marks):
       
        if student_id in self.student_records:
            if subject in self.student_records[student_id]:
                self.student_records[student_id][subject] = marks
                print(f"Marks for {subject} updated to {marks} for student ID {student_id}.")
            else:
                print(f"Subject {subject} does not exist for student ID {student_id}.")
        else:
            print(f"Student with ID {student_id} not found.")

    def delete_student(self, student_id):
        
        if student_id in self.student_records:
            del self.student_records[student_id]
            print(f"Student with ID {student_id} deleted successfully.")
        else:
            print(f"Student with ID {student_id} not found.")

    def calculate_total_and_percentage(self, student_id):
        
        if student_id in self.student_records:
            marks = self.student_records[student_id]
            total_marks = sum(marks.values())
            total_subjects = len(marks)
            percentage = (total_marks / (total_subjects * 100)) * 100
            return total_marks, percentage
        else:
            print(f"Student with ID {student_id} not found.")
            return None, None

    def display_student_info(self, student_id):
        
        if student_id in self.student_records:
            marks = self.student_records[student_id]
            total_marks, percentage = self.calculate_total_and_percentage(student_id)
            print(f"Student ID: {student_id}")
            print("Marks per subject:")
            for subject, mark in marks.items():
                print(f"  {subject}: {mark}")
            print(f"Total Marks: {total_marks}")
            print(f"Percentage: {percentage:.2f}%")
        else:
            print(f"Student with ID {student_id} not found.")

    def rank_students(self):
   
        student_totals = {}
        for student_id in self.student_records:
            total_marks, _ = self.calculate_total_and_percentage(student_id)
            student_totals[student_id] = total_marks

        ranked_students = sorted(student_totals.items(), key=lambda x: x[1], reverse=True)

        print("\nRanking of Students:")
        for rank, (student_id, total_marks) in enumerate(ranked_students, 1):
            print(f"Rank {rank}: Student ID {student_id} with Total Marks {total_marks}")



def main():
    srs = StudentRecordSystem()
    
    while True:
        print("\nSelect an option:")
        print("1. Add Student")
        print("2. Update Student Marks")
        print("3. Delete Student")
        print("4. Display Student Information")
        print("5. Rank Students")
        print("6. Exit")
        
        choice = input("Enter your choice (1-6): ")

        if choice == "1":
            student_id = int(input("Enter student ID: "))
            num_subjects = int(input("Enter number of subjects: "))
            subjects_marks = {}
            for _ in range(num_subjects):
                subject = input("Enter subject name: ")
                marks = int(input(f"Enter marks for {subject}: "))
                subjects_marks[subject] = marks
            srs.add_student(student_id, subjects_marks)
        
        elif choice == "2":
            student_id = int(input("Enter student ID: "))
            subject = input("Enter subject name: ")
            marks = int(input(f"Enter new marks for {subject}: "))
            srs.update_student(student_id, subject, marks)

        elif choice == "3":
            student_id = int(input("Enter student ID to delete: "))
            srs.delete_student(student_id)
        
        elif choice == "4":
            student_id = int(input("Enter student ID to display: "))
            srs.display_student_info(student_id)
        
        elif choice == "5":
            srs.rank_students()
        
        elif choice == "6":
            print("Exiting the program...")
            break
        
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
