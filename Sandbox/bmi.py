import logging
import os


log_filename = 'mijnlog.log'
os.remove(log_filename)
logging.basicConfig(filename = log_filename, # or to a file 'example.log',
                    level = logging.ERROR,  # Logging levels: DEBUG, INFO, WARNING, ERROR, CRITICAL
                    format = '%(levelname)s - %(message)s')

def calculate_bmi(weight, height, correctie_factor = 0.9):
    if height < 1 or height > 2.5:
        logging.error(f'invalid argument: height={height}')
    bmi = (weight / height ** 2) * correctie_factor
    # print('> ', weight, height, correctie_factor, bmi)
    logging.debug(f'{weight}, {height}, {correctie_factor}, {bmi}')
    return bmi


print(calculate_bmi(100, 1.80))
