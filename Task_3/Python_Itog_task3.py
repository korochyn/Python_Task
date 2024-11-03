from datetime import datetime, timedelta

def future_date(days_from_now):
    """
    Возвращает дату, которая наступит через указанное количество
    дней от текущей даты
    
    :param days_from_now: Количество дней от текущей даты
    :return: Отформатированная дата в формате YYYY-MM-DD

    """
    # Получение текущей даты и времени
    today = datetime.now()
    
    # Вычисление даты через указанное количество дней
    future_date = today + timedelta(days=days_from_now)
    
    # Форматирование будущей даты в строку в формате YYYY-MM-DD
    fomatted_future_date = future_date.strftime('%Y-%m-%d')
    
    return fomatted_future_date

if __name__=='__main__':
    days = 33 # Количество дней для вычисления
    print(f'Date {days} daysfrom now: {future_date(days)}')