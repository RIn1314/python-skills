# -*- coding: utf-8 -*-
import logging
import datetime


class My_log():
    ''' 日志输出 '''
    def __init__(self, file_name):
        FORMAT = '%(asctime)s %(filename)s[line:%(lineno)d] <%(levelname)s> %(message)s'
        logging.basicConfig(level=logging.INFO,
                            format=FORMAT,
                            filename=file_name,
                            filemode='a')  # 打印到控制台
        console = logging.StreamHandler()
        console.setLevel(logging.INFO)
        formatter = logging.Formatter(FORMAT)
        console.setFormatter(formatter)
        logging.getLogger().addHandler(console)


def log_print():
    # My_log(r'.\log_file.txt')
    My_log(r'.\%slog.txt' % (datetime.datetime.now().strftime('%Y-%m-%d')))
    logging.info('开始打印日志')
    logging.debug('这是debug')
    logging.error('这是error')
    logging.warning('这是warning')


if __name__ == '__main__':
    log_print()
