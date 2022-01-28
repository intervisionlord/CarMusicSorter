"""Отрисовка окна настроек."""
import os
import yaml
import re
from tkinter import BooleanVar
from tkinter import Toplevel, LabelFrame, PhotoImage, Label, messagebox
from tkinter.ttk import Combobox, Button, Checkbutton
from f_getconfig import getconfig

POPUP_WIDTH: int = 160
POPUP_HEIGHT: int = 110


def check_langs() -> list[str]:
    """Проверяет какие локализации доступны."""
    langs: list[str] = os.listdir('l10n')
    return langs


def apply(lang: str, popup, log_var: bool) -> None:
    """Применяет изменения и вносит их в конфиг."""
    conffile = open('conf/main.yml', 'r')
    config: dict[str, dict[str, str]] = yaml.full_load(conffile)
    conffile.close()
    config['settings']['locale'] = lang
    config['settings']['logging'] = re.sub(r'\'', '', str(log_var))
    with open(r'conf/main.yml', 'w') as file:
        yaml.dump(config, file)
    messagebox.showinfo(_('Information'),
                        _('Settings will be applied after programm restart.'))
    popup.destroy()


def current_lang() -> int:
    """Определяет индекс текущего языка для выпадающего списка."""
    return check_langs().index(getconfig()['settings']['locale'])


def popup_settings() -> None:
    """Открывает окно 'Настройки'."""
    popup = Toplevel()
    log_var = BooleanVar()
    launchicon = PhotoImage(file = 'data/imgs/20ok.png')
    center_x_pos = int(popup.winfo_screenwidth() / 2) - POPUP_WIDTH
    center_y_pos = int(popup.winfo_screenheight() / 2) - POPUP_HEIGHT

    popup.geometry(f'{POPUP_WIDTH}x{POPUP_HEIGHT}+'
                   f'{center_x_pos}+{center_y_pos}')
    popup.title(_('Settings'))
    popup.resizable(False, False)
    frame_settings = LabelFrame(popup, text = _('Settings'))
    frame_settings.grid(sticky = 'NWSE', column = 0, row = 0,
                        ipadx = 5, padx = 5, pady = 5)

    lang_label = Label(frame_settings, text = _('Localisation'))
    lang_label.grid(column = 0, row = 0, ipadx = 5)

    logs_label = Label(frame_settings, text = _('Logging'))
    logs_label.grid(column = 0, row = 1, ipadx = 5)

    lang_vars = Combobox(frame_settings, state = 'readonly',
                         values = check_langs(), width = 4)
    lang_vars.current(current_lang())
    lang_vars.grid(column = 1, row = 0)
    log_settings = Checkbutton(frame_settings,
                               variable = log_var, onvalue = True,
                               offvalue = False)

    log_settings.grid(column = 1, row = 1)

    if getconfig()['settings']['logging'] == 'True':
        log_var.set(True)
    elif getconfig()['settings']['logging'] == 'False':
        log_var.set(False)

    apply_button = Button(popup, text = _('Apply'), width = 20,
                          compound = 'left', image = launchicon,
                          command = lambda: apply(
                                                  lang_vars.get(),
                                                  popup, log_var.get()
                                                  )
                          )
    apply_button.grid(column = 0, row = 1)

    popup.grab_set()
    popup.focus_set()
    popup.wait_window()

if __name__ == '__main__':
    print(bool(getconfig()['settings']['logging']))
    print(getconfig()['settings']['logging'])