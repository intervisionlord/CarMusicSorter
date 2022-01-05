"""CLI Версия CMS."""
import os
from pathlib import Path

vers = '0.3.3с'


def ask_paths():
    """Запуск и в интерактивном режиме."""
    print('Путь до исходной директории')
    input_dir = input()
    print('Путь до конечной директории')
    output_dir = input()
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
        main_process()


def main_process():
    """Основной процесс программы."""
    pass


if input_dir == '' or output_dir == '':
    print('Не указана начальная или конечная директория')
    exit()
elif input_dir == output_dir:
    print('Начальная и конечная директории не должны совпадать')
    exit()
try:
    input_dir
except Exception:
    pass
else:
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
for files in os.walk(output_dir):
    for file in files[2]:
        try:
            source_file.append(re.search(r'.*\(.*[Rr]emix.*\).*|.*\(.*[Ll]ive.*\).*', file).group(0))
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
