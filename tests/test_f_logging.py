"""Тестирование механизмов логирования."""
import yaml
from f_logging import check_logging_opt


def test_check_logging_opt_true():
    """Проверка параметров логирования.

    Логирование True.
    """
    conffile = open('./conf/main.yml', 'r')
    config: dict[str, dict[str, str]] = yaml.full_load(conffile)
    conffile.close()
    config['settings']['logging'] = str(True)
    with open(r'conf/main.yml', 'w') as file:
        yaml.dump(config, file)
    assert check_logging_opt() is True, ('Check with TRUE: '
                                         'Return does not match '
                                         'expected value')


def test_check_logging_opt_false():
    """Проверка параметров логирования.

    Логирование False.
    """
    conffile = open('./conf/main.yml', 'r')
    config: dict[str, dict[str, str]] = yaml.full_load(conffile)
    conffile.close()
    config['settings']['logging'] = str(False)
    with open(r'conf/main.yml', 'w') as file:
        yaml.dump(config, file)
    assert check_logging_opt() is False, ('Check with FALSE: '
                                          'Return does not match '
                                          'expected value')


def test_check_logging_opt_none():
    """Проверка параметров логирования.

    Логирование не определено в конфиге.
    """
    conffile = open('./conf/main.yml', 'r')
    config: dict[str, dict[str, str]] = yaml.full_load(conffile)
    conffile.close()
    config['settings']['logging'] = ''
    with open(r'conf/main.yml', 'w') as file:
        yaml.dump(config, file)
    assert check_logging_opt() == 'ERR', ('Check with FALSE: '
                                          'Return does not match '
                                          'expected value')
    config['settings']['logging'] = str(False)
    with open(r'conf/main.yml', 'w') as file:
        yaml.dump(config, file)
