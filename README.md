<img src="https://i.imgur.com/dSzqaaP.png"  width=50 alt="Car Music Sorter Icon">

# Car Music Sorter

[![Build Status](https://app.travis-ci.com/intervisionlord/CarMusicSorter.svg?branch=master)](https://app.travis-ci.com/intervisionlord/CarMusicSorter)
[![Scrutinizer Code Quality](https://scrutinizer-ci.com/g/intervisionlord/CarMusicSorter/badges/quality-score.png?b=master)](https://scrutinizer-ci.com/g/intervisionlord/CarMusicSorter/?branch=master)
[![Code Intelligence Status](https://scrutinizer-ci.com/g/intervisionlord/CarMusicSorter/badges/code-intelligence.svg?b=master)](https://scrutinizer-ci.com/code-intelligence)
[![License: GPL v3](https://img.shields.io/badge/License-GPLv3-blue.svg)](https://www.gnu.org/licenses/gpl-3.0)

![GitHub contributors](https://img.shields.io/github/contributors/intervisionlord/CarMusicSorter)
![GitHub last commit](https://img.shields.io/github/last-commit/intervisionlord/CarMusicSorter)
[![Coverage Status](https://coveralls.io/repos/github/intervisionlord/CarMusicSorter/badge.svg?branch=dev)](https://coveralls.io/github/intervisionlord/CarMusicSorter?branch=master)
![Lines of code](https://img.shields.io/tokei/lines/github/intervisionlord/CarMusicSorter)

Утилита для извлечения треков из субдиректорий исполнителя (альбомов) и сохранении их в единой директории с названием исполнителя для последующей загрузки на флешку для автомагнитолы.

---

- [Car Music Sorter](#car-music-sorter)
    - [1. Общие сведения](#1-общие-сведения)
      - [Интерфейс](#интерфейс)
      - [Версии](#версии)
      - [Скачать последнюю версию](#скачать-последнюю-версию)
          - [CarMusicSorter (latest)](#carmusicsorter-latest)
    - [2. Использование](#2-использование)
    - [3. Локализация](#3-локализация)


### 1. Общие сведения
Программа собирает треки из директории исполнителя и субдиректорий, переносит их в целевую директорию одним списком (без субдиректорий).
Затем вычищает из имен файлов цифры в начале имени файла - номера треков (если есть), убирает потенциальные дубли треков (напр. синглы),
а также, Live и Remix треки.
Это позволяет упростить навигацию по трекам и исполнителям в некоторых магнитолах, которые производят переход к следующей директории только после обхода предыдущей директории.

<img src="https://i.imgur.com/wwkq7Sh.png">

#### Интерфейс
<img src="https://i.imgur.com/57hvvMy.png">

#### Версии
Реализовано 2 варианта программы:
  * С графическим интерфейсом (GUI)
  * Только командная строка (CLI)
В релиз входят обе версии (а также bash версия, в виде которой инструмент существовал ранее (просто так))

#### Скачать последнюю версию
###### [CarMusicSorter (latest)](https://github.com/intervisionlord/CarMusicSorter/releases/latest)

### 2. Использование
  1. После запуска программы необходимо указать начальную директорию, в которой будет осуществляться поиск треков.
  2. Далее необходимо указать конечную директорию, в которой будут размещены преобразовыные треки.
  3. После необходимо нажать кнопку `Начать` и дождаться завершения работы программы.

### 3. Локализация
Локализация размещается в директории `l10n`.
Для создания своей локализации можно взять за исходный шаблон `CarMusicSorter.pot`, после перевода и компиляции файлов перевода их необходимо разместить в директории `l10n` и поддиректории с кодом языка.

Установка необходимой локализации осуществляется в меню `Файл`->`Настройки` или конфиге `conf/main.yml`