# cig_detect
**Задача обучить нейросеть детектировать сигареты на фото и видео**   
**Необходимо  реализовать инференс на изображении из командной строки (отрисовать
bbox-ы).   
Пример запуска: python3 detector.py --source 00001.png**

1. Дататест с фото курильщиков обнаружен и взят с kaggle.com    
2. Проведена разметка для детекции с помощью https://www.makesense.ai/ . около 1200 изображений.      
3. Выбрана легковесная модель yolov5s .       
4. ДОбучена модель на весах COCO датасета на 35 эпохах.(больше уже не хватает бесплатного времени GPU в colab).          
5. Уже на наших весах делаем предикт тест дата.        
6. Для улучшения метрик(качества детекции) необходимо :      
- больше размеченных данных
- GPU для более долгого обучения, необходимо около 300 эпох минимум(колаб дает на малое кол-во времени GPU бесплатное)
7. Подготовлен скрип install.py для клона репозитария yolov5, установки необходимых библиотек и подгрузки обученных весов с облачного хранилища.
И сприпт detector.py который выполняет задачи согласно требования задания.
8. Для реализации запуска mp4 и одновременно детекции необходимо запускать стрим видео и тогда будет возможность в прямом эфире детектировать.
  Модель может сохранять видео mp4 c сигареты или делать детекцию в онлайне со стрима и др источников.        
  -- sourse        
0 #webcam, img.jpg, vid.mp4,  screen,  path/ , list.txt, list.streams, 'path/*.jpg',     'https://youtu.be/Zgi9g1ksQHc',     'rtsp://example.com/media.mp4'     


Инструкция по применению:       
1. скачать install.py, detector.py  в исходную папку    где будт фото  
2. запустить install.py выполнится клон репозитария yolov5, скачивание весов детекции сигарет в текущую папку.     
3. Запускать  python3 detector --sourse 0001.jpg , в папке появится фото с детектированием сигаретой с таким же именем.


![image](https://github.com/ivan74rus/cig_detect/assets/117063726/918e0c56-9f5b-4131-a681-ced92175a596)

