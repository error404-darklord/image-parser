# IMAGE-PARSER

Скрипт на Python для скачивания изображений с веб-страниц. Пользователь вводит список ссылок, и программа автоматически сохраняет все найденные изображения в указанную папку на устройстве.

## Возможности

- Загрузка изображений с нескольких URL.
- Поддержка большого количества форматов изображений:
  `.jpg`, `.jpeg`, `.png`, `.gif`, `.bmp`, `.webp`, `.heic`, `.heif`, `.tiff`, `.raw`, `.psd`, `.ico`, `.dds`, `.apng`, `.tga`, `.xcf` и др.
- Красивое ASCII-меню при запуске.
- самостоятельное указание пути для загрузки.

## Куда сохраняются изображения?

Изображения сохраняются в папку которую вы укажите, если таковой нет значит он напишет:

`error 404 - папки не существует`

# Где доступно?

Абсолютно везде:
- ANDROID (TERMUX)
- WINDOWS
- LINUX
- UBUNTU/DEBIAN

## Требования ОБЯЗАТЕЛЬНО ПРОЧИТАТЬ!

### Общие
- Python 3.6 или выше
- Подключение к интернету

### Python-библиотеки
- requests
- beautifulsoup4
- colorama

### Android (через Termux)
- Termux
- Python: `pkg install python`
- Git: `pkg install git`

### Android (через Pydroid 3)
- Приложение Pydroid 3
- Доп. пакет Pydroid repository plugin (для pip)
- Вручную добавить файлы в `/storage/emulated/0/` или использовать встроенный редактор

### Windows
- Установленный Python (с официального сайта https://python.org)
- Git (опционально, https://git-scm.com)

### Ubuntu / Debian
- Python и pip:
  ```bash
  sudo apt install python3 python3-pip

# Инструкция по установке.
---
### ANDROID (TERMUX)
```
pkg update && pkg upgrade
pkg install git python
git clone https://github.com/error404-darklord/image-parser.git
cd image-parser
pip install requests beautifulsoup4 colorama
python pars-4.0.py
```
### WINDOWS
```
git clone https://github.com/error404-darklord/image-parser.git
cd image-parser
pip install requests beautifulsoup4 colorama
python pars-4.0.py
```
### UBUNTU / DEBIAN
```
sudo apt update
sudo apt install git python3 python3-pip
git clone https://github.com/error404-darklord/image-parser.git
cd image-parser
pip3 install requests beautifulsoup4 colorama
python3 pars-4.0.py
```
