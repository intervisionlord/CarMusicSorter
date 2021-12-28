"""Отрисовка окна настроек."""
import os
from tkinter import Toplevel, LabelFrame
from tkinter.ttk import Combobox

POPUP_WIDTH: int = 400
POPUP_HEIGHT: int = 200


def check_langs():
    """Проверяет какие локализации доступны."""
    langs = os.listdir('l10n')
    return langs


def popup_settings():
    """Открывает окно 'Настройки'."""
    popup = Toplevel()

    center_x_pos = int(popup.winfo_screenwidth() / 2) - POPUP_WIDTH
    center_y_pos = int(popup.winfo_screenheight() / 2) - POPUP_HEIGHT

    popup.geometry(f'{POPUP_WIDTH}x{POPUP_HEIGHT}+'
                   f'{center_x_pos}+{center_y_pos}')
    popup.title(_('Settings'))
    frameSettings = LabelFrame(popup, text = _('Language'))
    frameSettings.grid(sticky = 'NWSE', column = 0, row = 0)

    langVars = Combobox(frameSettings, values = check_langs(), width = 4)
    langVars.grid(column = 0, row = 0)

    popup.grab_set()
    popup.focus_set()
    popup.wait_window()
