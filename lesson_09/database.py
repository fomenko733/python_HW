# 09_lesson/database.py
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base
from dotenv import load_dotenv
import os

# Загружаем переменные из .env, если файл есть
load_dotenv()

# Получаем параметры подключения из переменных окружения или используем дефолтные
DATABASE_URL = os.getenv(
    "DATABASE_URL",
    "postgresql://myuser:mypassword@localhost:5432/mydatabase"
)

# Создаём engine
engine = create_engine(DATABASE_URL, echo=False)

# Создаём сессию
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Базовый класс для моделей
Base = declarative_base()
