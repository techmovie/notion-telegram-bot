import logging
import os

def setup_logger():
    logs_directory = 'logs'
    if not os.path.exists(logs_directory):
        os.makedirs(logs_directory)
    log_file_path = os.path.join(logs_directory, 'bot.log')

    logging.basicConfig(
        level=logging.INFO,
        format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
        handlers=[
            logging.FileHandler(log_file_path),
            logging.StreamHandler()
        ]
    )

    logger = logging.getLogger(__name__)
    return logger

logger = setup_logger()
