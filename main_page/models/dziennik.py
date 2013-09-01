# -*- coding: utf-8 -*-

from .meta import *
class SchoolYears(Base):
    __tablename__ = 'log_school_years'
    id = Column(Integer, primary_key=True)
    add_date = Column(Date)
    start = Column(Date)
    end = Column(Date)
    def __init__(self, start, end): 	# Rok szkolny - start.year/end.year
        self.add_date = datetime.datetime.now()
        self.start = start
        self.end = end
        
class Terms(Base):
    __tablename__ = 'log_terms'						# Semestr 1 / Semestr 2
    id = Column(Integer, primary_key=True)
    year_id = Column(Integer, ForeignKey('log_school_years.id'))
    year = relationship("SchoolYears")
    start = Column(Date)
    end = Column(Date)
    add_date = Column(Date)
    def __init__(self, year_id, start, end):
        self.year_id = year_id 
        self.start = start
        self.end = end
        self.add_date = datetime.datetime.now()

class Subjects(Base):								### Nazwy przemiotów nauczanych w placówce
    __tablename__ = 'log_subjects'
    id = Column(Integer, primary_key=True)
    name = Column(Text)
    short = Column(Text)
    def __init__(self, name, short):
        self.name = name
        self.short = short
        
class DivisionsCategories(Base):									### Gimnazjum, Liceum, Klasy Językowe
    __tablename__ = 'log_divisions_categories'
    id = Column(Integer, primary_key=True)
    name = Column(Text)
    short = Column(Text)
    def __init__(self, name, short):
        self.name = name
        self.short = short

class Divisions(Base):									### Klasy utworzone w danym roku szkolnym
    __tablename__ = 'log_divisions'					### Każda klasa musi mieć conajmniej jedną grupę!
    id = Column(Integer, primary_key=True)
    name = Column(Text)
    year_id = Column(Integer)
    category_id = Column(Integer, ForeignKey('log_divisions_categories.id'))
    category = relationship("DivisionsCategories")
    def __init__(self, category_id, name, year_id):
        self.category_id = category_id
        self.name = name
        self.year_id = year_id
        
class Groups(Base):									### Lista grup
    __tablename__ = 'log_groups'
    id = Column(Integer, primary_key=True)
    division_id = Column(Integer, ForeignKey('log_divisions.id'))
    division = relationship("Divisions")
    name = Column(Text)
    def __init__(self, division_id, name):
        self.name = name
        self.division_id = division_id
        
class Courses(Base):										# Kurs - połączenie semestru, przedmiotu, _grup_ i _nauczycieli_
    __tablename__ = 'log_courses'							# Klasa uczestniczy w kursie
    id = Column(Integer, primary_key=True)					# Do jednego kursu może być przypisanych kilku nauczycieli
    term_id = Column(Integer, ForeignKey('log_terms.id')) # Sposób oceniania wybierać nauczyciel o przypisaniu o najmniejszym ID
    term = relationship("Terms")
    subject_id = Column(Integer, ForeignKey('log_subjects.id'))
    subject = relationship("Subjects")
    def __init__(self, term_id, subject_id):
        self.term_id = term_id
        self.subject_id = subject_id

class GroupCorse(Base):									# Lista grup uczestniczących w danym kursie
    __tablename__ = 'log_group_course'
    id = Column(Integer, primary_key=True)
    group_id = Column(Integer, ForeignKey('log_groups.id'))
    group = relationship("Groups")
    course_id = Column(Integer, ForeignKey('log_courses.id'))
    course = relationship("Courses")
    def __init__(self, group_id, course_id):
        self.group_id = group_id
        self.course_id = course_id
class TeacherCourse(Base):   						# Nauczyciele uczący na danym kursie
    __tablename__ = 'log_teacher_course'
    id = Column(Integer, primary_key=True)
    teacher_id = Column(Integer, ForeignKey('people.id'))
    teacher = relationship("People")
    course_id = Column(Integer, ForeignKey('log_courses.id'))
    course = relationship("Courses")
    def __init__(self, teacher_id, course_id):
        self.teacher_id = teacher_id
        self.course_id = course_id
  
class TeacherWeights(Base):						# Wagi ocen ustalone przez nauczyciela - wykorzystywane w CoursesWeights
    __tablename__ = 'log_teacher_weights'			# Przykłady: 'sprawdzin', 'kartkówka', 'praca dodatkowa', 'jedynka za pracę domową'/'praca w domu', 'akywność'
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
    def __init__(self,course_id,weight_id):
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
    def __init__(self,teacher_id,course_id,student_id,value,weight_id,add_date,comment,corrected):
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
    def __init__(self,course_id,student_id,value):
        self.course_id = course_id
        self.student_id = student_id
        self.value = value

### Plan lekcji#
class Schedules(Base):
    __tablename__ = 'log_schedules'
    id = Column(Integer, primary_key=True)
    year_id = Column(Integer)
    start = Column(Date)
    end = Column(Date)
    updated = Column(DateTime)
    def __init__(self, start, end):
        self.year_id = 1
        self.start = start
        self.end = end
        self.updated = datetime.datetime.now()

class Lessons(Base):
    __tablename__ = 'log_lessons'
    id = Column(Integer, primary_key=True)
    schedule_id = Column(Integer, ForeignKey('log_schedules.id'))
    schedule = relationship("Schedules")
    teacher_id = Column(Integer, ForeignKey('people.id'))
    teacher = relationship("People")
    group_id = Column(Integer, ForeignKey('log_groups.id'))
    group = relationship("Groups")
    subject_id = Column(Integer, ForeignKey('log_subjects.id'))
    subject = relationship("Subjects")
    day = Column(Integer)
    order = Column(Integer)
    room = Column(Integer)
    updated = Column(DateTime)
    def __init__(self, schedule_id, teacher_id, group_id, subject_id, day, order, room):
        self.schedule_id = schedule_id
        self.teacher_id = teacher_id
        self.group_id = group_id
        self.subject_id = subject_id
        self.day = day
        self.order = order
        self.room = room
        self.updated = datetime.datetime.now()

class LessonsLog(Base):
    __tablename__ = 'log_lessons_log'
    id = Column(Integer, primary_key=True)
    start=Column(DateTime)
    end=Column(DateTime)
    add_date=Column(DateTime)
    def __init__(self, start, end):
        self.start = start
        self.end = end
        self.updated = datetime.datetime.now()
        

class Settings(Base):
    __tablename__ = 'settings'
    id = Column(Integer, primary_key=True)
