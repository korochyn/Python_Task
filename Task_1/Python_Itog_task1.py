import logging

# Настройка логгирования

logger = logging.getLogger()
logger.setLevel(logging.DEBUG)

# Форматер для сообщения

formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')

# Обработчик для сообщений уровня DEBUG и INFO

debug_info_handler = logging.FileHandler('Task_1\debug_info.log')
debug_info_handler.setLevel(logging.DEBUG)
debug_info_handler.setFormatter(formatter)
logger.addHandler(debug_info_handler)

# Обработчик для сообщений уровня WARNING и выше
warning_errors_handler = logging.FileHandler('Task_1\warnings_errors.log')
warning_errors_handler.setLevel(logging.WARNING)
warning_errors_handler.setFormatter(formatter)
logger.addHandler(warning_errors_handler)

# Логгирование сообщений различных уровней

logger.debug('Это сообщение уровня DEBUG.')
logger.info('Это сообщение уровня INFO.')
logger.warning('Это сообщение уровня WARNING.')
logger.error('Это сообщение уровня ERROR.')
logger.critical('Это сообщение уровня CRITICAL.')