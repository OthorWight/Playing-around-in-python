import threading
import time
from appJar import gui

class work (threading.Thread):
    def __init__(self, threadID, name, counter, delay):
        threading.Thread.__init__(self)
        self.threadID = threadID
        self.name = name
        self.counter = counter
        self.delay = delay
        self.paused = False
        self.pause_cond = threading.Condition(threading.Lock())
    def pause(self):
        self.paused = True
        self.pause_cond.acquire()
    def resume(self):
        self.paused = False
        self.pause_cond.notify()
        self.pause_cond.release()
    def run(self):
        print("Starting " + self.name)
        while self.counter:
            time.sleep(self.delay)
            while self.paused:
                time.sleep(.1)
            print("%s: %s: %s" %(self.name, time.ctime(time.time()), self.counter))
            self.counter -= 1
        print("Exiting " + self.name)

def press(button):
    if button == "T1":
        global thread1
        thread1 = work(1, "Worker-1", 5, 2)
        thread1.start()
    elif button == "T2":
        global thread2
        thread2 = work(2, "Worker-2", 10, 1)
        thread2.start()
    elif button == "P1":
        thread1.pause()
    elif button == "P2":
        thread2.pause()
    elif button == "R1":
        thread1.resume()
    elif button == "R2":
        thread2.resume()
    elif button == "Exit":
        app.stop()

app = gui("Threads", "400x300")
app.setFont(18)

app.addButtons(["T1", "T2", "Exit"], press)
app.addButtons(["P1", "P2"], press)
app.addButtons(["R1", "R2"], press)

app.go()

print("Exiting main thread")