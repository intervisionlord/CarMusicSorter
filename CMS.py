import yaml, gettext, locale, os, re, shutil
from sys  import exit
from tkinter import *
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
        else:
            input_dir = ''
    elif param == 'outdir':
        global output_dir
        output_dir = fd.askdirectory(title = _('Set destination directory'))
        if output_dir != '':
            dest_label.config(text = output_dir)
        else:
            output_dir = ''

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
    imagepath = 'data/imgs/main.png'
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

window.iconphoto(True, PhotoImage(file = 'data/imgs/main.png'))
window.geometry('400x200')
window.eval('tk::PlaceWindow . center')
window.title('Car Music Sorter')

# Пути к оформлению
sourceicon = PhotoImage(file = 'data/imgs/20source.png')
desticon = PhotoImage(file = 'data/imgs/20dest.png')

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
source_label_text = _('Input DIR not defined')
dest_label_text = _('Output DIR not defined')

source_label = Label(window, text = source_label_text, justify = LEFT)
source_label.grid(column = 2, row = 0)
dest_label = Label(window, text = dest_label_text, justify = LEFT)
dest_label.grid(column = 2, row = 1)

# 2. Кнопки
source_button = Button(window, text = _('Choose input DIR'), command = lambda: workdirs('indir'), \
image = sourceicon, width = 140, height = 20, compound = 'left').grid(column = 1, row = 0)

dest_button = Button(window, text = _('Choose output DIR'), command = lambda: workdirs('outdir'), \
image = desticon, width = 140, height = 20, compound = 'left').grid(column = 1, row = 1)
window.mainloop()

# Код ниже работает после закрытия окна программы (временно)
# Для простоты тестировния. Его надо распихать по функциям и прикрепить к кнопке.

# 3. !! Оперирование файлами !!
if input_dir == '' or output_dir == '':
    print('Не указана начальная или конечная директория')
    exit()
elif input_dir == output_dir:
    print('Начальная и конечная директории не должны совпадать')
    exit()
try:
    input_dir
except:
    pass
else:
    for path, subdirs, files in os.walk(input_dir):
        for file in files:
# Перегоняем все MP3 в целевую директорию, потом разберемся что с ними делать
# Хотя, лучше искать только нужные (отбрасывать лайвы и ремиксы и перегонять уже без них)
            filtered = re.search('.*mp3', file)
            if filtered != None:
                print(f'{path}/{filtered.group(0)}')
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
    print('Removing Remix: ', file)
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
#    print(new_file) # Вывод для дебага
#    print('OldFile: ', file)
    shutil.move(f'{output_dir}/{file}', f'{output_dir}/{new_file}')
source_file.clear()