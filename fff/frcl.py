class File:

    def __init__(self, file_path): #ПУТЬ ФАЙЛА ИННА СЧИТАЙ ИМЯ
        self.file_path = file_path

    def create_file(self): #ЭТО СОЗДАНИЕ ФАЙЛА ЕСЛИ ЕГО НЕТ
        try:
            with open(self.file_path, 'x') as ffile:
                return 'фааайл создан!'
        except FileExistsError:
            return 'уже есть файл не'

    def read_file(self): #туда сюда просто вывод данных.не представляю что тут надо если мп3 скинуть...
        try:
            with open(self.file_path, 'r') as ffile:
                ffile.seek(0)
                ref = ffile.read()
                print('в вашем файлееее')
                return ref
        except FileNotFoundError:
            return 'такого файла нееет'

    def write_file(self): #это с нуля С НУЛЯ заполнение файла.. мп3... грустно...
        try:
            with open(self.file_path, 'w') as ffile:
                a = ffile.write(f'input()')
                return a
        except FileNotFoundError:
            return 'такого файла нееет'

    def add_in_file(self): #добавление в файл
        try:
            with open(self.file_path, 'a+') as ffile: #novaya str
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



# readme = File(r'E:\РАБОЧИЙ СТОЛ\моя папка!\Readme.txt')
# aaa = File(r'E:\РАБОЧИЙ СТОЛ\моя папка!\prov.txt')
# print(readme.read_file())
# aaa.write_file()
file = input('Введите путь файла, либо напишите "НЕТ" если файла нет ')
if file.lower() == 'нет':
    name = input('Введите имя файла и его путь? я не знаю работает ли без пути....')
    newfile = File(name)
    newfile.create_file()
else:
    newfile = File(file)

#newfile.write_file()
#newfile.add_in_file()
newfile.delete_deta()
print(newfile.read_file())
