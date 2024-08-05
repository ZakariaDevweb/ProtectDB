from tkinter import Tk
from threading import Thread
from view import View


class App:
    __window: Tk
    __main_thread: Thread
    __run: bool
    __view: View

    def __init__(self) -> None:
        self.__window = Tk("Name")
        self.__main_thread = Thread(target=self.__interface)
        self.__run = False

        self.__view = View.PASSWORD_REQUEST
        self.__load_ui()

    def get_current_view(self) -> View:
        return self.__view

    def __interface(self) -> None:
        while self.__run:
            self.__window.update()

    def start(self) -> None:
        self.__run = True
        self.__main_thread.start()

    def stop(self) -> None:
        self.__run = False
        self.__main_thread = Thread(target=self.__interface)

    def __load_ui(self) -> bool:
        """
        Helper method which loads up the corresponding ui depending on the current view.
        :return: False if the view is incorrect. True in all other cases.
        """
        if self.__view == View.PASSWORD_REQUEST:
            self.__load_password_request_ui()
            return True

        if self.__view == View.PASSWORDS:
            self.__load_passwords_view_ui()
            return True

        if self.__view == View.DATABASE:
            self.__load_database_view_ui()
            return True

        if self.__view == View.PASSWORD_CREATION:
            self.__load_password_creation_ui()
            return True

        return False

    def __load_password_request_ui(self) -> None:
        pass

    def __load_passwords_view_ui(self) -> None:
        pass

    def __load_database_view_ui(self) -> None:
        pass

    def __load_password_creation_ui(self) -> None:
        pass

    def switch_to_password_view(self) -> None:
        self.__view = View.PASSWORDS
        self.__load_passwords_view_ui()

    def switch_to_database_view(self) -> None:
        self.__view = View.DATABASE
        self.__load_database_view_ui()

    def switch_to_password_request_view(self) -> None:
        self.__view = View.PASSWORD_REQUEST
        self.__load_password_request_ui()

    def switch_to_password_creation_view(self) -> None:
        self.__view = View.PASSWORD_CREATION
        self.__load_password_creation_ui()
