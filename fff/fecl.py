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
            return 'картинка не найдена'

    def show_png(self):
        with Image.open(self.file_path) as image:
            image.show()

    def change_format(self, new_format):
        image = self.open_png()
        new_path = self.file_path.split('.')[0] + f'.{new_format}'
        image.save(new_path)

    def resize_png(self, new_size):
        image = self.open_png()
        print(image.size)
        resize = image.resize(new_size)
        resize.show()
        resize.save(self.file_path)


# file = FilePng(r'E:\РАБОЧИЙ СТОЛ\photo_2024-03-30_20-32-46.jpg')
# new_size = tuple([int(i) for i in input().split()])
# print(new_size)
# file.resize_png(new_size)
