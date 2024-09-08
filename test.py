class Student:
    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}

    def rate_lecturer(self, lecturer, course, grade):
    	if isinstance(lecturer, Lecturer) and course in self.courses_in_progress and course in lecturer.courses_attached:
    		if course in lecturer.grades:
    			lecturer.grades[course] += [grade]
    		else:
    			lecturer.grades[course] = [grade]
    	else:
    		return 'Ошибка'

    def __str__(self):
    	avg_grade = self.calculate_avg_grade()
    	return f"Имя: {self.name}\nФамилия: {self.surname}\nСредняя оценка за домашние задания: {avg_grade}\nКурсы в процессе изучения: {', '.join(self.courses_in_progress)}\nЗавершенные курсы: {', '.join(self.finished_courses)}"

    def calculate_avg_grade(self):
        total = 0
        count = 0
        for grades in self.grades.values():
            for grade in grades:
                total += grade
                count += 1
        return round(total / count, 1) if count else 0	

    def __eq__(self, other):
        return self.calculate_avg_grade() == other.calculate_avg_grade()

    def __lt__(self, other):
        return self.calculate_avg_grade() < other.calculate_avg_grade()

    def __gt__(self, other):
        return self.calculate_avg_grade() > other.calculate_avg_grade()

    def __ge__(self, other):
        return self.calculate_avg_grade() >= other.calculate_avg_grade()

    def __le__(self, other):
        return self.calculate_avg_grade() <= other.calculate_avg_grade()

    def __ne__(self, other):
        return self.calculate_avg_grade() != other.calculate_avg_grade()   
        
class Mentor:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []
        
class Lecturer(Mentor):
    def __init__(self, name, surname):
        super().__init__(name, surname)
        self.grades = {}

    def __str__(self):
        avg_grade = self.calculate_avg_grade()
        return f'Имя: {self.name}\nФамилия: {self.surname}\nСредняя оценка за лекции: {avg_grade}'

    def calculate_avg_grade(self):
        total = 0
        count = 0
        for grades in self.grades.values():
            for grade in grades:
                total += grade
                count += 1
        return round(total / count, 1) if count else 0

    def __eq__(self, other):
        if isinstance(other, Lecturer):
            return self.calculate_avg_grade() == other.calculate_avg_grade()
        return False

    def __lt__(self, other):
        if isinstance(other, Lecturer):
            return self.calculate_avg_grade() < other.calculate_avg_grade()
        return False

    def __gt__(self, other):
        if isinstance(other, Lecturer):
            return self.calculate_avg_grade() > other.calculate_avg_grade()
        return False

    def __le__(self, other):
        if isinstance(other, Lecturer):
            return self.calculate_avg_grade() <= other.calculate_avg_grade()
        return False

    def __ge__(self, other):
        if isinstance(other, Lecturer):
            return self.calculate_avg_grade() >= other.calculate_avg_grade()
        return False

    def __ne__(self, other):
        if isinstance(other, Lecturer):
            return self.calculate_avg_grade() != other.calculate_avg_grade()
        return False

class Reviewer(Mentor):
    def rate_hw(self, student, course, grade):
        if isinstance(student, Student) and course in self.courses_attached and course in student.courses_in_progress:
            if course in student.grades:
                student.grades[course] += [grade]
            else:
                student.grades[course] = [grade]
        else:
            return 'Ошибка'

    def __str__(self):
    	return f'Имя: {self.name}\nФамилия: {self.surname}'
 
student1 = Student('Ruoy', 'Eman', 'your_gender')
student1.courses_in_progress += ['Python']

student2 = Student('Igor', 'Dyshakov', 'male')
student2.courses_in_progress += ['Python']
 
cool_reviewer = Reviewer('Some', 'Buddy')
cool_reviewer.courses_attached += ['Python']

cool_reviewer2 = Reviewer('Paul', 'Wakker')
cool_reviewer2.courses_attached += ['Python']

cool_lecturer = Lecturer('Another', 'Buddy')
cool_lecturer.courses_attached += ['Python']

cool_lecturer2 = Lecturer('Stepan', 'Ivanov')
cool_lecturer2.courses_attached += ['PYthon']
 
cool_reviewer.rate_hw(student1, 'Python', 10)
cool_reviewer.rate_hw(student1, 'Python', 10)
cool_reviewer.rate_hw(student1, 'Python', 1)
 
student1.rate_lecturer(cool_lecturer, 'Python', 9)
student1.rate_lecturer(cool_lecturer, 'Python', 6)
student2.rate_lecturer(cool_lecturer2, 'Python', 10)

print(cool_reviewer)

print(student1)

print(student1 == student2)

def calculate_avg_student_grade(students, course):
    total = 0
    count = 0
    for student in students:
        if course in student.grades:
            for grade in student.grades[course]:
                total += grade
                count += 1
    return round(total / count, 1) if count else 0

def calculate_avg_lecture_grade(lecturers, course):
    total = 0
    count = 0

    for lecturer in lecturers:
        if course in lecturer.grades:
            for grade in lecturer.grades[course]:
                total += grade
                count += 1
    return round(total / count, 1) if count else 0

print(calculate_avg_student_grade([student1, student2], "Python"))
print(calculate_avg_lecture_grade([cool_lecturer, cool_lecturer2], "Python"))

