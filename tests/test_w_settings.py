"""Тестирование функционала настроек."""
import os
from pathlib import Path
from w_settings import check_langs


def test_getconfig_locales_count():
    """Тестирует, кол-во локализаций.

    Проверяет, что кол-во файлов соответствует тому,
    что видит программа в итоге.
    """
    nominal_count = len(os.listdir(Path('l10n')))
    assert nominal_count == len(check_langs()), ('Folders with'
                                                 'localisations does not equal'
                                                 'localisations list')
