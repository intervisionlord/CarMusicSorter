"""Определяет логирование процесса."""
import os

from f_getconfig import getconfig

opt_logging = getconfig()['settings']['logging']
opt_logname = getconfig()['settings']['logname']


def check_logging_opt():
    """Проверяет параметр логирования в конфиге."""
    if opt_logging is True:
        return True
    elif opt_logging is False:
        return False
    else:
        return 'ERR'


def writelog(logmsg):
    """Пишет лог, если так указано в конфиге."""
    if os.path.isfile(opt_logname) is False:
        with open(opt_logname, 'w') as log:
            pass
    if check_logging_opt() is True:
        with open(opt_logname, 'a') as log:
            log.write(f'{logmsg}\n')
