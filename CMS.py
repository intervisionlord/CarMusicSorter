import yaml, gettext, locale, os, re, shutil
from sys  import exit
from tkinter import *
from tkinter import ttk

import tkinter.filedialog as fd
input_dir = ''
output_dir = ''
# Определение исходной и целевой директорий
def workdirs(param):
    if param == 'indir':
        global input_dir
        input_dir = fd.askdirectory(title = _('Open source directory'))
        if input_dir != '':
            source_label.config(text = input_dir)
            printlog(_('Input DIR set to: ') + input_dir)
        else:
            input_dir = ''
    elif param == 'outdir':
        global output_dir
        output_dir = fd.askdirectory(title = _('Set destination directory'))
        if output_dir != '':
            dest_label.config(text = output_dir)
            printlog(_('Output DIR set to: ') + output_dir)
        else:
            output_dir = ''
    elif param == 'clear':
        source_label.config(text = _('Input DIR not defined'))
        dest_label.config(text = _('Output DIR not defined'))
        printlog(_('Paths cleared'))
        input_dir = output_dir = ''

def printlog(text):
    progress_log.config(state = NORMAL)
    progress_log.insert(END, f'{text}\n')
    progress_log.config(state = DISABLED)

# Вызов "О программе"
def popup_about(vers):

    # Центровка окна
    main_width = 400
    main_height = 150
    center_x_pos = int(window.winfo_screenwidth() / 2) - main_width
    center_y_pos = int(window.winfo_screenheight() / 2) - main_height

    popup = Toplevel()
    popup.geometry(f'{main_width}x{main_height}+{center_x_pos}+{center_y_pos}')
    #popup.eval('tk::PlaceWindow . center')
    popup.title(_('About'))
    imagepath = 'data/imgs/main.png'
    img = PhotoImage(file = imagepath)
    poplabel1 = Label(popup, image = img)
    poplabel1.grid(sticky = 'W', column = 0, row = 0)

    poplabel2 = Label(popup, text = 'Car Music Sorter\n\n' + _('Version: ') + vers + \
    _('\nAuthor: ') + 'Intervision\nGithub: https://github.com/intervisionlord', justify = LEFT)
    poplabel2.grid(sticky = 'W', column = 1, row = 0)
    # Автор иконок
    poplabel3 = Label(popup, text = _('Icons: ') + 'icon king1 on freeicons.io', justify = LEFT)
    poplabel3.grid(sticky = 'W', column = 1, row = 1)

    popup.grab_set()
    popup.focus_set()
    popup.wait_window()
    popup.mainloop()

def processing():
    if input_dir == '' or output_dir == '':
        printlog(_('Input DIR or Output DIR are not defined!'))
    elif input_dir == output_dir:
        printlog(_('Input DIR and Output DIR must be different!'))
        return
    else:
        for path, subdirs, files in os.walk(input_dir):
            for file in files:
    # Перегоняем все MP3 в целевую директорию, потом разберемся что с ними делать
    # Хотя, лучше искать только нужные (отбрасывать лайвы и ремиксы и перегонять уже без них)
                filtered = re.search('.*mp3', file)
                if filtered != None:
                    printlog(f'{path}/{filtered.group(0)}')
                    shutil.copyfile(f'{path}/{filtered.group(0)}', f'{output_dir}/{filtered.group(0)}')

    source_file = []
    # 3.1. Удаление ремиксов и лайвов
    for files in os.walk(output_dir):
        for file in files[2]:
            try:
                source_file.append(re.search('.*\(.*[Rr]emix.*\).*|.*\(.*[Ll]ive.*\).*', file).group(0))
            except:
                pass
    for file in source_file:
        printlog('Removing Remix: ' + file)
        os.remove(f'{output_dir}/{file}')
    source_file.clear() # Очищаем список

    # 3.2. Готовим список свежепринесенных файлов с вычищенными ремиксами и лайвами
    for files in os.walk(output_dir):
        for file in files[2]:
            try:
                source_file.append(file)
            except:
                pass

    # 3.3. Убираем из имен файлов мусор (номера треков в различном формате)
    for file in source_file:
        new_file = re.sub('^[\d{1,2}\s\-\.]*', '', file)
        shutil.move(f'{output_dir}/{file}', f'{output_dir}/{new_file}')
    source_file.clear()
    printlog(_('Completed!'))

###########################################
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
menu.add_cascade(label = _('Info'), menu = menu_about)

# Элементы меню
menu_about.add_command(label=_('About'), command = lambda: popup_about(vers))

window.config(menu = menu)
# Строим элеметны основного окна и группы
first_group = ttk.LabelFrame(window, text = _('IO Directories'))
first_group.grid(sticky = 'W', column = 0, row = 0, padx = 5, pady = 10, ipadx = 2, ipady = 4)
operation_group = ttk.LabelFrame(window, text = _('Operations'))
operation_group.grid(sticky = 'W', column = 0, row = 1, padx = 5, pady = 10, ipadx = 2, ipady = 4)
progress_group = ttk.LabelFrame(window, text = _('Progress'))
progress_group.grid(sticky = 'WSEN', column = 1, row = 0, padx = 5, pady = 10, ipadx = 0, ipady = 2, rowspan = 2)

# 1. Пояснения
source_label_text = _('Input DIR not defined')
dest_label_text = _('Output DIR not defined')

source_label = ttk.Label(first_group, text = source_label_text, justify = LEFT)
source_label.grid(column = 1, row = 0)
dest_label = Label(first_group, text = dest_label_text, justify = LEFT)
dest_label.grid(column = 1, row = 1)

# 2. Кнопки
source_button = ttk.Button(first_group, text = _('Choose input DIR'), command = lambda: workdirs('indir'), \
image = sourceicon, width = 20, compound = 'left')
source_button.grid(row = 0, ipadx = 2, ipady = 2, padx = 4)

dest_button = ttk.Button(first_group, text = _('Choose output DIR'), command = lambda: workdirs('outdir'), \
image = desticon, width = 20, compound = 'left')
dest_button.grid(row = 1, ipadx = 2, ipady = 2, padx = 4)

launch_button = ttk.Button(operation_group, text = _('Process'), command = processing, \
image = launchicon, width = 20, compound = 'left')
launch_button.grid(column = 0, row = 2, ipadx = 2, ipady = 2, padx = 4)

calear_button = ttk.Button(operation_group, text = _('Clear'), command = lambda: workdirs('clear'), \
image = clearicon, width = 20, compound = 'left')
calear_button.grid(column = 1, row = 2, ipadx = 2, ipady = 2, padx = 4)

# 4. Лог и прогресс
progress_log = Text(progress_group, state = DISABLED, relief = FLAT, width = 31, height = 10)
progress_log.grid(ipadx = 2, ipady = 2, padx = 4)
window.mainloop()