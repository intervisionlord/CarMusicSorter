"""Функция работы с файлом конфигурации."""
import yaml


def getconfig():
    """Определяет наличие конфига и загружает его."""
    try:
        conffile = open('conf/main.yml', 'r')
    except IOError:  # FIXME: Убрать exit() в результате эксепшена
        exit(messagebox.showerror('ERROR', _('Config file not found')))

    config = yaml.full_load(conffile)
    conffile.close()
    return config
