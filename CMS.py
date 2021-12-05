import yaml, gettext, locale, os
import functions.functions as func
from sys  import exit
from tkinter import *
from tkinter import Menu, messagebox

# Проверяем конфиг
try:
    conffile = open('conf/main.yml', 'r')
except:
    exit(messagebox.showerror('ERROR', 'Config file not found'))

config = yaml.full_load(conffile)
conffile.close()

# Вводим основные переменные
vers = config['core']['version']
locale = config['settings']['locale']
# Локализация
gettext.translation('CarMusicSorter', localedir='l10n', languages=[locale]).install()

# Рисуем окно
window = Tk()
window.iconphoto(True, PhotoImage(file = 'data/assets/imgs/main.png'))
window.geometry('400x200')
window.title(f'Car Music Sorter v.: {vers}')

# Основное меню
menu = Menu(window)
menu_about = Menu(menu, tearoff = 0)
menu.add_cascade(label = _('Info'), menu = menu_about)

# Элементы меню
menu_about.add_command(label=_('About'), command = lambda: func.popup_about(vers))

window.config(menu = menu)

# Строим элеметны основного окна
main_label = Label(window, text = _('Choose directory where tracks were taken from')).grid(column = 0, row = 0)

# Главная кнопка ;)
go_button = Button(window, text = _('Begin!'), command = lambda: func.on_click('go')).grid(column = 1, row = 0)

window.mainloop()