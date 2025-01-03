from models import Base, engine
from seed import seed_database
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from models import Student, Group, Subject, Teacher, Grade
import os
from my_select import select_1

Session = sessionmaker(bind=engine)
session = Session()
# Створення бази даних (якщо її ще немає)
def create_database():
    # Якщо база даних ще не створена, то створюємо таблиці
    if not os.path.exists('your_database.db'):
        Base.metadata.create_all(engine)
        print("Database created successfully!")
    else:
        print("Database already exists.")

# Заповнення бази даних випадковими даними
def fill_database():
    session = sessionmaker(bind=engine)()
    
    try:
        # Генерація випадкових даних за допомогою Faker
        seed_database()
        print("Database successfully seeded!")
    except Exception as e:
        session.rollback()
        print(f"Error during seeding: {e}")
    finally:
        session.close()

# Основна функція для виконання дій
def main():
    create_database()  # Створюємо таблиці, якщо їх ще немає
    fill_database()    # Заповнюємо базу даних випадковими даними
    

if __name__ == "__main__":
    main()

    # приклад вибірки 
    students = select_1(session)

# Виводимо результати
    for student in students:    
        print(student)