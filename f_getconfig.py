"""Функция работы с файлом конфигурации."""
import yaml


def getconfig() -> dict[str, dict[str, str]]:
    """Определяет наличие конфига и загружает его.

    Returns:
        dict: Список параметров в виде словаря.
    """

    try:
        conffile = open('conf/main.yml', 'r')
    except IOError:
        exit(messagebox.showerror('ERROR', _('Config file not found')))

    config: dict[str, dict[str, str]] = yaml.full_load(conffile)
    conffile.close()
    return config


if __name__ == '__main__':
    print(getconfig.__doc__)