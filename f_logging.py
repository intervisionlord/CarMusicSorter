"""Определяет логирование процесса."""
import os
import codecs
from typing import Union
from f_getconfig import getconfig
from datetime import datetime

timestamp = datetime.now().strftime("%d/%m/%Y, %H:%M:%S")

opt_logname: str = getconfig()['settings']['logname']


def check_logging_opt() -> Union[bool, str]:
    """Проверяет параметр логирования в конфиге."""
    opt_logging: str = getconfig()['settings']['logging']
    if opt_logging == 'True':
        return True
    elif opt_logging == 'False':
        return False
    else:
        return 'ERR'


def writelog(logmsg: str) -> None:
    """Пишет лог, если так указано в конфиге."""
    if os.path.isfile(opt_logname) is False:
        pass
    elif check_logging_opt() is True:
        if logmsg == 'init':
            with codecs.open(opt_logname, 'a', 'utf-8') as log:
                log.write(f'\n\n{timestamp} - Start Program\n----------\n')
        else:
            with codecs.open(opt_logname, 'a', 'utf-8') as log:
                log.write(f'{timestamp} - {logmsg}\n')
    elif check_logging_opt() == 'ERR':
        with codecs.open(opt_logname, 'a', 'utf-8') as log:
            log.write(f'{timestamp} - Logging config error!\n')
