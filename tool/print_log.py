# プリント出力を行う

from .time_system import TimeSystem
from .txt_system import TxtSystem

class PrintLog:

    def __init__(self, module):

        self.__module = module
        self.__message = None
        self.__time = TimeSystem()
        self.__txt = TxtSystem()
        self.__log_level = ["[INFO]", "[ERROR]", "[WARN]", "[Debug]"]

        # debugログを出力する際にはTrueにする
        self.__is_debug_log = True

    def print_info(self, message):
        """ infoログを出力する """

        self.__message = message
        self.__log_info_print(self.__log_level[0])

    def print_error(self, message):
        """ errorログを出力する """

        self.__message = message
        self.__log_info_print(self.__log_level[1])

    def print_warn(self, message):
        """ warnログを出力する """

        self.__message = message
        self.__log_info_print(self.__log_level[2])

    def print_debug(self, message):
        """ debugログを出力する """

        if self.__is_debug_log is False:
            return

        self.__message = message
        self.__log_info_print(self.__log_level[3])

    def __log_info_print(self, log_level):
        """ ログを表示させる """

        message = None
        time = self.__time.print_time()
        message = f"{time} {log_level} [{self.__module}]: {self.__message}"
        self.__txt.write_log_txt(message)
        print(message)
        

