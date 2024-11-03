import os
import logging
from collections import namedtuple
from argparse import ArgumentParser

# Определение nametuple для хранения информации о файле/каталоге
FileInfo = namedtuple('FileInfo',['name', 'extension', 'is_directory', 'parent_directory'])

# Настройки логгирования
logging.basicConfig(filename='Task_5\directory_contents.log', level=logging.INFO, format='%(asctime)s - %(message)s')

def collect_info(directory_path):
    """Собирает информацию о содержимом директории и сохраняет в лог    
    """
    if not os.path.isdir(directory_path):
        raise ValueError(f"Указанный путь {directory_path} не является директорией")
    
    # Получаем родительский каталог
    parent_directory = os.path.basename(os.path.abspath(directory_path))
    
    # Перебираем содержимое директории
    for entry in os.listdir(directory_path):
        entry_path = os.path.join(directory_path, entry)
        
        # Проверяем, является ли элемент директорией
        if os.path.isdir(entry_path):
            file_info = FileInfo(name=entry,extension=None, is_directory=True, parent_directory=parent_directory)
        else:
            name, extension = os.path.splitext(entry)
            file_info = FileInfo(name=name, extension=extension.lstrip('.'), is_directory=False, parent_directory=parent_directory)
            
        # Запись в лог
        logging.info(f'{file_info.name}' | {file_info.extension if file_info.extension else "N/A"} |
                     {"Diractory" if file_info.is_directory else "File"} | {file_info.parent_directory} )

def main():
    """Основная функция для обработки командной строки и сбора информации"""
    
    parser = ArgumentParser(description="Сбор информации о содержимом директории и запись в лог")
    parser.add_argument('directory', type=str, help="Путь до директории для анализа")
    
    args = parser.parse_args()
    directory_path = args.directory
    
    try:
        collect_info(directory_path)
        print(f'Информация о содержимом директории "{directory_path} успешно записана в файл "directory_contents.log" .')
    except ValueError as e:
        print(e)
    
if __name__ == '__main__':
    main()