from .meta import *
class Substitutions(Base):
    __tablename__ = 'substitutions'
    id = Column(Integer, primary_key=True)
    date_for = Column(Date)
    date_as = Column(Date)
    published = Column(DateTime)
    suit = Column(Boolean)
    comments = Column(Text)

    def __init__(self, date_for, date_as, published, suit, comments):
        self.date_for = date_for
        self.date_as = date_as
        self.published = published
        self.suit = suit
        self.comments = comments
        
class Occupations(Base):
    __tablename__ = 'occupations'
    id = Column(Integer, primary_key=True)
    name = Column(Text)
    
    def __init__(self, name):
        self.name = name


class Absent(Base):
    __tablename__ = 'substitutions_absent_teachers'
    id = Column(Integer, primary_key=True)
    teacher_id = Column(Integer, ForeignKey('people.id'))
    reason = Column(Text)
    lesson1 = Column(Boolean)
    lesson2 = Column(Boolean)
    lesson3 = Column(Boolean)
    lesson4 = Column(Boolean)
    lesson5 = Column(Boolean)
    lesson6 = Column(Boolean)
    lesson7 = Column(Boolean)
    lesson8 = Column(Boolean)
    substitutions_id = Column(Integer, ForeignKey('substitutions.id'))

    def __init__(self, teacher_id, reason, lesson1, lesson2, lesson3, lesson4, lesson5, lesson6, lesson7, lesson8, substitutions_id):
        self.teacher_id = teacher_id
        self.reason = reason
        self.lesson1 = lesson1
        self.lesson2 = lesson2
        self.lesson3 = lesson3
        self.lesson4 = lesson4
        self.lesson5 = lesson5
        self.lesson6 = lesson6
        self.lesson7 = lesson7
        self.lesson8 = lesson8
        self.substitutions_id = substitutions_id
        
        
class Replace(Base):
    __tablename__ = 'substitutions_replace_teachers'
    id = Column(Integer, primary_key=True)
    teacher_id = Column(Integer)
    empty_column = Column(Text)
    c1_id = Column(Integer, ForeignKey('log_groups.id'))
    c1_g1 = Column(Boolean)
    c1_g2 = Column(Boolean)
    c2_id = Column(Integer, ForeignKey('log_groups.id'))
    c2_g1 = Column(Boolean)
    c2_g2 = Column(Boolean)
    c3_id = Column(Integer, ForeignKey('log_groups.id'))
    c3_g1 = Column(Boolean)
    c3_g2 = Column(Boolean)
    c4_id = Column(Integer, ForeignKey('log_groups.id'))
    c4_g1 = Column(Boolean)
    c4_g2 = Column(Boolean)
    c5_id = Column(Integer, ForeignKey('log_groups.id'))
    c5_g1 = Column(Boolean)
    c5_g2 = Column(Boolean)
    c6_id = Column(Integer, ForeignKey('log_groups.id'))
    c6_g1 = Column(Boolean)
    c6_g2 = Column(Boolean)
    c7_id = Column(Integer, ForeignKey('log_groups.id'))
    c7_g1 = Column(Boolean)
    c7_g2 = Column(Boolean)
    c8_id = Column(Integer, ForeignKey('log_groups.id'))
    c8_g1 = Column(Boolean)
    c8_g2 = Column(Boolean)
    substitutions_id = Column(Integer)

    def __init__(self, teacher_id, empty_column, c1_id, c1_g1, c1_g2, c2_id, c2_g1, c2_g2, c3_id, c3_g1, c3_g2, c4_id, c4_g1, c4_g2,
    c5_id, c5_g1, c5_g2, c6_id, c6_g1, c6_g2, c7_id, c7_g1, c7_g2, c8_id, c8_g1, c8_g2, substitutions_id):
        self.teacher_id = teacher_id
        self.empty_column = empty_column
        self.c1_id = c1_id
        self.c1_g1 = c1_g1
        self.c1_g2 = c1_g2
        self.c2_id = c1_id
        self.c2_g1 = c1_g1
        self.c2_g2 = c1_g2
        self.c3_id = c1_id
        self.c3_g1 = c1_g1
        self.c3_g2 = c1_g2
        self.c4_id = c1_id
        self.c4_g1 = c1_g1
        self.c4_g2 = c1_g2
        self.c5_id = c1_id
        self.c5_g1 = c1_g1
        self.c5_g2 = c1_g2
        self.c6_id = c1_id
        self.c6_g1 = c1_g1
        self.c6_g2 = c1_g2
        self.c7_id = c1_id
        self.c7_g1 = c1_g1
        self.c7_g2 = c1_g2
        self.c8_id = c1_id
        self.c8_g1 = c1_g1
        self.c8_g2 = c1_g2
        self.substitutions_id = substitutions_id

class Duty(Base):
    __tablename__ = 'substitutions_duty'
    id = Column(Integer, primary_key=True)
    teacher1_id = Column(Integer)
    shift_id = Column(Integer)
    place_id = Column(Integer)
    teacher2_id = Column(Integer)
    substitutions_id = Column(Integer)
    
    def __init__(self, teacher1_id, shift_id, place_id, teacher2_id, substitutions_id):
        self.teacher1_id = teacher1_id
        self.shift_id = shift_id
        self.place_id = place_id
        self.teacher2_id = teacher2_id
        self.substitutions_id = substitutions_id

class Shift(Base):
    __tablename__ = 'shift'
    id = Column(Integer, primary_key=True)
    name = Column(Text)
    
    def __init__(self, name):
        self.name = name

class Places(Base):
    __tablename__ = 'places'
    id = Column(Integer, primary_key=True)
    name = Column(Text)
    
    def __init__(self, name):
        self.name = name
        
class Association(Base):
    __tablename__ = 'people_groups'
    id = Column(Integer, primary_key=True)
    people_id = Column(Integer, ForeignKey('people.id'))
    #student = relationship("People")
    groups_id = Column(Integer, ForeignKey('log_groups.id')) ## possibly nosense
    #groups = relationship("Groups")
    part_1 = Column(Boolean)
    part_2 = Column(Boolean)
    
    def __init__(self, people_id, groups_id, part_1, part_2):
        self.people_id = people_id
        self.groups_id = groups_id
        self.part_1 = part_1
        self.part_2 = part_2
        
class LuckyNumbers(Base):
    __tablename__ = 'lucky_numbers'
    id = Column(Integer, primary_key=True)
    date = Column(Date)
    number = Column(Integer)

    def __init__(self, date, number):
        self.date = date
        self.number = number
