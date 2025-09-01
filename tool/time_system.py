# 時間の管理を行う

import time
import datetime

class TimeSystem:
    
    def __init__(self):

        self.__current_time = None
    
    def print_time(self):
        """ ログ出力用に現在の時間を返す """

        time_message = self.get_current_time()
        time_message = f"[{time_message}]"
        return time_message

    def get_current_time(self):
        """ 現在の時間を取得する """

        dt_now = datetime.datetime.now()
        self.__current_time = dt_now.strftime('%Y-%m-%d_%H-%M-%S')
        return self.__current_time
