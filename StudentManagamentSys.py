import heapq
import copy

class HashMapRecording:  
    undo_stack = []
    List_of_Students = [[] for _ in range(20)]   # Buckets for hash table

    def __init__(self, roll_no, name, course, grades):
        self.roll_no = roll_no
        self.name = name
        self.course = course
        self.grade = grades

    @staticmethod
    def hash_function(value):
        value = str(value)
        sum_of_char = sum(ord(char) for char in value)
        return sum_of_char % 20

    def addStudent(self):
        index = HashMapRecording.hash_function(self.roll_no)
        for student in HashMapRecording.List_of_Students[index]:
            if student.roll_no == self.roll_no:
                print(f"--Student with roll no. {self.roll_no} already exists--")
                return
        HashMapRecording.List_of_Students[index].append(self)
        # Save to undo stack
        HashMapRecording.undo_stack.append(('add', self))
        print(f"--Student {self.name} added at index {index}--")

    @staticmethod
    def searchStudent(roll_no):
        index = HashMapRecording.hash_function(roll_no)
        for student in HashMapRecording.List_of_Students[index]:
            if student.roll_no == roll_no:
                print("--Student Found--")
                print(f"Roll.no: {student.roll_no}")
                print(f"Name: {student.name}")
                print(f"Course: {student.course}")
                print(f"Grade: {student.grade}")
                return
        print("--Student not found--")

    @staticmethod
    def updateStudent(roll_no):
        index = HashMapRecording.hash_function(roll_no)
        for student in HashMapRecording.List_of_Students[index]:
            if student.roll_no == roll_no:
                # Save previous state for undo
                previous = copy.deepcopy(student)
                print("--Student Found--")
                while True:
                    print("\n1. Update Name")
                    print("2. Update Course")
                    print("3. Update Grade")
                    print("4. Back")
                    update_input = input("Enter choice: ")

                    try:
                        update_input = int(update_input)
                        if 1 <= update_input <= 4:
                            if update_input == 1:
                                student.name = input("Enter Updated Name: ")
                                print("--Student Name Updated Successfully--")
                            elif update_input == 2:
                                student.course = input("Enter Updated Course: ")
                                print("--Course Updated Successfully--")
                            elif update_input == 3:
                                updated_grade = input("Enter Updated Grades (comma separated): ")
                                student.grade = [g.strip() for g in updated_grade.split(",")]
                                print("--Grades Updated Successfully--")
                            elif update_input == 4:
                                print("--Back to main menu--")
                                return
                            HashMapRecording.undo_stack.append(('update', previous))
                        else:
                            print("--Invalid Choice--")
                    except:
                        print("--Input must be a valid number--")
                return
        print("--Student not found--")

    @staticmethod
    def deleteStudent(roll_no):
        index = HashMapRecording.hash_function(roll_no)
        for i, student in enumerate(HashMapRecording.List_of_Students[index]):
            if student.roll_no == roll_no:
                deleted = HashMapRecording.List_of_Students[index].pop(i)
                HashMapRecording.undo_stack.append(('delete', deleted))
                print(f"--Student with Roll no. {student.roll_no} deleted--")
                return
        print(f"--Student with roll no. {roll_no} not found--")

    def merge(left, right):
        result = []
        i = j = 0
        while i < len(left) and j < len(right):
            if left[i].roll_no < right[j].roll_no:
                result.append(left[i])
                i += 1
            else:
                result.append(right[j])
                j += 1
        result.extend(left[i:])
        result.extend(right[j:])
        return result

    def mergeSortStudents(students):
        if len(students) <= 1:
            return students
        mid = len(students) // 2
        left = HashMapRecording.mergeSortStudents(students[:mid])
        right = HashMapRecording.mergeSortStudents(students[mid:])
        return HashMapRecording.merge(left, right)

    @staticmethod
    def ShowStudents():
        all_students = []
        for bucket in HashMapRecording.List_of_Students:
            all_students.extend(bucket)
        if not all_students:
            print("--No student records found--")
            return
        sorted_students = HashMapRecording.mergeSortStudents(all_students)
        for student in sorted_students:
            print(f"Roll.no: {student.roll_no}")
            print(f"Name: {student.name}")
            print(f"Course: {student.course}")
            print(f"Grade: {student.grade}")
            print("----------------------")

    @staticmethod
    def calculate_average(grades):
        numeric_grades = []
        for g in grades:
            try:
                numeric_grades.append(float(g))
            except ValueError:
                letter_to_num = {'A': 90, 'B': 80, 'C': 70, 'D': 60, 'F': 0}
                numeric_grades.append(letter_to_num.get(g.strip().upper(), 0))
        return sum(numeric_grades) / len(numeric_grades) if numeric_grades else 0

    def topScorers():
        all_students = []
        for bucket in HashMapRecording.List_of_Students:
            all_students.extend(bucket)
        if not all_students:
            print("--No student records--")
            return
        student_averages = [(s, HashMapRecording.calculate_average(s.grade)) for s in all_students]
        top_students = sorted(student_averages, key=lambda x: x[1], reverse=True)[:3]
        for student, avg in top_students:
            print(f"Roll.no: {student.roll_no}, Name: {student.name}, Avg Grade: {avg:.2f}")
            print("----------------------")

    @staticmethod
    def rankings():
        all_students = []
        for bucket in HashMapRecording.List_of_Students:
            all_students.extend(bucket)
        if not all_students:
            print("--No student records--")
            return
        ranking_heap = [(-HashMapRecording.calculate_average(s.grade), s) for s in all_students]
        heapq.heapify(ranking_heap)
        rank = 1
        while ranking_heap:
            avg, student = heapq.heappop(ranking_heap)
            print(f"Rank {rank}: {student.name} (Avg Grade: {-avg:.2f})")
            rank += 1

    @staticmethod
    def undoLastOp():
        if not HashMapRecording.undo_stack:
            print("--No operations to undo--")
            return

        last_op, data = HashMapRecording.undo_stack.pop()
        index = HashMapRecording.hash_function(data.roll_no)

        if last_op == 'add':
            HashMapRecording.List_of_Students[index] = [
                s for s in HashMapRecording.List_of_Students[index] if s.roll_no != data.roll_no
            ]
            print(f"--Undo Add: Student {data.name} removed--")

        elif last_op == 'delete':
            HashMapRecording.List_of_Students[index].append(data)
            print(f"--Undo Delete: Student {data.name} restored--")

        elif last_op == 'update':
            for i, student in enumerate(HashMapRecording.List_of_Students[index]):
                if student.roll_no == data.roll_no:
                    HashMapRecording.List_of_Students[index][i] = data
                    print(f"--Undo Update: Student {data.name} reverted to previous state--")
                    return

