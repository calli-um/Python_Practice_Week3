import heapq

# For Core Features
class HashMapRecording:  
    undo_stack=[]
    List_of_Students=[ [] for _ in range(20)]   # List of recorded data per student, inside a List of students

    # Constructor for a new record to be added
    def __init__(self, roll_no,name,course,grades):
        self.roll_no=roll_no
        self.name=name
        self.course=course
        self.grade=grades

    # Hash Map KEY Calculation
    @staticmethod
    def hash_function(value):
        value=str(value)
        sum_of_char=0
        for char in value:
            sum_of_char+=ord(char)

        return sum_of_char%20
    
    def addStudent(self):
        index = HashMapRecording.hash_function(self.roll_no)
        for student in HashMapRecording.List_of_Students[index]:
            if student.roll_no==self.roll_no:
                print(f"--Student with roll no. {self.roll_no} already exits--")
                return
            
        HashMapRecording.List_of_Students[index].append(self)
        print(f"--Student {self.name} added at index {index}--")
    
    @staticmethod
    def searchStudent(roll_no):
        index = HashMapRecording.hash_function(roll_no)
        for student in HashMapRecording.List_of_Students[index]:
            if student.roll_no==roll_no:
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
            if student.roll_no==roll_no:
                print("--Student Found--")
                while(True):
                    print("\n")
                    print(f"1. Update Name: {student.name}")
                    print(f"2. Update Course: {student.course}")
                    print(f"3. Update Grade: {student.grade}")
                    print(f"4. Back")
                    update_input=input("Enter choice: ")
                    print("\n")
                    try:
                        update_input=int(update_input)
                        if 0<update_input<5:
                            if update_input==1:
                                updated_name=input("Enter Updated Name: ")
                                student.name=updated_name
                                print("--Student Name Updated Successfully")
                                print("\n")
                            if update_input==2:
                                updated_course=input("Enter Updated Course: ")
                                student.course=updated_course
                                print("--Course Updated Successfully")
                                print("\n")
                            if update_input==3:
                                updated_grade = input("Enter Updated Grades separated by commas: ")
                                student.grade = [g.strip() for g in updated_grade.split(",")]
                                
                                print("--Grade Updated Successfully")
                                print("\n")
                            if update_input==4:
                                print("--Back to the main menu--")
                                print("\n")
                                return 
                        else:
                            print("--Invalid Choice--")
                            
                    except:
                        print("--Input must be a valid number--")

        print("--Student not found--")
        
    @staticmethod
    def deleteStudent(roll_no):
        index = HashMapRecording.hash_function(roll_no)
        for i, student in enumerate(HashMapRecording.List_of_Students[index]):
            if student.roll_no==roll_no:
                del HashMapRecording.List_of_Students[index][i]
                print(f"--Student with Roll no. {student.roll_no} deleted--")
                return
        print(f"--Student with roll no. {roll_no} not found--")

    def merge(left,right):
        result=[]
        i=j=0
        while i<len(left) and j<len(right):
            if left[i].roll_no < right[j].roll_no:
                result.append(left[i])
                i+=1
            else:
                result.append(right[j])
                j+=1

        result.extend(left[i:])
        result.extend(right[j:])
        return result
        
    def mergeSortStudents(students):
        if len(students)<=1:
            return students
        
        mid = len(students)//2
        left = HashMapRecording.mergeSortStudents(students[:mid])
        right= HashMapRecording.mergeSortStudents(students[mid:])

        return HashMapRecording.merge(left, right)
   

    @staticmethod
    def ShowStudents():
        all_students=[]
        for bucket in HashMapRecording.List_of_Students:
            all_students.extend(bucket)

        if not all_students:
            print("--No student records found--")
            return
        
        sorted_students=HashMapRecording.mergeSortStudents(all_students)
        
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
            # Convert letter grades to numbers 
                letter_to_num = {'A': 90, 'B': 80, 'C': 70, 'D': 60, 'F': 0}  # Dictionary
                numeric_value = letter_to_num.get(g.strip().upper(), 0)  # Default to 0 if unknown grade
                numeric_grades.append(numeric_value)

    # Return average if list is not empty
        if numeric_grades:
            return sum(numeric_grades) / len(numeric_grades)
        else:
            return 0
        
    def topScorers():
        all_students = []
        for bucket in HashMapRecording.List_of_Students:
            all_students.extend(bucket)

        if not all_students:
            print("--No student records--")
            return

        student_averages = []  

        for student in all_students:
            grades = student.grade if isinstance(student.grade, list) else student.grade.split(',')
            average = HashMapRecording.calculate_average(grades)
            student_averages.append((student, average))

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

        ranking_heap = []
        for student in all_students:
            avg = HashMapRecording.calculate_average(student.grade)
            heapq.heappush(ranking_heap, (-avg, student))  

        rank = 1
        while ranking_heap:
            avg, student = heapq.heappop(ranking_heap)
            print(f"Rank {rank}: {student.name} (Avg Grade: {-avg:.2f})")
            rank += 1


    def undoLastOp():
        print("--Not applicable yet--")


def main():
    while (True):
# Functionalities
        print("\n")
        print("1. Add Student")
        print("2. Search Student")
        print("3. Update Record")
        print("4. Delete Student")
        print("5. Display all Students")
        print("6. Top 3 Scorers")
        print("7. Show Rankings")
        print("8. Undo Last Operation")
        print("9. Exit")
        func_input=input("Enter your choice: ")
        try:
            func_input=int(func_input)
            if 0<func_input<10:
                if func_input==1:
                    print("\n")
                    roll_no=input("Enter Roll.no: ")
                    name=input("Enter Name: ")
                    course=input("Enter Course: ")
                    grades_input = input("Enter Grades separated by commas (e.g., 80,85,A,F): ")
                    grades = [g.strip() for g in grades_input.split(",")]
                    student = HashMapRecording(roll_no, name, course, grades)
                    student.addStudent()

                elif func_input==2:
                    print("\n")
                    roll_no=input("Enter Roll.no to search: ")
                    HashMapRecording.searchStudent(roll_no)

                elif func_input==3:
                    print("\n")
                    roll_no=input("Enter Roll.no to update: ")
                    HashMapRecording.updateStudent(roll_no)

                elif func_input==4:
                    print("\n")
                    roll_no=input("Enter Roll.no to delete: ")
                    HashMapRecording.deleteStudent(roll_no)

                elif func_input==5:
                    print("\n")
                    print("--Students List--")
                    print("----------------------")
                    HashMapRecording.ShowStudents()

                elif func_input==6:
                    print("\n")
                    print("--Top 3 Scorers--")
                    print("----------------------")
                    HashMapRecording.topScorers()

                elif func_input==7:
                    print("\n")
                    print("--Ranking--")
                    print("----------------------")
                    HashMapRecording.rankings()

                elif func_input==8:
                    HashMapRecording.undoLastOp()
                    
                elif func_input==9:
                    print("\n")
                    print("Exiting Program...")
                    break

            else:
                print("\n")
                print("--Invalid input--")
        except:
            print("--Input must be a valid number--")

print("-------------------------------")
print("---STUDENT MANAGEMENT SYSTEM---")
print("-------------------------------")
main()