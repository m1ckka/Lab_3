from Staff import Student, Professor, PersonalInfo, Department, Group, MathProfessor
from Course import MathCourse, ProgrammingCourse, AlgorithmCourse, CourseInfo, Seminar, Enrollment

if __name__ == "__main__":

    student = Student(None, None)
    student.personal_info = PersonalInfo(None, None, None, None, None, None, None, None, None)

    Franko_University = Department(None, None, None, None, None, None)

    course1 = MathCourse(None, None)
    course1.course_info = CourseInfo(None, None, None, None, None, None, None, [])
    course2 = ProgrammingCourse(None, None)
    course2.course_info = CourseInfo(None, None, None, None, None, None, None, None)
    course3 = AlgorithmCourse(None, None)
    course3.course_info = CourseInfo(None, None, None, None, None, None, None, None)
    seminar1 = Seminar(None, None, None, None, None, None)

    professor1 = MathProfessor(None, None)
    group = Group(None, None, None, None)

    print(f"{student.personal_info}\n{student}\n")
    print(Franko_University)

    enrollment_math = Enrollment(student, course1)
    enrollment_math.enroll()
    enrollment_math.unenroll()
    print(f"\n{course1.course_info.students_list}")
    print(f"{course1.course_info.students_list}")
    print(f"{course1.course_info.students_list}")

    course1.add_student(student.personal_info.id)
    course1.remove_student(student.personal_info.id)
    print(f"{course1.course_info.students_list}")
    print(f"{course1.course_info.students_list}")

    print(f"\n ")
    new_course = professor1.create_course(professor1, None, None, None, None, None, None, None, None)
    print(f"{new_course.course_info}")

    print(seminar1)
    course1.seminars = seminar1.title
    print(f"Seminars: {course1.seminars}")
