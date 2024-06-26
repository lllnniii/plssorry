from PIL import Image
from frcl import File
import os


class FilePng(File):
    def __init__(self, file_path):
        super().__init__(file_path)

    def open_png(self):
        try:
            return Image.open(self.file_path)
        except FileNotFoundError:
            print('картинка не найдена')

    def show_png(self):
        try:
            image = self.open_png()
            image.show()
        except FileNotFoundError:
            print('картинка не найдена')
        except AttributeError:
            print('я не понимаю почему эта ошибка...')

    def change_format(self, new_format):
        try:
            image = self.open_png()
            new_path = self.file_path.split('.')[0] + f'.{new_format}'
            image.save(new_path)
        except FileNotFoundError:
            print('картинка не найдена')

    def resize_png(self, new_size):
        try:
            image = self.open_png()
            print(image.size)
            resize = image.resize(new_size)
            resize.show()
            resize.save(self.file_path)
        except FileNotFoundError:
            print('картинка не найдена ')


# file = FilePng(r"E:\РАБОЧИЙ СТОЛ\metoo.png")
# file.show_png()
# new_size = tuple([int(i) for i in input().split()])
