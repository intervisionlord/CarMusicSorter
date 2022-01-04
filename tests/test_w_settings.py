import os
import pytest
from pathlib import Path
from w_settings import check_langs

def test_getconfig_locales_count():
    nominal_count = len(os.listdir(Path('l10n')))
    assert nominal_count == len(check_langs()), 'Folders with localisations does not equal localisations list'