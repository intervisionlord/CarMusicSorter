from tkinter import *
from pathlib import Path
def on_click(cmd):
    if cmd == 'go':
        return 'test'
    else:
        return _('Begin!')

def popup_about(vers):
    popup = Toplevel()
    popup.geometry('380x150')
    popup.title(_('About'))
    imagepath = Path(Path(__file__).parents[1], 'data/assets/imgs/main.png')
    img = PhotoImage(file = imagepath)
    poplabel1 = Label(popup, image = img).grid(column = 0, row = 0)
    poplabel2 = Label(popup, text = 'Car Music Sorter\n\n' + _('Version: ') + vers + \
    _('\nAuthor: ') + 'Intervision\nGithub: https://github.com/intervisionlord', justify=LEFT).grid(column = 1, row = 0)
    popup.mainloop()

if __name__ == '__main__':
    imagepath = Path(Path(__file__).parents[1], 'data/assets/imgs/main.png')
#    imagepath = Path(os.getcwd()).parent + '/data'
    popup_about(0)