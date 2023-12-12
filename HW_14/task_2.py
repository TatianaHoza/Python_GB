import logging

logging.basicConfig(filename='log_task_2.log',
                    filemode='w',
                    format='{levelname} - {asctime} - {msg}',
                    style='{',
                    encoding='utf-8',
                    level=logging.INFO)
logger = logging.getLogger('app')


def number(num):
    try:
        if 1 < num and num < 100001:
            if num // num == 1 and num % num == 0 and (num % 2 != 0 or num == 2) and (num % 3 != 0 or num == 3):
                print(f'{num} является простым числом')
        else:
            print(f'{num} является составным числом')

    except ValueError as e:
        logger.error(f"Поймал ошибку {e}")

number(10000000)
number(5)
