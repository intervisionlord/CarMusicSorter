from f_getconfig import getconfig


def test_getconfig():
    """Проверка, что конфиг не пустой."""
    assert getconfig() is not None, 'Config is empty'