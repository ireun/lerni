# -*- coding: utf-8 -*-
from .meta import *


class LuckyNumbers(Base):
    __tablename__ = 'lucky_numbers'
    id = Column(Integer, primary_key=True)
    date = Column(Date)
    number = Column(Integer)

    def __init__(self, date, number):
        self.date = date
        self.number = number


class SchoolYears(Base):
    __tablename__ = 'log_school_years'
    id = Column(Integer, primary_key=True)
    start = Column(Date)
    end = Column(Date)
    add_date = Column(Date)
    modification_date = Column(Date)

    # Rok szkolny - start.year/end.year
    def __init__(self, start, end):
        self.start = start
        self.end = end
        self.add_date = datetime.datetime.now()
        self.modification_date = datetime.datetime.now()


# Semestr 1 / Semestr 2
class Terms(Base):
    __tablename__ = 'log_terms'
    id = Column(Integer, primary_key=True)
    year_id = Column(Integer, ForeignKey('log_school_years.id'))
    year = relationship("SchoolYears")
    start = Column(Date)
    end = Column(Date)
    add_date = Column(Date)
    modification_date = Column(Date)

    def __init__(self, year_id, start, end):
        self.year_id = year_id 
        self.start = start
        self.end = end
        self.add_date = datetime.datetime.now()
        self.modification_date = datetime.datetime.now()


# List of subject taught in the given school
class Subjects(Base):
    __tablename__ = 'log_subjects'
    id = Column(Integer, primary_key=True)
    name = Column(Text)
    short = Column(Text)
    add_date = Column(Date)
    modification_date = Column(Date)

    def __init__(self, name, short):
        self.name = name
        self.short = short
        self.add_date = datetime.datetime.now()
        self.modification_date = datetime.datetime.now()

        
class DivisionsCategories(Base):
    __tablename__ = 'log_divisions_categories'
    id = Column(Integer, primary_key=True)
    name = Column(Text)
    short = Column(Text)
    add_date = Column(Date)
    modification_date = Column(Date)

    def __init__(self, name, short):
        self.name = name
        self.short = short
        self.add_date = datetime.datetime.now()
        self.modification_date = datetime.datetime.now()


# List of groups
# Each division must have at least one group!
class Divisions(Base):
    __tablename__ = 'log_divisions'
    id = Column(Integer, primary_key=True)
    name = Column(Text)
    year_id = Column(Integer)
    category_id = Column(Integer, ForeignKey('log_divisions_categories.id'))
    category = relationship("DivisionsCategories")
    add_date = Column(Date)
    modification_date = Column(Date)

    def __init__(self, category_id, name, year_id):
        self.category_id = category_id
        self.name = name
        self.year_id = year_id
        self.add_date = datetime.datetime.now()
        self.modification_date = datetime.datetime.now()


# List of groups
class Groups(Base):
    __tablename__ = 'log_groups'
    id = Column(Integer, primary_key=True)
    division_id = Column(Integer, ForeignKey('log_divisions.id'))
    division = relationship("Divisions")
    name = Column(Text)
    add_date = Column(Date)
    modification_date = Column(Date)

    def __init__(self, division_id, name):
        self.name = name
        self.division_id = division_id
        self.add_date = datetime.datetime.now()
        self.modification_date = datetime.datetime.now()


# List of courses
# Course lasts for one term
# It have specified subject
# One or more group take part in course (but [rather] no more than one division)
# One course can be held by one or more teachers
# They choose the grading system together
class Courses(Base):
    __tablename__ = 'log_courses'
    id = Column(Integer, primary_key=True)
    term_id = Column(Integer, ForeignKey('log_terms.id'))
    term = relationship("Terms")
    subject_id = Column(Integer, ForeignKey('log_subjects.id'))
    subject = relationship("Subjects")
    add_date = Column(Date)
    modification_date = Column(Date)

    def __init__(self, term_id, subject_id):
        self.term_id = term_id
        self.subject_id = subject_id
        self.add_date = datetime.datetime.now()
        self.modification_date = datetime.datetime.now()


# Groups that take part in course
class GroupCorse(Base):
    __tablename__ = 'log_group_course'
    id = Column(Integer, primary_key=True)
    group_id = Column(Integer, ForeignKey('log_groups.id'))
    group = relationship("Groups")
    course_id = Column(Integer, ForeignKey('log_courses.id'))
    course = relationship("Courses")

    def __init__(self, group_id, course_id):
        self.group_id = group_id
        self.course_id = course_id


# Teachers that take part in course
class TeacherCourse(Base):
    __tablename__ = 'log_teacher_course'
    id = Column(Integer, primary_key=True)
    teacher_id = Column(Integer, ForeignKey('people.id'))
    teacher = relationship("People")
    course_id = Column(Integer, ForeignKey('log_courses.id'))
    course = relationship("Courses")

    def __init__(self, teacher_id, course_id):
        self.teacher_id = teacher_id
        self.course_id = course_id


