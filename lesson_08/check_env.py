import os
from dotenv import load_dotenv

# Загружаем .env (явный путь для надёжности)
current_dir = os.path.dirname(os.path.abspath(__file__))
env_path = os.path.join(current_dir, '.env')
load_dotenv(env_path)

print("=== Проверка переменных окружения ===")
print(f"YOUGILE_LOGIN: {os.getenv('YOUGILE_LOGIN', '❌ НЕ НАЙДЕН')}")
print(f"YOUGILE_PASSWORD: {'***' if os.getenv('YOUGILE_PASSWORD') else '❌ НЕ НАЙДЕН'}")
print(f"YOUGILE_COMPANY_ID: {os.getenv('YOUGILE_COMPANY_ID', '❌ НЕ НАЙДЕН')}")
print(f"YOUGILE_API_KEY: {'***' if os.getenv('YOUGILE_API_KEY') else '❌ НЕ НАЙДЕН'}")

# Проверка через Config
print("\n=== Проверка Config ===")
try:
    from config import Config
    cfg = Config()
    print(f"API URL: {cfg.api_url}")
    auth = cfg.auth_headers.get('Authorization', '❌ Нет токена')
    if auth and len(auth) > 30:
        print(f"Authorization: {auth[:30]}...")
    else:
        print(f"Authorization: {auth}")
    print("✅ Config работает корректно!")
except Exception as e:
    print(f"❌ Ошибка импорта Config: {type(e).__name__}: {e}")