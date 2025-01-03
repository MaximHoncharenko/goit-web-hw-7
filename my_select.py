from sqlalchemy import func, desc
from models import Student, Grade, Group, Teacher, Subject

# 1. Знайти 5 студентів із найбільшим середнім балом з усіх предметів
def select_1(session):
    result = session.query(Student.name, func.round(func.avg(Grade.grade), 2).label('avg_grade'))\
        .select_from(Grade).join(Student).group_by(Student.id)\
        .order_by(desc('avg_grade')).limit(5).all()
    return result

# 2. Знайти студента із найвищим середнім балом з певного предмета
def select_2(session, subject_id):
    result = session.query(Student.name, func.round(func.avg(Grade.grade), 2).label('avg_grade'))\
        .select_from(Grade).join(Student).join(Subject)\
        .filter(Subject.id == subject_id).group_by(Student.id)\
        .order_by(desc('avg_grade')).first()
    return result

# 3. Знайти середній бал у групах з певного предмета
def select_3(session, subject_id):
    result = session.query(Group.name, func.round(func.avg(Grade.grade), 2).label('avg_grade'))\
        .select_from(Grade).join(Student).join(Group).join(Subject)\
        .filter(Subject.id == subject_id).group_by(Group.id).all()
    return result

# 4. Знайти середній бал на потоці (по всій таблиці оцінок)
def select_4(session):
    result = session.query(func.round(func.avg(Grade.grade), 2).label('avg_grade')).scalar()
    return result

# 5. Знайти які курси читає певний викладач
def select_5(session, teacher_id):
    result = session.query(Subject.name).join(Teacher).filter(Teacher.id == teacher_id).all()
    return result

# 6. Знайти список студентів у певній групі
def select_6(session, group_id):
    result = session.query(Student.name).join(Group).filter(Group.id == group_id).all()
    return result

# 7. Знайти оцінки студентів у окремій групі з певного предмета
def select_7(session, group_id, subject_id):
    result = session.query(Student.name, Grade.grade)\
        .join(Group).join(Subject).filter(Group.id == group_id, Subject.id == subject_id).all()
    return result

# 8. Знайти середній бал, який ставить певний викладач зі своїх предметів
def select_8(session, teacher_id):
    result = session.query(func.round(func.avg(Grade.grade), 2).label('avg_grade'))\
        .join(Subject).join(Teacher).filter(Teacher.id == teacher_id).scalar()
    return result

# 9. Знайти список курсів, які відвідує певний студент
def select_9(session, student_id):
    result = session.query(Subject.name).join(Grade).filter(Grade.student_id == student_id).all()
    return result

# 10. Список курсів, які певному студенту читає певний викладач
def select_10(session, student_id, teacher_id):
    result = session.query(Subject.name).join(Grade).join(Teacher).filter(Grade.student_id == student_id, Teacher.id == teacher_id).all()
    return result
