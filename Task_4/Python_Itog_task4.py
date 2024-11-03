import argparse

def main():
    
    # Создание парсера аргументов
    parser = argparse.ArgumentParser(description='Парсинг числа и строки с дополнительными опциями')
    
    # Добавление обязательных аргументов
    parser.add_argument('number', type=int, help='Число для вывода')
    parser.add_argument('text', type=str, help ='Строка для вывода')
    
    # Добавление опций
    parser.add_argument('--verbose', action='store_true', help='Вывод дополнительной информации')
    parser.add_argument('--repeat', type=int, default=1, help='Количество повторений строки')
    
    # Парсинг аргументов
    args = parser.parse_args()
    
    # Вывод дополнительной информации, если опция verbose установлена
    if args.verbose:
        print(f'Полученные аргументы: number={args.number}, text ="{args.text}", repeat={args.repeat} ')
        
    print(f'Число: {args.number}, Строка: {args.text*args.repeat}')
    
if __name__ == '__main__':
    main()