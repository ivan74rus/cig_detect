#!/usr/bin/env python3

import subprocess
import os
import gdown


# Клонирование репозитория
subprocess.run(['git', 'clone', 'https://github.com/ultralytics/yolov5'])

# Изменение текущей рабочей директории на yolov5
os.chdir('yolov5')

# Установка зависимостей
subprocess.run(['pip', 'install', '-qr', 'requirements.txt'])

# Импорт библиотек
import torch
import sys

# Добавьте путь к текущей директории в sys.path
sys.path.append('.')

# Импорт модуля utils
import utils

display = utils.notebook_init()

# Создание папки yolov5/weights
os.makedirs('weights', exist_ok=True)

# URL для скачивания файла
url = 'https://drive.google.com/uc?id=1-5pFUhVbngP6Jt56IySnN6723fR1YgYG'

# Путь к папке "weights"
weights_dir = 'weights'

# Убедитесь, что папка "weights" существует
os.makedirs(weights_dir, exist_ok=True)

# Имя файла для сохранения
filename = os.path.join(weights_dir, 'cigarette_v2.pt')

# Скачивание файла
gdown.download(url, filename, quiet=False)


