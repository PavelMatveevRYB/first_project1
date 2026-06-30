from dotenv import load_dotenv  # ← эту строку нужно добавить
import os

def print_author():
    load_dotenv()  # загружаем переменные из .env-файла
    author = os.getenv('AUTHOR')  # читаем значение AUTHOR
    print(f"Автор проекта: {author}")

print_author()  # вызываем функцию

