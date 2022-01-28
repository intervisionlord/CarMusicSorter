"""Окно с описанием."""
import webbrowser
from tkinter import Toplevel, PhotoImage, Label


def goto_url(url):
    """Переходит по предоставленной ссылке."""
    webbrowser.open_new(url)


def popup_about(window, vers: str) -> None:
    """Открывает окно 'О программе'."""
# Центровка окна
    main_width = 350
    main_height = 150
    center_x_pos = int(window.winfo_screenwidth() / 2) - main_width
    center_y_pos = int(window.winfo_screenheight() / 2) - main_height

    popup = Toplevel()
    popup.geometry(f'{main_width}x{main_height}+{center_x_pos}+{center_y_pos}')
    popup.title(_('About'))
    imagepath = 'data/imgs/main.png'
    img = PhotoImage(file = imagepath)
    poplabel1 = Label(popup, image = img)
    poplabel1.grid(sticky = 'W', column = 0, row = 0, rowspan = 3)

    progname = 'Car Music Sorter'
    name_vers_str = _('Version: ') + vers
    prog_author = _('\nAuthor: ') + 'Intervision'
    author_github = 'https://github.com/intervisionlord'
    poplabel_progname = Label(popup,
                              text = progname,
                              justify = 'left')
    poplabel_progname.config(font = ('16'))
    poplabel_progname.grid(column = 1, row = 0)
    poplabel_maindesc = Label(popup,
                              text = name_vers_str + prog_author,
                              justify = 'left')
    poplabel_maindesc.grid(sticky = 'W', column = 1, row = 1)

    poplabel_giturl = Label(popup,
                            text = author_github,
                            justify = 'left',
                            fg = 'blue',
                            cursor = 'hand2')
    poplabel_giturl.bind('<Button-1>',
                         lambda u: goto_url(author_github))
    poplabel_giturl.grid(sticky = 'W', column = 1, row = 2)
# Автор иконок
    icons_author = _('Icons: ') + 'icon king1 ' + _('on') + ' freeicons.io'
    poplabel_icons = Label(popup, text = icons_author, justify = 'left')
    poplabel_icons.grid(sticky = 'W', column = 1, row = 3)

    popup.grab_set()
    popup.focus_set()
    popup.wait_window()
