import logging

logging.basicConfig(level=logging.DEBUG,
                    filename = 'logfile.txt',
                    format='%(asctime)s.%(msecs)03d - %(levelname)s: %(message)s',
                    datefmt='%Y-%m-%dT%H:%M:%S')

logging.critical('BANNNGGGG!!!!')
logging.critical('BANNNGGGG!!!!')
logging.debug('Dit is OK')
logging.info('Hier ben ik')
logging.warning('Dit gaat bijna fout')
logging.error('Fout')
logging.critical('BANNNGGGG!!!!')
