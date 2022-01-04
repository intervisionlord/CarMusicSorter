"""Отрисовка окна настроек."""
import os
import yaml
from tkinter import Toplevel, LabelFrame, PhotoImage, Label, messagebox
from tkinter.ttk import Combobox, Button

POPUP_WIDTH: int = 180
POPUP_HEIGHT: int = 90


def check_langs():
    """Проверяет какие локализации доступны."""
    langs: list = os.listdir('l10n')
    return langs


def apply(lang, popup):
    """Применяет изменения и вносит их в конфиг."""
    conffile = open('conf/main.yml', 'r')
    config = yaml.full_load(conffile)
    conffile.close()
    config['settings']['locale'] = lang
    with open(r'conf/main.yml', 'w') as file:
        yaml.dump(config, file)
    messagebox.showinfo(_('Information'),
                        _('Settings will be applied after programm restart.'))
    popup.destroy()


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
    frame_settings.grid(sticky = 'NWSE', column = 0, row = 0,
                        ipadx = 5, padx = 5, pady = 5)

    lang_label = Label(frame_settings, text = _('Localisation'))
    lang_label.grid(column = 0, row = 0, ipadx = 5)

    lang_vars = Combobox(frame_settings, state = 'readonly',
                         values = check_langs(), width = 4)
    lang_vars.grid(column = 1, row = 0)

    apply_button = Button(popup, text = _('Apply'),
                          width = 20, compound = 'left',
                          image = launchicon,
                          command = lambda: apply(lang_vars.get(), popup))
    apply_button.grid(column = 0, row = 1)

    popup.grab_set()
    popup.focus_set()
    popup.wait_window()
