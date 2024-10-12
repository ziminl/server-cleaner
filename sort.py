import os
import shutil

current_directory = os.getcwd()
destination_folder = 'logs folder'

if not os.path.exists(destination_folder):
    os.makedirs(destination_folder)

for filename in os.listdir(current_directory):
    if 'log' in filename:
        file_path = os.path.join(current_directory, filename)
        shutil.move(file_path, os.path.join(destination_folder, filename))

print("success")
