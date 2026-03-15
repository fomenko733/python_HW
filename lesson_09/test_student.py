# test_student.py
import pytest
from models import Student


def test_add_student(db_session):
    """Тест добавления студента"""
    student = Student(name="Анна Петрова", email="anna@test.ru")
    db_session.add(student)
    db_session.commit()
    db_session.refresh(student)

    assert student.id is not None
    assert student.name == "Анна Петрова"
    assert student.email == "anna@test.ru"

    # Проверка, что студент действительно в БД
    found = db_session.query(Student).filter_by(email="anna@test.ru").first()
    assert found is not None
    assert found.id == student.id


def test_update_student(db_session, create_test_student):
    """Тест изменения студента"""
    # Создаём тестовые данные
    student = create_test_student(name="Иван Иванов", email="ivan@test.ru")
    original_id = student.id

    # Обновляем данные
    student.name = "Иван Сидоров"
    student.email = "ivan.sidorov@test.ru"
    db_session.commit()
    db_session.refresh(student)

    # Проверяем изменения
    assert student.id == original_id  # ID не изменился
    assert student.name == "Иван Сидоров"
    assert student.email == "ivan.sidorov@test.ru"

    # Проверка через прямой запрос
    updated = db_session.query(Student).filter_by(id=original_id).first()
    assert updated.name == "Иван Сидоров"


def test_delete_student(db_session, create_test_student):
    """Тест удаления студента с очисткой данных"""
    # Создаём и удаляем
    student = create_test_student(name="Мария Смирнова", email="maria@test.ru")
    student_id = student.id

    db_session.delete(student)
    db_session.commit()

    # Проверяем, что студент удалён
    deleted = db_session.query(Student).filter_by(id=student_id).first()
    assert deleted is None

    # Дополнительная проверка: в таблице не должно быть записи с этим email
    by_email = db_session.query(Student).filter_by(email="maria@test.ru").first()
    assert by_email is None