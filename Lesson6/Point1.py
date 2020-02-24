import time

class TrafficLight:
    __d_color = {0: 'RED', 1: 'YELLOW', 2: 'GREEN'}
    def __init__(self):
        self.__traffic_color = self.__d_color[0]

    def running(self):
        cnt = 0
        while True:
            self.__traffic_color = self.__d_color[0]
            print(self.__traffic_color)
            time.sleep(7)
            self.__traffic_color = self.__d_color[1]
            print(self.__traffic_color)
            time.sleep(2)
            self.__traffic_color = self.__d_color[2]
            print(self.__traffic_color)
            time.sleep(5)


t = TrafficLight()
t.running()

