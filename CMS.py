import yaml
import functions as func
from tkinter import *

try:
    conffile = open('conf/main.yml', 'r')
except:
    errorcode = 'Конфиг не найден'
    exit(errorcode)

config = yaml.full_load(conffile)
conffile.close()

vers = config['core']['version']

window = Tk()
window.iconphoto(True, PhotoImage(file = 'data/assets/icons/main.png'))
window.geometry('400x200')
window.title(f'Car Music Sorter v.: {vers}')

main_label = Label(window, text = 'Выберите директорию, в которой необходимо произвести\nпреобразование').grid(column = 0, row = 0)
go_button = Button(window, text = 'Начать!', command = func.on_click('go')).grid(column = 1, row = 0)

window.mainloop()