from tkinter import Tk
from threading import Thread

class App:

    __window: Tk
    __main_thread: Thread
    __run: bool

    def __init__(self):
        self.__window = Tk("Name")
        self.__main_thread = Thread(target=self.interface)
        self.__run = False

        self.load_ui()

    def interface(self):
        while self.__run:
            self.__window.update()

    def start(self):
        self.__run = True
        self.__main_thread.start()

    def stop(self):
        self.__run = False
        self.__main_thread = Thread(target=self.interface)

    def load_ui(self):
        pass
