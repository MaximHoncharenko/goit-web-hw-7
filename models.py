from sqlalchemy import Column, Integer, String, ForeignKey, Date
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# Створюємо engine для підключення до бази даних
DATABASE_URL = "postgresql://postgres:mysecretpassword@localhost:5432/postgres"  # Змініть на відповідну URL
engine = create_engine(DATABASE_URL)

# Створюємо сесію для роботи з базою даних
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Створення базового класу для моделей
Base = declarative_base()

# Модель для Group
class Group(Base):
    __tablename__ = 'groups'
    
    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    
    # Зв'язок з студентами
    students = relationship('Student', back_populates='group')
    
    def __repr__(self):
        return f"<Group(id={self.id}, name={self.name})>"

# Модель для Student
class Student(Base):
    __tablename__ = 'students'
    
    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    group_id = Column(Integer, ForeignKey('groups.id'))
    
    # Зв'язок з групою
    group = relationship('Group', back_populates='students')
    
    # Зв'язок з оцінками
    grades = relationship('Grade', back_populates='student')
    
    def __repr__(self):
        return f"<Student(id={self.id}, name={self.name}, group_id={self.group_id})>"

# Модель для Teacher
class Teacher(Base):
    __tablename__ = 'teachers'
    
    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    
    # Зв'язок з предметами
    subjects = relationship('Subject', back_populates='teacher')
    
    def __repr__(self):
        return f"<Teacher(id={self.id}, name={self.name})>"

# Модель для Subject
class Subject(Base):
    __tablename__ = 'subjects'
    
    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    teacher_id = Column(Integer, ForeignKey('teachers.id'))
    
    # Зв'язок з викладачем
    teacher = relationship('Teacher', back_populates='subjects')
    
    # Зв'язок з оцінками
    grades = relationship('Grade', back_populates='subject')
    
    def __repr__(self):
        return f"<Subject(id={self.id}, name={self.name}, teacher_id={self.teacher_id})>"

# Модель для Grade (оцінки)
class Grade(Base):
    __tablename__ = 'grades'
    
    id = Column(Integer, primary_key=True)
    grade = Column(Integer, nullable=False)
    date = Column(Date, nullable=False)
    student_id = Column(Integer, ForeignKey('students.id'))
    subject_id = Column(Integer, ForeignKey('subjects.id'))
    
    # Зв'язок з студентом
    student = relationship('Student', back_populates='grades')
    
    # Зв'язок з предметом
    subject = relationship('Subject', back_populates='grades')
    
    def __repr__(self):
        return f"<Grade(id={self.id}, grade={self.grade}, date={self.date}, student_id={self.student_id}, subject_id={self.subject_id})>"

