class Students:
    def __init__(self, student_id, student_Name, department, Year_of_study,
                 age, gender, CGPA, mobile, address):
        self.student_id = student_id
        self.student_Name = student_Name
        self.department = department
        self.Year_of_study = Year_of_study
        self.age = age
        self.gender = gender
        self.CGPA = CGPA
        self.mobile = mobile
        self.address = address

    def Show(self):
        print(f"{self.student_id:<5}"
              f"{self.student_Name:<18}"
              f"{self.department:<10}"
              f"{self.Year_of_study:<6}"
              f"{self.age:<5}"
              f"{self.gender:<8}"
              f"{self.CGPA:<6}"
              f"{self.mobile:<15}"
              f"{self.address:<15}")


students = []


n = int(input("Enter number of students: "))


for i in range(n):
    print(f"\nEnter details of Student {i+1}")

    sid = int(input("Student ID: "))
    name = input("Name: ")
    dept = input("Department: ")
    year = int(input("Year of Study: "))
    age = int(input("Age: "))
    gender = input("Gender: ")
    cgpa = float(input("CGPA: "))
    mobile = input("Mobile Number: ")
    address = input("Address: ")

    students.append(
        Students(sid, name, dept, year, age, gender, cgpa, mobile, address)
    )


print("\nALL STUDENTS")
print("-" * 110)
print(f"{'ID':<5}{'Name':<18}{'Dept':<10}{'Year':<6}{'Age':<5}"
      f"{'Gender':<8}{'CGPA':<6}{'Mobile':<15}{'Address':<15}")
print("-" * 110)

for student in students:
    student.Show()


print("\nTotal Students =", len(students))


print("\nStudents having CGPA > 8.5")
print("-" * 110)
print(f"{'ID':<5}{'Name':<18}{'Dept':<10}{'Year':<6}{'Age':<5}"
      f"{'Gender':<8}{'CGPA':<6}{'Mobile':<15}{'Address':<15}")
print("-" * 110)

for student in students:
    if student.CGPA > 8.5:
        student.Show()

students.sort(key=lambda x: x.CGPA, reverse=True)

print("\nStudents Sorted by CGPA (Highest First)")
print("-" * 110)
print(f"{'ID':<5}{'Name':<18}{'Dept':<10}{'Year':<6}{'Age':<5}"
      f"{'Gender':<8}{'CGPA':<6}{'Mobile':<15}{'Address':<15}")
print("-" * 110)

for student in students:
    student.Show()