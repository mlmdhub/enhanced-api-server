import logging
import os

def root():
    current_dir = os.getcwd()
    return os.path.dirname(current_dir)

def init():
    if not os.path.exists(root() + '/data'):
        os.makedirs(root() + '/data')
    if not os.path.exists(root() + '/data/formatted'):
        os.path.exists(root() + '/data/formatted')
    if not os.path.exists(root() + '/data/log'):
        os.makedirs(root() + '/data/log')
    if not os.path.exists(root() + '/data/packages'):
        os.makedirs(root() + '/data/packages')
    if not os.path.exists(root() + '/config'):
        os.makedirs(root() + '/config')

def clear():
    if os.path.exists(root() + '/data'):
        if os.path.exists(root() + '/data/formatted'):
            for file in os.listdir(root() + '/data/formatted'):
                os.remove(root() + '/data/formatted/' + file)
        if os.path.exists(root() + '/data/packages'):
            for file in os.listdir(root() + '/data/packages'):
                os.remove(root() + '/data/packages/' + file)
        if os.path.exists(root() + '/data/log'):
            for file in os.listdir(root() + '/data/log'):
                os.remove(root() + '/data/log/' + file)
    init()

def get_logger(logger_name):
    logger = logging.getLogger(logger_name)
    logger.setLevel(logging.DEBUG)
    file_handler = logging.FileHandler(root()+"/data/log/"+logger_name+'.log')
    file_handler.setLevel(logging.DEBUG)
    formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
    file_handler.setFormatter(formatter)
    logger.addHandler(file_handler)
    return logger

