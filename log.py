import logging
import os


def get_logger_by_account(account_name):
    if not os.path.exists('logs'):
        os.makedirs('logs')

    filename = 'logs/' + account_name + '.log'

    logging.basicConfig(
        level=logging.INFO,
        format="%(asctime)s [%(levelname)s] - %(message)s",
        handlers=[
            logging.FileHandler(filename),
            logging.StreamHandler()
        ]
    )

    return logging.getLogger(account_name)
