from pathlib import Path

# Определение полного пути корневой директории работы программы
ROOT = Path(__file__).resolve().parent

# Указываем путь к файлам
OPERATIONS = Path.joinpath(ROOT, 'data_files/operations.json')

