import os
import shutil
import random


def move_and_delete(root_folder, destination_folder, portion=0.3):
    # Создаем целевую папку, если она не существует
    if not os.path.exists(destination_folder):
        os.makedirs(destination_folder)

    # Проходим по всем папкам A-Z
    for letter_folder in os.listdir(root_folder):
        if letter_folder.isalpha():  # Проверяем, что это папка с буквой
            letter_folder_path = os.path.join(root_folder, letter_folder)
            # Получаем список файлов в папке
            files = [f for f in os.listdir(letter_folder_path) if os.path.isfile(os.path.join(letter_folder_path, f))]
            # Определяем количество файлов, которые нужно переместить
            num_to_move = int(len(files) * portion)
            # Случайным образом выбираем файлы для перемещения
            files_to_move = random.sample(files, num_to_move)
            # Перемещаем выбранные файлы в целевую папку
            for file_to_move in files_to_move:
                source_file = os.path.join(letter_folder_path, file_to_move)
                destination_file = os.path.join(destination_folder, letter_folder, file_to_move)
                # Создаем папку для буквы в целевой папке, если она не существует
                if not os.path.exists(os.path.join(destination_folder, letter_folder)):
                    os.makedirs(os.path.join(destination_folder, letter_folder))
                shutil.move(source_file, destination_file)
                print(f"{file_to_move} moved")


# Укажите путь к корневой папке, содержащей папки A-Z
root_folder = "Latin"
# Укажите путь к целевой папке, куда будут перемещены папки A-Z
destination_folder = "Latin-valid"
# Указываем долю файлов, которые нужно переместить (в данном случае 30%)
portion = 0.1

move_and_delete(root_folder, destination_folder, portion)
