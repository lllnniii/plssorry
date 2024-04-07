from frcl import File
from os import environ
environ['PYGAME_HIDE_SUPPORT_PROMPT'] = '1'
import pygame


class FileMp3(File):
    def __init__(self, file_path):
        super().__init__(file_path)

    def play_mp3(self):
        try:
            pygame.mixer.init()
            pygame.mixer.music.load(self.file_path)
            pygame.mixer.music.play(loops=0)
        except FileNotFoundError:
            return 'mp3 фа2л не найден'

    def pause_mp3(self):
        pygame.mixer.music.pause()

    def unpause_mp3(self):
        pygame.mixer.music.unpause()

    def stop_mp3(self):
        pygame.mixer.music.stop()


# file = FileMp3(input('Введите путь файла '))
# file.play_mp3()
# com = input()
# pygame.time.delay(5000)
