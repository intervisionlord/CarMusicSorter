#!/bin/bash

#################################
# Car Music Sorter
# Intervision
# v:. 0.01
#################################

#	VARS	#################
FOLDER=''

if [ -n "$1" ]
then
	FOLDER=$1
else
	echo "Использование: $0 <Директория для обработки (полный путь)>"
	echo "Не указана директория или директория задана некорректно"
	exit 42
fi

echo "Переходим в рабочую директорию $FOLDER"
cd $FOLDER
echo "Переносим треки из альбомов в корневую директорию $FOLDER"
find . -name '*.mp3' -exec mv {} ./ \;

echo "DONE"
echo "Удаляем цифры из начала имен файлов"

for f in [0-9]*; do mv -f "$f" "`echo $f | sed 's/^[0-9]*\W*//'`"; done
echo "DONE"

echo "Удаляем директории"
find . ! -name "." ! -name ".." -type d -exec rm -rf {} +
echo "DONE"

echo "Работа завершена"