import pytest
from pathlib import Path
from CMS import getconfig, path_short


def test_getconfig_locale_not_null():
    """Проверка заполненности локали в конфиге."""
    assert getconfig()['settings']['locale'] is not None, 'Locale is not set'


@pytest.mark.parametrize('testpath, shortlen, expected',
                         [
                             ('test1/test2/test3', 1, 'test3'),
                             ('megapath/azaza/ololo', 2, 'azaza/ololo'),
                             ('t1/t2/t3', 3, 't1/t2/t3')
                             ])
def test_path_short(testpath, shortlen, expected):
    """Проверка сокращения путей."""
    assert path_short(testpath,
                      shortlen) == Path(expected), ('Short path is not valid')
