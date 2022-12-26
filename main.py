from notifypy import Notify
import time
import random
import pystray
import PIL.Image
import threading
import sys, os

def resource_path(relative):
    try:
        base_path = sys._MEIPASS
    except Exception:
        base_path = os.path.abspath(".")
    return os.path.join(base_path,relative)

def pause():
    """ pause break time loop """
    while sleep:
        if not running: sys.exit(0)
        time.sleep(1)


def tenSecsBreakNotify():
    """ give the break notifictaion """
    notitication.title = "Break Time"
    notitication.message = "Time for your 10 seconds break"
    notitication.send()


def exitNotify():
    """ Application has been exited """
    notitication.title = "Exited"
    notitication.message = "See you soon"
    notitication.send()


def pauseNotify():
    """ Application has been paused """
    notitication.title = "Paused"
    notitication.message = "Come back soon!"
    notitication.send() 

def continueNotify():
    """ give the break notifictaion """
    notitication.title = "Continue"
    notitication.message = "Back To work"
    notitication.send()

def goWorkNotify():
    """ give the go work notification """
    notitication.title = "Time to Learn"
    notitication.message = "Go learn"
    notitication.send()


def on_click(icon, item):
    """ clicked button in hidden menu """
    if str(item) == "Pause":
        global sleep
        sleep = True
        pauseNotify()
    elif str(item) == "Exit":
        global running
        exitNotify()
        Icon.stop()
        running = False
    elif str(item) == "Continue":
        continueNotify()
        sleep = False


image = PIL.Image.open(resource_path("icon.png"))  #image 
sleep = False  #pause attribute
running = True

notitication = Notify(
    default_notification_application_name="10sPause",
    default_notification_message="10 seconds pause applicaiton",
    default_notification_icon= resource_path("icon.png")
    ) 

notitication.title = "10sPause"
notitication.message = "Application is running"
notitication.send()

Icon = pystray.Icon("10sPause", image, menu=pystray.Menu(
    pystray.MenuItem("Exit", on_click),
    pystray.MenuItem("Pause", on_click),
    pystray.MenuItem("Continue", on_click)

))

def run():
    """ run in a thread icon """
    Icon.run()



thread2 = threading.Thread(target=run)
thread2.start()


while running: 
    """ main loop """
    breakTime = 90 + (random.uniform(0,0.75) * 60)
    currentTime = 0
    sleepTime = 0

    while currentTime < breakTime:
        if not running: sys.exit(0)
        if sleep: pause()
        """ Timer """
        time.sleep(1)
        currentTime += 1

    if not running: sys.exit(0)
    tenSecsBreakNotify()

    while sleepTime < 10:
        if not running: sys.exit(0)
        """ 10 seconds break """
        if sleep:

            """ application is paused """
            pause()
        time.sleep(1)
        sleepTime += 1

    """ Go work notify """
    goWorkNotify()


