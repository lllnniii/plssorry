import os

class File:

    def __init__(self, file_path):
        self.file_path = file_path

    def rename_file(self, new_path):
        try:
            os.rename(self.file_path, new_path)
        except FileNotFoundError:
            print("Файл не найден")
