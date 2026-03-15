# conftest.py
import pytest
from sqlalchemy import create_engine, event
from sqlalchemy.orm import sessionmaker, close_all_sessions
from models import Base, Student
from database import DATABASE_URL, SessionLocal


@pytest.fixture(scope="function")
def db_session():
    """Создаёт изолированную сессию БД для каждого теста"""
    # Создаём тестовый engine с изоляцией транзакций
    engine = create_engine(DATABASE_URL, echo=False)

    # Создаём все таблицы
    Base.metadata.create_all(bind=engine)

    # Начинаем транзакцию
    connection = engine.connect()
    transaction = connection.begin()

    # Создаём сессию, привязанную к этой транзакции
    Session = sessionmaker(bind=connection)
    session = Session()

    yield session

    # Откатываем все изменения после теста
    session.close()
    transaction.rollback()
    connection.close()

    # Очищаем все сессии
    close_all_sessions()
    Base.metadata.drop_all(bind=engine)


@pytest.fixture
def create_test_student(db_session):
    """Хелпер для создания тестового студента"""

    def _create(name: str, email: str):
        student = Student(name=name, email=email)
        db_session.add(student)
        db_session.commit()
        db_session.refresh(student)
        return student

    return _create