import yaml, gettext, locale, os
from sys  import exit
from tkinter import *
import tkinter.filedialog as fd

# Определение исходной и целевой директорий
def workdirs(param):
    if param == 'indir':
        input_dir = fd.askdirectory(title = _('Open source directory'))
        if input_dir != '':
            source_label.config(text = _('Source dir is: ') + input_dir)
    elif param == 'outdir':
        output_dir = fd.askdirectory(title = _('Set destination directory'))
        if output_dir != '':
            dest_label.config(text = _('Destination dir is: ') + output_dir)

# Вызов "О программе"
def popup_about(vers):

    # Центровка окна
    main_width = 380
    main_height = 150
    center_x_pos = int(window.winfo_screenwidth() / 2) - main_width
    center_y_pos = int(window.winfo_screenheight() / 2) - main_height

    popup = Toplevel()
    popup.geometry(f'{main_width}x{main_height}+{center_x_pos}+{center_y_pos}')
    #popup.eval('tk::PlaceWindow . center')
    popup.title(_('About'))
    imagepath = 'data/assets/imgs/main.png'
    img = PhotoImage(file = imagepath)
    poplabel1 = Label(popup, image = img).grid(column = 0, row = 0)
    poplabel2 = Label(popup, text = 'Car Music Sorter\n\n' + _('Version: ') + vers + \
    _('\nAuthor: ') + 'Intervision\nGithub: https://github.com/intervisionlord', justify = LEFT).grid(column = 1, row = 0)
    popup.grab_set()
    popup.focus_set()
    popup.wait_window()
    popup.mainloop()

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
window.eval('tk::PlaceWindow . center')
window.title(f'Car Music Sorter v.: {vers}')

# Пути к оформлению
sourceicon = PhotoImage(file = 'data/assets/imgs/20source.png')
desticon = PhotoImage(file = 'data/assets/imgs/20dest.png')

# Основное меню
menu = Menu(window)
menu_about = Menu(menu, tearoff = 0)
menu.add_cascade(label = _('Info'), menu = menu_about)

# Элементы меню
menu_about.add_command(label=_('About'), command = lambda: popup_about(vers))

window.config(menu = menu)
# _('Choose directory where tracks were taken from')
# Строим элеметны основного окна
first_step = Label(window, text =  '1. ', font = 'bold').grid(column = 0, row = 0)
second_step = Label(window, text = '2. ', font = 'bold').grid(column = 0, row = 1)

# 1. Пояснения
source_label_text = _('Choose input directory')
dest_label_text = _('Choose output directory')

source_label = Label(window, text = source_label_text, justify = LEFT)
source_label.grid(column = 2, row = 0)
dest_label = Label(window, text = dest_label_text, justify = LEFT)
dest_label.grid(column = 2, row = 1)

# 2. Кнопки
source_button = Button(window, text = _('Browse'), command = lambda: workdirs('indir'), \
image = sourceicon, width = 80, height = 20, compound = 'left').grid(column = 1, row = 0)

dest_button = Button(window, text = _('Browse'), command = lambda: workdirs('outdir'), \
image = desticon, width = 80, height = 20, compound = 'left').grid(column = 1, row = 1)
window.mainloop()