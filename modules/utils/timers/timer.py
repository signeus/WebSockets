import threading

class Timer():
    def __init__(self, time, func):
        self.time = int(time)
        self.timer = 0
        self.activate = False
        self.func = func

    def activeTimer(self):
        self.timer = threading.Timer(self.time, self.func)
        self.timer.start()
        self.activate =  True

    def deactiveTimer(self):
        self.timer.cancel()
        self.activate = False