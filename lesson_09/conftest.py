# 09_lesson/conftest.py
import pytest
from sqlalchemy import create_engine, event
from sqlalchemy.orm import sessionmaker, close_all_sessions
from database import Base, SessionLocal, DATABASE_URL  # ✅ Теперь эти импорты работают
from models import Student, Subject  # ✅ И эти тоже


@pytest.fixture(scope="function")
def db_session():
    """
    Фикстура создаёт изолированную сессию БД для каждого теста.
    Все изменения откатываются после завершения теста.
    """
    # Создаём тестовый engine
    engine = create_engine(DATABASE_URL, echo=False)

    # Создаём все таблицы из моделей
    Base.metadata.create_all(bind=engine)

    # Подключаемся и начинаем транзакцию
    connection = engine.connect()
    transaction = connection.begin()

    # Создаём сессию, привязанную к этой транзакции
    Session = sessionmaker(bind=connection)
    session = Session()

    yield session  # Передаём сессию в тест

    # === ОЧИСТКА ПОСЛЕ ТЕСТА ===
    session.close()
    transaction.rollback()  # Отменяем все изменения
    connection.close()

    # Закрываем все сессии и удаляем таблицы
    close_all_sessions()
    Base.metadata.drop_all(bind=engine)


@pytest.fixture
def create_test_student(db_session):
    """Хелпер для быстрого создания тестового студента"""

    def _create(name: str, email: str, group: str = "TestGroup"):
        student = Student(name=name, email=email, group=group)
        db_session.add(student)
        db_session.commit()
        db_session.refresh(student)
        return student

    return _create


@pytest.fixture
def create_test_subject(db_session):
    """Хелпер для быстрого создания тестового предмета"""

    def _create(title: str, hours: int = 36):
        subject = Subject(title=title, hours=hours)
        db_session.add(subject)
        db_session.commit()
        db_session.refresh(subject)
        return subject

    return _create
