from faker import Faker
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine
from models import Base, Group, Student, Teacher, Subject, Grade
import random
import datetime

# Ініціалізація Faker
fake = Faker()

# Параметри підключення до бази даних
DATABASE_URL = "postgresql://postgres:mysecretpassword@localhost:5432/postgres"
engine = create_engine(DATABASE_URL, echo=False)

# Створення сесії
Session = sessionmaker(bind=engine)
session = Session()

# Функція для створення груп
def create_groups():
    groups = ['Group A', 'Group B', 'Group C']
    for group_name in groups:
        group = Group(name=group_name)
        session.add(group)
    session.commit()
    return session.query(Group).all()

# Функція для створення викладачів
def create_teachers():
    teachers = [fake.name() for _ in range(3)]
    teacher_objects = [Teacher(name=teacher) for teacher in teachers]
    session.add_all(teacher_objects)
    session.commit()
    return session.query(Teacher).all()

# Функція для створення предметів
def create_subjects(teachers):
    subjects = ['Math', 'Physics', 'Chemistry', 'History', 'Biology', 'Programming']
    subject_objects = []
    for subject in subjects:
        teacher = random.choice(teachers)
        subject_objects.append(Subject(name=subject, teacher=teacher))
    session.add_all(subject_objects)
    session.commit()
    return session.query(Subject).all()

# Функція для створення студентів
def create_students(groups):
    students = []
    for _ in range(30):  # Створюємо 30 студентів
        student = Student(
            name=fake.name(),
            group=random.choice(groups)
        )
        students.append(student)
    session.add_all(students)
    session.commit()
    return students

# Функція для створення оцінок
def create_grades(students, subjects):
    for student in students:
        for subject in subjects:
            for _ in range(random.randint(1, 2)):  # Максимум 2 оцінки на студента з кожного предмета
                grade = Grade(
                    student=student,
                    subject=subject,
                    grade=random.randint(1, 5),  # Оцінки від 1 до 5
                    date=fake.date_this_year()
                )
                session.add(grade)
    session.commit()

# Основна функція для заповнення бази даних
def seed_database():
    # Створення таблиць (якщо вони не створені раніше)
    Base.metadata.create_all(engine)
    
    # Створення груп, викладачів, предметів та студентів
    groups = create_groups()
    teachers = create_teachers()
    subjects = create_subjects(teachers)
    students = create_students(groups)
    
    # Створення оцінок для студентів
    create_grades(students, subjects)
    
    print("Базу даних успішно заповнено!")

# Викликаємо функцію заповнення бази даних
if __name__ == "__main__":
    seed_database()
