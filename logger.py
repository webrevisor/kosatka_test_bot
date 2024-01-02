import logging
import config

# Настройки логирования
logging.basicConfig(
    level=logging.INFO,
    format=config.LOG_FORMAT,
    handlers=[
        logging.FileHandler(config.LOG_FILE),   # Логирование в файл
        logging.StreamHandler()                 # Логирование в стандартный вывод
    ]
)

logger = logging.getLogger(__name__)
