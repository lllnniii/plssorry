from frcl import File


class FileTxt(File):

    def __init__(self, file_path):
        super().__init__(file_path)

    def create_file(self):  # ЭТО СОЗДАНИЕ ФАЙЛА ЕСЛИ ЕГО НЕТ
        try:
            with open(self.file_path, 'x') as ffile:
                return 'фааайл создан!'
        except FileExistsError:
            return 'уже есть такой файл'

    def read_file(self):  # туда сюда просто вывод данных.
        try:
            with open(self.file_path, 'r') as ffile:
                ffile.seek(0)
                ref = ffile.read()
                print('в вашем файлееее: \n')
                print(ref)
        except FileNotFoundError:
            return 'такого файла нееет'

    def write_file(self):  # это с нуля С НУЛЯ заполнение файла..
        try:
            with open(self.file_path, 'w') as ffile:
                a = ffile.write(input())
                return a
        except FileNotFoundError:
            return 'такого файла нееет'

    def add_in_file(self):  # добавление в файл
        try:
            with open(self.file_path, 'a+') as ffile:  # novaya str
                ffile.seek(0)
                data = ffile.read(100)
                if len(data) > 0:
                    ffile.write('\n')

            with open(self.file_path, 'r') as ffile:
                strings = ffile.readlines()
            strings.insert(int(input('Введите строку ')) - 1, input('ТЕКСТ ') + '\n')
            newlines = ''.join(strings)
            with open(self.file_path, 'w') as ffile:
                a = ffile.write(newlines)
                return a

        except FileNotFoundError:
            return 'такого файла нееет'

    def delete_deta(self):
        try:
            with open(self.file_path, 'r') as ffile:
                strings = ffile.readlines()
            del strings[int(input('строка для удаления ')) - 1]
            newlines = ''.join(strings)
            with open(self.file_path, 'w') as ffile:
                a = ffile.write(newlines)
                return a

        except FileNotFoundError:
            return 'такого файла нееет'
