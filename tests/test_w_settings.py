"""Тестирование функционала настроек."""
import os
from pathlib import Path
from w_settings import check_langs, current_lang


def test_getconfig_locales_count():
    """Тестирует, кол-во локализаций.

    Проверяет, что кол-во файлов соответствует тому,
    что видит программа в итоге.
    """
    nominal_count = len(os.listdir(Path('l10n')))
    assert nominal_count == len(check_langs()), ('Folders with'
                                                 'localisations does not equal'
                                                 'localisations list')


def test_current_lang():
    """Тестирует невыход за значения."""
    assert current_lang() <= len(check_langs())
