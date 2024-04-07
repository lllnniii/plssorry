from frcl import File
from scclpdf import FilePdf
from thclmp3 import FileMp3
from feclpng import FilePng
from fitxt import FileTxt
import os


def check_file(file_path):
    file_extension = file_path.split('.')[-1].lower()
    try:

        if file_extension == 'pdf':
            print('pdf')
            return FilePdf(file_path, os.path.dirname(file_path))
        elif file_extension == 'txt':
            print('txt')
            return FileTxt(file_path)
        elif file_extension == 'mp3':
            print('mp3')
            return FileMp3(file_path)
        elif file_extension == 'png':
            print('png')
            return FilePng(file_path)
    except FileNotFoundError:
        print("Файл не найден")


file = input()
plsidun = check_file(file)

if plsidun:
    if isinstance(plsidun, FilePdf):
        plsidun.open_pdf()
    elif isinstance(plsidun, FileTxt):
        plsidun.read_file()
    elif isinstance(plsidun, FileMp3):
        plsidun.play_mp3()
        input()
    elif isinstance(plsidun, FilePng):
        plsidun.show_png()
else:
    print('выберите другой файл')
#txt ne rabotaet tk ya dura