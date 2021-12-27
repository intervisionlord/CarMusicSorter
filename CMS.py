"""Car Music Sorter."""
import yaml
import gettext
import os
import re
import shutil

from sys import exit
from tkinter import Tk, PhotoImage, Menu, LabelFrame
from tkinter import Text, Toplevel, messagebox
from tkinter.ttk import Button, Label, Progressbar
from pathlib import Path

import tkinter.filedialog as fd
input_dir = ''
output_dir = ''

source_file = []


# BEGIN FUNCTIONS #
# FIXME: Вынести по возможности в отдельные файлы
# Определение исходной и целевой директорий
def workdirs(param):
    """Открывает диалог выбора директории."""
    if param == 'indir':
        global input_dir
        input_dir = fd.askdirectory(title = _('Open source directory'))
        if input_dir != '':
            source_label.config(text = f'...{path_short(input_dir, 2)}')
            printlog(_('Input DIR set to: ') + input_dir)
        else:
            input_dir = ''
    elif param == 'outdir':
        global output_dir
        output_dir = fd.askdirectory(title = _('Set destination directory'))
        if output_dir != '':
            dest_label.config(text = f'...{path_short(output_dir, 2)}')
            printlog(_('Output DIR set to: ') + output_dir)
        else:
            output_dir = ''
    elif param == 'clear':
        source_label.config(text = _('Input DIR not defined'))
        dest_label.config(text = _('Output DIR not defined'))
        printlog(_('Paths cleared'))
        main_progressbar['value'] = 0
        input_dir = output_dir = ''


def printlog(text):
    """Пишет лог операции в TextBox."""
    progress_log.config(state = 'normal')
    progress_log.insert('end', f'{text}\n')
    progress_log.config(state = 'disabled')
    progress_log.see('end')


def path_short(path_string, len):
    """Сокращает путь для корректного отображения в лейбле."""
    return Path(*Path(path_string).parts[-len:])


# Вызов "О программе"
def popup_about(vers):
    """Открывает окно 'О программе'."""
    # Центровка окна
    main_width = 400
    main_height = 150
    center_x_pos = int(window.winfo_screenwidth() / 2) - main_width
    center_y_pos = int(window.winfo_screenheight() / 2) - main_height

    popup = Toplevel()
    popup.geometry(f'{main_width}x{main_height}+{center_x_pos}+{center_y_pos}')
    popup.title(_('About'))
    imagepath = 'data/imgs/main.png'
    img = PhotoImage(file = imagepath)
    poplabel1 = Label(popup, image = img)
    poplabel1.grid(sticky = 'W', column = 0, row = 0, rowspan = 2)

    name_vers_str = 'Car Music Sorter\n\n' + _('Version: ') + vers
    author_github = 'https://github.com/intervisionlord'
    prog_author = _('\nAuthor: ') + 'Intervision\nGithub: ' + author_github
    poplabel_maindesc = Label(popup,
                              text = name_vers_str + prog_author,
                              justify = 'left')
    poplabel_maindesc.grid(sticky = 'W', column = 1, row = 0)
    # Автор иконок
    icons_author = _('Icons: ') + 'icon king1 ' + _('on') + ' freeicons.io'
    poplabel_icons = Label(popup, text = icons_author, justify = 'left')
    poplabel_icons.grid(sticky = 'W', column = 1, row = 1)

    popup.grab_set()
    popup.focus_set()
    popup.wait_window()


# Основные операции
def check_paths():
    """Проверяет, что все пути заданы корректно и запускает копирование."""
    if input_dir == '' or output_dir == '':
        printlog(_('Input DIR or Output DIR are not defined!'))
    elif input_dir == output_dir:
        printlog(_('Input DIR and Output DIR must be different!'))
        return
    else:
        for path, subdirs, files in os.walk(input_dir):
            for file in files:
                # Перегоняем все MP3 в целевую директорию,
                # потом разберемся что с ними делать
                # Хотя, лучше искать только нужные (отбрасывать лайвы
                # и ремиксы и перегонять уже без них)
                filtered = re.search('.*mp3', file)
                if filtered is not None:
                    source_file.append(f'{path}/{filtered.group(0)}')
    main_progressbar['maximum'] = len(source_file)
    for files in source_file:
        maincopy(files, output_dir)
    source_file.clear()


def processing():
    """Удаляет ремиксы и лайвы."""
    check_paths()
# Удаление ремиксов и лайвов
    liveregexp = r'.*\(.*[Rr]emix.*\).*|.*\(.*[Ll]ive.*\).*'
    for files in os.walk(output_dir):
        for file in files[2]:
            try:
                source_file.append(re.search(liveregexp, file).group(0))
            except Exception:
                pass
    for file in source_file:
        printlog('Removing Remix: ' + file)
        os.remove(f'{output_dir}/{file}')
        main_progressbar['value'] = main_progressbar['value'] + 1
        window.update_idletasks()
    source_file.clear()  # Очищаем список
    polish_filenames()


def polish_filenames():
    """Удаляет из имен треков мусор."""
