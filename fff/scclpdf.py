from frcl import File
from pdf2image import convert_from_path
from PIL import Image


class FilePdf(File):
    def __init__(self, file_path, save_dir, res=400):
        super().__init__(file_path)
        self.save_dir = save_dir
        self.res = res
        self.img_path = []

    def open_pdf(self):
        try:
            pages = convert_from_path(self.file_path, self.res,
                                      poppler_path=r'C:\Program Files\poppler-24.02.0\Library\bin')

            name_with_extension = self.file_path.rsplit('\\')[-1]
            name = name_with_extension.rsplit('.')[0]
            for idx, page in enumerate(pages):
                image_path = f'{self.save_dir}/{name}_{idx}.png'
                page.save(image_path, 'PNG')
                self.img_path.append(image_path)

            for pages in self.img_path:
                page = Image.open(pages)
                page.show()
        except FileNotFoundError:
            return 'ПДФ не найден'


# file_path = input('введите путь файла ').replace('\\', '/')
# dir = input('введите путь к файлу для сохранения ')
#
# pdf_file = FilePdf(file_path, dir)
# pdf_file.open_pdf()