# Weights used in the weighted average, set by holding teacher
# Przykłady: 'sprawdzin', 'kartkówka', 'praca dodatkowa', 'jedynka za pracę domową'/'praca w domu', 'akywność'
class TeacherWeights(Base):
    __tablename__ = 'log_teacher_weights'
    id = Column(Integer, primary_key=True)
    teacher_id = Column(Integer, ForeignKey('people.id'))
    teacher = relationship("People")
    name = Column(Text)
    short = Column(Text)
    weight = Column(Integer)

    def __init__(self, teacher_id, name, short, weight):
        self.teacher_id = teacher_id
        self.name = name
        self.short = short
        self.weight = weight


class CourseWeights(Base):
    __tablename__ = 'log_course_weights'
    id = Column(Integer, primary_key=True)
    course_id = Column(Integer, ForeignKey('log_courses.id'))
    course = relationship("Courses")
    weight_id = Column(Integer, ForeignKey('log_teacher_weights.id'))
    weight = relationship("TeacherWeights")

    def __init__(self, course_id, weight_id):
        self.course_id = course_id
        self.weight_id = weight_id


### Uczniowie i ich oceny#
class Marks(Base):
    __tablename__ = 'log_marks'
    id = Column(Integer, primary_key=True)
    teacher_id = Column(Integer)
    teacher = relationship("People")
    course_id = Column(Integer, ForeignKey('log_courses.id'))
    course = relationship("Courses")
    student_id = Column(Integer)
    student = relationship("People")
    value = Column(Integer)
    weight_id = Column(Integer, ForeignKey('log_teacher_weights.id'))
    weight = relationship("TeacherWeights")
    add_date = Column(Date)
    comment = Column(Text)
    corrected = Column(Boolean)
    __table_args__ = (ForeignKeyConstraint(["teacher_id", "student_id"], ["people.id", "people.id"]), {})

    def __init__(self, teacher_id, course_id, student_id, value, weight_id, add_date, comment, corrected):
        self.teacher_id = teacher_id
        self.course_id = course_id
        self.student_id = student_id
        self.value = value
        self.weight_id = weight_id
        self.add_date = add_date
        self.comment = comment
        self.corrected = corrected


class EndMarks(Base):
    __tablename__ = 'log_end_marks'
    id = Column(Integer, primary_key=True)
    course_id = Column(Integer, ForeignKey('log_courses.id'))
    course = relationship("Courses")
    student_id = Column(Integer, ForeignKey('people.id'))
    student = relationship("People")
    value = Column(Integer)

    def __init__(self, course_id, student_id, value):
        self.course_id = course_id
        self.student_id = student_id
        self.value = value


### Plan lekcji#
class Schedules(Base):
    __tablename__ = 'log_schedules'
    id = Column(Integer, primary_key=True)
    start = Column(Date)
    end = Column(Date)
    updated = Column(DateTime)

    def __init__(self, start, end):
        self.start = start
        self.end = end
        self.updated = datetime.datetime.now()


class Lessons(Base):
    __tablename__ = 'log_lessons'
    id = Column(Integer, primary_key=True)
    schedule_id = Column(Integer, ForeignKey('log_schedules.id'))
    schedule = relationship("Schedules")
    teacher_id = Column(Integer, ForeignKey('log_teachers.id'))
    teacher = relationship("Teachers")
    subject_id = Column(Integer, ForeignKey('log_subjects.id'))
    subject = relationship("Subjects")
    day = Column(Integer)
    order = Column(Integer)
    room = Column(Integer)
    updated = Column(DateTime)

    def __init__(self, schedule_id, teacher_id, subject_id, day, order, room):
        self.schedule_id = schedule_id
        self.teacher_id = teacher_id
        self.subject_id = subject_id
        self.day = day
        self.order = order
        self.room = room
        self.updated = datetime.datetime.now()


class LessonsGroups(Base):
    __tablename__ = 'log_lessons_groups'
    id = Column(Integer, primary_key=True)
    lesson_id = Column(Integer, ForeignKey('log_lessons.id'))
    lesson = relationship("Lessons")
    group_id = Column(Integer, ForeignKey('log_groups.id'))
    group = relationship("Groups")

    def __init__(self, lesson_id, group_id):
        self.lesson_id = lesson_id
        self.group_id = group_id


class LessonsLog(Base):
    __tablename__ = 'log_lessons_log'
    id = Column(Integer, primary_key=True)
    start = Column(DateTime)
    end = Column(DateTime)
    add_date = Column(DateTime)

    def __init__(self, start, end):
        self.start = start
        self.end = end
        self.updated = datetime.datetime.now()
        

class Settings(Base):
    __tablename__ = 'settings'
    id = Column(Integer, primary_key=True)
