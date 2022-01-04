"""Отрисовка окна настроек."""
import os
from tkinter import Toplevel, LabelFrame, PhotoImage, Label
from tkinter.ttk import Combobox, Button

POPUP_WIDTH: int = 400
POPUP_HEIGHT: int = 200


def check_langs():
    """Проверяет какие локализации доступны."""
    langs: list = os.listdir('l10n')
    return langs


def apply():
    """Применяет изменения и вносит их в конфиг."""
    pass


def popup_settings():
    """Открывает окно 'Настройки'."""
    popup = Toplevel()
    launchicon = PhotoImage(file = 'data/imgs/20ok.png')
    center_x_pos = int(popup.winfo_screenwidth() / 2) - POPUP_WIDTH
    center_y_pos = int(popup.winfo_screenheight() / 2) - POPUP_HEIGHT

    popup.geometry(f'{POPUP_WIDTH}x{POPUP_HEIGHT}+'
                   f'{center_x_pos}+{center_y_pos}')
    popup.title(_('Settings'))
    frame_settings = LabelFrame(popup, text = _('Settings'))
    frame_settings.grid(sticky = 'NWSE', column = 0, row = 0)

    lang_vars = Combobox(frame_settings, values = check_langs(), width = 4)
    lang_vars.grid(column = 0, row = 0)

    apply_button = Button(popup, text = _('Apply'),
                          width = 20, compound = 'left',
                          image = launchicon, command = apply)
    apply_button.grid(column = 0, row = 1)

    popup.grab_set()
    popup.focus_set()
    popup.wait_window()
