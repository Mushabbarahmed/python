from time import time
from datetime import datetime
from pygame import mixer
import time

def ms(stopper):
    print("music")
    mixer.init()
    mixer.music.load("good3.mp3")
    mixer.music.play()
    while True:
        a=input()
        if a==stopper:
            mixer.music.stop()
            break
ms("drank")
# n=datetime.now()
# print(n)
# n1=time.asctime()
# print(n1)