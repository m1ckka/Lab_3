from __future__ import annotations
from typing import TYPE_CHECKING, Any
from datetime import datetime, date
from dataclasses import dataclass
from abc import ABC, abstractmethod
if TYPE_CHECKING:
    from Staff import Student

@dataclass
class GroupInfo:
    """Information about Group.
    Args:
        id (int): Group id.
        title (str): Group name.
        students_list (list): Group list.
        department_id (int) Department id.
    """

    id: int
    title: str
    students_list: list
    department_id: int

@dataclass
class CourseInfo:
    """Information about Course.
        Args:
            title (str): Course title.
            start_date (date): Date of start.
            finish_date (date): Date of end.
            description (str): Information about 'Course'.
            lectures (list): Lectures list.
            assignments (list): Assignments list.
            limit (int): Students limit.
            students_list (list): Students List.
        """
    title: str
    start_date: date
    finish_date: date
    description: str
    lectures: list[str]
    assignments: list[str]
    limit: int
    students_list: list[int]

    def __str__(self) -> str:
        return f"Title: {self.title}\n" \
               f"Description: {self.description}\n" \
               f"Start date: {self.start_date}\n" \
               f"Finish date: {self.finish_date}\n" \
               f"Lectures: {self.lectures}\n" \
               f"Assignments: {self.assignments}\n" \
               f"Student limit: {self.limit}\n" \
               f"Students list: {self.students_list}\n"


class CourseProgress:
    """Progress of the course.
    Args:
        received_marks (dict): Student received marks.
        visited_lectures (int): Student attendance.
        completed_assignments (dict): Student assignments.
        notes (dict): student note.
    """

    def __init__(self, received_marks: dict, visited_lectures: int, completed_assignments: dict, notes: dict) -> None:
        self.received_marks = received_marks
        self.visited_lectures = visited_lectures
        self.completed_assignments = completed_assignments
        self.notes = notes

    def get_progress_to_date(self, date: datetime) -> list:
        """Returning marks.
        Arguments:
            date (datetime): date the mark is made.
        """
        marks = []
        for k, x in self.completed_assignments.items():
            if k < date:
                marks.append(x["mark"])
        return marks

    def get_final_mark(self) -> float:

        values = self.received_marks.values()
        amounts_of_marks = self.received_marks
        return sum(values) / len(amounts_of_marks)

    def fill_notes(self, note: str) -> None:
        """Adding new note
        Args:
            note (str): note.
        """
        today_date = date.today()
        self.notes[today_date] = note

    def remove_note(self, date: date) -> None:
        del self.notes[date]

class Course(ABC):
    def __init__(self) -> None:
        self._course_info = None

    @property
    def course_info(self) -> CourseInfo:
        return self._course_info

    @course_info.setter
    def course_info(self, course_info: CourseInfo) -> None:
        if isinstance(course_info, CourseInfo):
            self._course_info = course_info

    @abstractmethod
    def add_student(self, student: Student.personal_info.id) -> None:
        if student in self.course_info.students_list:
            raise ValueError(f"Student {student} already exists.")
        else:
            self.course_info.students_list.append(student)

    @abstractmethod
    def remove_student(self, student: Student.personal_info.id) -> None:
        if student not in self.course_info.students_list:
            raise ValueError(f"Student {student} doesn`t exists.")
        else:
            self.course_info.students_list.remove(student)


class MathCourse(Course):
    def __init__(self, practice_classes: int, modules: int):
        super().__init__()
        self.practice_classes = practice_classes
        self.modules = modules

    def __str__(self):
        return f"Course info: {self.course_info}" \
               f"\nMath course classes: {self.practice_classes}, Modules: {self.modules}"

    def add_student(self, student: Student.personal_info.id):
        if student in self.course_info.students_list:
            raise ValueError(f"Student {student} already exists.")
        else:
            self.course_info.students_list.append(student)

    def remove_student(self, student: Student.personal_info.id):
        if student not in self.course_info.students_list:
            raise ValueError(f"Student {student} doesn`t exists.")
        else:
            self.course_info.students_list.remove(student)


class ProgrammingCourse(Course):
    def __init__(self, patterns: int, modules: int):
        super().__init__()
        self.patterns = patterns
        self.modules = modules

    def __str__(self):
        return f"Course info: {self.course_info}" \
               f"\nProgramming course patterns: {self.patterns}, Modules: {self.modules}"

    def add_student(self, student: Student.personal_info.id):
        if student in self.course_info.students_list:
            raise ValueError(f"Student {student} already exists.")
        else:
            self.course_info.students_list.append(student)

    def remove_student(self, student: Student.personal_info.id):
        if student not in self.course_info.students_list:
            raise ValueError(f"Student {student} doesn`t exists.")
        else:
            self.course_info.students_list.remove(student)


class AlgorithmCourse(Course):
    def __init__(self, algorithms: int, modules: int):
        super().__init__()
        self.algorithms = algorithms
        self.modules = modules

    def __str__(self):
        return f"Course info: {self.course_info}" \
               f"\nProgramming course patterns: {self.algorithms}, Modules: {self.modules}"

    def add_student(self, student: Student.personal_info.id):
        if student in self.course_info.students_list:
            raise ValueError(f"Student {student} already exists.")
        else:
            self.course_info.students_list.append(student)

    def remove_student(self, student: Student.personal_info.id):
        if student not in self.course_info.students_list:
            raise ValueError(f"Student {student} doesn`t exists.")
        else:
            self.course_info.students_list.remove(student)

class Seminar:
    """Class represents seminar for 'Course'.
    Args:
        id_ (int): Seminar id.
        title (str): Seminar name.
        deadline (date): Seminar Deadline.
        assignments (list): Seminar assignments.
        status (Any): Seminar status.
        related_course (str): Seminar course.
    """
    def __init__(self, id_: int, title: str, deadline: date,
                 assignments: list[dict], status: Any, related_course: str) -> None:
        self.id = id_
        self.title = title
        self.deadline = deadline
        self.assignments = assignments
        self.status = status
        self.related_course = related_course

    def __str__(self):
        return f"\nSeminar id: {self.id} \nSeminar title: {self.title} " \
               f"\nDeadline: {self.deadline} \nAssignments: {self.assignments}" \
               f"\nStatus: {self.status} \nCourse: {self.related_course}"

    def implement_item(self, item_name: str) -> None:
        pass

    def add_comment(self, comment: str) -> None:
        pass

class Enrollment:
    """Enrollment Student to Course.
    Args:
        student (Student): Added student.
        course (Course): Added student to the ccurse.
    """

    def __init__(self, student: Student, course: Course):
        self.student = student
        self.course = course

    def enroll(self) -> None:
        if self.student.personal_info.id in self.course.course_info.students_list:
            raise ValueError("Student has already exists.")
        else:
            self.course.course_info.students_list.append(self.student.personal_info.id)

    def unenroll(self) -> None:
        if self.student.personal_info.id in self.course.course_info.students_list:
            self.course.course_info.students_list.remove(self.student.personal_info.id)
        else:
            raise ValueError("Student doesn`t exists.")