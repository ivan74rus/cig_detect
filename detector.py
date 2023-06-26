#!/usr/bin/env python3
import sys
import subprocess
import os

source_file = sys.argv[2] if len(sys.argv) > 2 else ""

# Получение абсолютного пути к текущей директории
current_directory = os.getcwd()

# Формирование пути к файлу detect.py
detect_script_path = os.path.join(current_directory, 'yolov5', 'detect.py')

command = f'python {detect_script_path} --weights yolov5/weights/cigarette_v2.pt --img 640 --conf 0.25 --exist-ok --name "$(pwd)" --source {source_file}'
subprocess.run(command, shell=True)