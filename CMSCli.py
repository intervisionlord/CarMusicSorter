"""CLI Версия CMS."""
import os

vers = '0.3.4'


def ask_paths():
    """Запуск и в интерактивном режиме."""
    input_dir = input('Путь до исходной директории: ')
    output_dir = input('Путь до конечной директории: ')
    return input_dir, output_dir


def start_interactive():
    """Запуск интерактивного режима."""
    answers = ask_paths()
    input_dir = answers[0]
    output_dir = answers[1]
    if input_dir is None or output_dir is None:
        print('Не указана начальная или конечная директория')
        return
    elif input_dir == output_dir:
        print('Начальная и конечная директории не должны совпадать')
        return
    else:
        main_process(input_dir, output_dir)


def main_process(input_dir, output_dir):
    """Принимает начальную и конечную директории, запускает копирование.

    Параметры
    ----------
    input_dir : string
        Путь начальной директории в виде строки.
    output_dir : string
        Путь конечной директории в виде строки.

    Не возвращает результатов.
    -------
    """
    pass


start_interactive()
exit()

for path, subdirs, files in os.walk(input_dir):
    for file in files:
        # Перегоняем все MP3 в целевую директорию,
        # потом разберемся что с ними делать
        # Хотя, лучше искать только нужные (отбрасывать лайвы и ремиксы
        # и перегонять уже без них)
        filtered = re.search('.*mp3', file)
        if filtered is not None:
            print(f'{path}/{filtered.group(0)}')
            shutil.copyfile(f'{path}/{filtered.group(0)}',
                            f'{output_dir}/{filtered.group(0)}')

source_file = []
# 3.1. Удаление ремиксов и лайвов
regex = r'.*\(.*[Rr]emix.*\).*|.*\(.*[Ll]ive.*\).*'
for files in os.walk(output_dir):
    for file in files[2]:
        try:
            source_file.append(re.search(regex, file).group(0))
        except Exception:
            pass
for file in source_file:
    print('Removing Remix: ', file)
    os.remove(f'{output_dir}/{file}')
source_file.clear()  # Очищаем список

# 3.2. Готовим список свежепринесенных файлов с вычищенными ремиксами и лайвами
for files in os.walk(output_dir):
    for file in files[2]:
        try:
            source_file.append(file)
        except Exception:
            pass

# 3.3. Убираем из имен файлов мусор (номера треков в различном формате)
for file in source_file:
    new_file = re.sub(r'^[\d{1,2}\s\-\.]*', '', file)
    shutil.move(f'{output_dir}/{file}', f'{output_dir}/{new_file}')
source_file.clear()
