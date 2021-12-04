import yaml, gettext, locale
from sys  import exit
import functions as func
from tkinter import *

try:
    conffile = open('conf/main.yml', 'r')
except:
    errorcode = 'Config was not found'
    exit(errorcode)
finally:
    config = yaml.full_load(conffile)
    conffile.close()

vers = config['core']['version']
locale = config['settings']['locale']

gettext.translation('CarMusicSorter', localedir='l10n', languages=[locale]).install()

window = Tk()
window.iconphoto(True, PhotoImage(file = 'data/assets/imgs/main.png'))
window.geometry('400x200')
window.title(f'Car Music Sorter v.: {vers}')

main_label = Label(window, text = _('Choose directory where tracks were taken from')).grid(column = 0, row = 0)
go_button = Button(window, text = _('Begin!'), command = func.on_click('go')).grid(column = 1, row = 0)

window.mainloop()