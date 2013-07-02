from .meta import *
class SupportSections(Base):
	__tablename__ = 'support_sections'
	id = Column(Integer, primary_key=True)
	name = Column(Text)
	def __init__(self, name):
		self.name = name

class SupportSubSections(Base):
	__tablename__ = 'support_sub_sections'
	id = Column(Integer, primary_key=True)
	section_id = Column(Integer, ForeignKey('support_sections.id'))
	section = relationship("SupportSections")
	name = Column(Text)
	short_name = Column(Text)
	def __init__(self, section_id, name, short_name):
		self.section_id = section_id
		self.name = name
		self.short_name = short_name

class SupportTickets(Base):
	__tablename__ = 'support_tickets'
	id = Column(Integer, primary_key=True)
	sub_section_id = Column(Integer, ForeignKey('support_sub_sections.id'))
	sub_section = relationship("SupportSubSections")
	topic = Column(Text)
	email = Column(Text)
	password = Column(Text)
	importance = Column(Integer)
	confirmed = Column(Boolean)
	confirmation_code = Column(Text)
	add_date = Column(DateTime)
	def __init__(self, sub_section_id, topic, email, password, importance, confirmed, confirmation_code, add_date):
		self.sub_section_id = sub_section_id
		self.topic = topic
		self.email = email
		self.password = password
		self.importance = importance 
		self.confirmed = confirmed
		self.confirmation_code = confirmation_code
		self.add_date = add_date
		
class SupportQuestions(Base):
	__tablename__ = 'support_questions'
	id = Column(Integer, primary_key=True)
	ticket_id = Column(Integer, ForeignKey('support_tickets.id'))
	ticket = relationship("SupportTickets")
	text = Column(Text)
	add_date = Column(DateTime)
	def __init__(self, ticket_id, text, add_date):
		self.ticket_id = ticket_id
		self.text = text 
		self.add_date = add_date 
	