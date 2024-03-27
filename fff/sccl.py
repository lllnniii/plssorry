from frcl import File
import PyPDF2


class FilePDF(File):
    def __int__(self, file_path):
        super().__init__(file_path)

    def output_file(self):
        try:
            with open(self.file_path, 'rb') as ffile:
                reader = PyPDF2.PdfReader(ffile)
                txt = ''
                for page in range(reader.getNumPages()):
                    pa = reader.getPage(page)
                    txt += pa.extractText()
                return txt
        except FileNotFoundError:
            return 'Файла НеЕЕт'


#inp = input()
#path = FilePDF(inp)
#print(path.output_file())