# Готовим список свежепринесенных файлов с вычищенными ремиксами и лайвами
    for files in os.walk(output_dir):
        for file in files[2]:
            try:
                source_file.append(file)
            except Exception:
                pass

    # Убираем из имен файлов мусор (номера треков в различном формате)
    main_progressbar['maximum'] = (main_progressbar['maximum'] +
                                   len(source_file))
    trashregexp = r'^[\d{1,2}\s\-\.]*'
    for file in source_file:
        new_file = re.sub(trashregexp, '', file)
        shutil.move(f'{output_dir}/{file}', f'{output_dir}/{new_file}')
        main_progressbar['value'] = main_progressbar['value'] + 1
        window.update_idletasks()
    source_file.clear()
    printlog(_('Completed!'))


# Копируем файлы
def maincopy(files, output_dir):
    """Копирует файлы."""
    printlog(f'{files}')
    filename = str.split(files, '/')
    printlog(filename[-1])
    shutil.copyfile(f'{files}', f'{output_dir}/{filename[-1]}')
    main_progressbar['value'] = main_progressbar['value'] + 1
    window.update_idletasks()
# TODO: Вывести запись логов в файл, убрать бокс с логом из окна.
# END FUNCTIONS #


# Проверяем конфиг
try:
    conffile = open('conf/main.yml', 'r')
except IOError:  # FIXME: Убрать exit() в результате эксепшена
    exit(messagebox.showerror('ERROR', 'Config file not found'))

config = yaml.full_load(conffile)
conffile.close()

# Вводим основные переменные
vers = config['core']['version']
langcode = config['settings']['locale']
# Локализация
gettext.translation('CarMusicSorter', localedir='l10n',
                    languages=[langcode]).install()
# Рисуем окно
window = Tk()

window.iconphoto(True, PhotoImage(file = 'data/imgs/main.png'))
window.geometry('650x300')
window.eval('tk::PlaceWindow . center')
window.title('Car Music Sorter')

# Пути к оформлению
sourceicon = PhotoImage(file = 'data/imgs/20source.png')
desticon = PhotoImage(file = 'data/imgs/20dest.png')
launchicon = PhotoImage(file = 'data/imgs/20ok.png')
clearicon = PhotoImage(file = 'data/imgs/20clear.png')

# Основное меню
menu = Menu(window)
menu_about = Menu(menu, tearoff = 0)
menu_file = Menu(menu, tearoff = 0)
menu.add_cascade(label = _('File'), menu = menu_file)
menu.add_cascade(label = _('Info'), menu = menu_about)
# Элементы меню
menu_about.add_command(label = _('About'), command = lambda: popup_about(vers))

menu_file.add_command(label = _('Input Dir'),
                      command = lambda: workdirs('indir'))
menu_file.add_command(label = _('Output Dir'),
                      command = lambda: workdirs('outdirs'))

window.config(menu = menu)
# Строим элеметны основного окна и группы
first_group = LabelFrame(window, text = _('IO Directories'))

first_group.grid(sticky = 'WE', column = 0, row = 0, padx = 5, pady = 10,
                 ipadx = 2, ipady = 4)

operation_group = LabelFrame(window, text = _('Operations'))
operation_group.grid(sticky = 'WE', column = 0, row = 1, padx = 5, pady = 10,
                     ipadx = 2, ipady = 4)

progress_group = LabelFrame(window, text = _('Progress'))
progress_group.grid(sticky = 'WSEN', column = 1, row = 0, padx = 5, pady = 10,
                    ipadx = 0, ipady = 2, rowspan = 2)

# Прогрессбар
main_progressbar = Progressbar(progress_group, length = 255, value = 0,
                               orient = 'horizontal', mode = 'determinate')
main_progressbar.grid(pady = 4, column = 0, row = 1)

# Поясняющие лейблы
source_label_text = _('Input DIR not defined')
dest_label_text = _('Output DIR not defined')

source_label = Label(first_group, text = source_label_text, justify = 'left')
source_label.grid(column = 1, row = 0)
dest_label = Label(first_group, text = dest_label_text, justify = 'left')
dest_label.grid(column = 1, row = 1)

# Кнопки
source_button = Button(first_group, text = _('Input Dir'),
                       command = lambda: workdirs('indir'), image = sourceicon,
                       width = 20, compound = 'left')
source_button.grid(row = 0, ipadx = 2, ipady = 2, padx = 4)

dest_button = Button(first_group, text = _('Output Dir'),
                     command = lambda: workdirs('outdir'), image = desticon,
                     width = 20, compound = 'left')
dest_button.grid(row = 1, ipadx = 2, ipady = 2, padx = 4)

launch_button = Button(operation_group, text = _('Process'),
                       command = processing, image = launchicon,
                       width = 20, compound = 'left')
launch_button.grid(column = 0, row = 2, ipadx = 2, ipady = 2, padx = 4)

clear_button = Button(operation_group, text = _('Clear'),
                      command = lambda: workdirs('clear'), image = clearicon,
                      width = 20, compound = 'left')

clear_button.grid(column = 1, row = 2, ipadx = 2, ipady = 2, padx = 4)

# Лог и прогресс
progress_log = Text(progress_group, state = 'disabled', relief = 'flat',
                    width = 31, height = 10)
progress_log.grid(ipadx = 2, ipady = 2, padx = 4, column = 0, row = 0)

window.mainloop()
