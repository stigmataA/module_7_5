import os
import time


directory = "."
#print(os.getcwd())
for root, dirs, file in os.walk(directory):
    print(f'Корень = "{root}", Директория = "{dirs}"')
    for i, file in enumerate(file):
        print(f'{i + 1}:', end = '')
        filepath = os.path.join(root, file)
        filetime = os.path.getmtime(filepath)
        formatted_time = time.strftime("%d.%m.%Y %H:%M", time.localtime(filetime))
        filesize = os.path.getsize(filepath)
        parent_dir = os.path.dirname(root)
        print(
            f'Обнаружен файл: {file}, Путь: {filepath}, Размер: {filesize} байт, Время изменения: {formatted_time}, Родительская директория: {parent_dir}')