def main():
    while True:
        print("\n1. Add Student\n2. Search Student\n3. Update Record\n4. Delete Student")
        print("5. Display all Students\n6. Top 3 Scorers\n7. Show Rankings")
        print("8. Undo Last Operation\n9. Exit")
        func_input = input("Enter your choice: ")

        try:
            func_input = int(func_input)
            if func_input == 1:
                roll_no = input("Enter Roll.no: ")
                name = input("Enter Name: ")
                course = input("Enter Course: ")
                grades_input = input("Enter Grades (comma separated): ")
                grades = [g.strip() for g in grades_input.split(",")]
                student = HashMapRecording(roll_no, name, course, grades)
                student.addStudent()
            elif func_input == 2:
                roll_no = input("Enter Roll.no to search: ")
                HashMapRecording.searchStudent(roll_no)
            elif func_input == 3:
                roll_no = input("Enter Roll.no to update: ")
                HashMapRecording.updateStudent(roll_no)
            elif func_input == 4:
                roll_no = input("Enter Roll.no to delete: ")
                HashMapRecording.deleteStudent(roll_no)
            elif func_input == 5:
                print("--Students List--")
                HashMapRecording.ShowStudents()
            elif func_input == 6:
                print("--Top 3 Scorers--")
                HashMapRecording.topScorers()
            elif func_input == 7:
                print("--Ranking--")
                HashMapRecording.rankings()
            elif func_input == 8:
                HashMapRecording.undoLastOp()
            elif func_input == 9:
                print("Exiting Program...")
                break
            else:
                print("--Invalid Choice--")
        except:
            print("--Input must be a valid number--")

print("-------------------------------")
print("---STUDENT MANAGEMENT SYSTEM---")
print("-------------------------------")
main()
