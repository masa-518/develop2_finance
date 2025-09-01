# txtファイルの関係を扱う

import shutil
from .time_system import TimeSystem

class TxtSystem:
    
    def __init__(self):
        
        self.__time = TimeSystem()

    def write_log_txt(self, message):
        """ ログの出力内容をtxtファイルに反映する """
        
        with open("log_txt/temp.txt", mode = 'a') as fw:
            fw.write(f'{message}\n')
            
    def log_txt_initialize(self):
        """ temのログファイルを作成する """
        
        with open("log_txt/temp.txt", mode = 'w') as fw:
            message = self.__time.print_time() + 'Print Log'
            fw.write(f'{message}\n')

    def log_txt_perce(self):
        """ ログをtempから転送する """
        
        copy_path = "log_txt/" + f"{self.__time.get_current_time()}.txt"
        shutil.copy("log_txt/temp.txt", copy_path)