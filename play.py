from tkinter import *
from tkvideo import tkvideo
import sqlite3
import time

waitingStatus = False
extraTime = 4

root = Tk()
root.attributes('-fullscreen', True)

img=PhotoImage(file='waiting.png')

video = Label(root)
waiting = Label(root,image=img)

# shows waiting screen
def showWaiting():
    global waiting, video
    video.after(0, lambda: video.destroy())
    waiting = Label(root,image=img)
    waiting.pack()

def updatePending(pendingId):
    conn = sqlite3.connect('primes')
    c = conn.cursor()
    c.execute('UPDATE incoming_phrases SET pending = 0 WHERE id = ' + str(pendingId))
    conn.commit()

def getPending():
    conn = sqlite3.connect('primes')
    c = conn.cursor()
    c.execute('SELECT * FROM incoming_phrases WHERE pending = 1 AND videoId <> 0 LIMIT 1')
    data = c.fetchall()

    # check if there are no pending phrases
    if not data:
        return False

    print("Found 1")
    print(data[0])
    # if there is a pending phrase, return it
    return data[0]

# plays video
def playVideo(path, pendingId):
    global waiting, video
    waiting.after(0, lambda: waiting.destroy())
    video = Label(root)
    video.pack()
    player = tkvideo("/home/pi/primes/videos/" + path,video, loop = 0, size=(480,330))
    player.play()
    updatePending(pendingId)

def getVideoInfo(videoId):
    conn = sqlite3.connect('primes')
    c = conn.cursor()
    c.execute('SELECT * FROM videos WHERE id = ' + str(videoId))
    data = c.fetchall()

    return data[0]

# main function to periodically check for pending video
def check():
    global root, waitingStatus, extraTime
    pending = getPending()
    print(pending, waitingStatus)
    if (pending == False):
        if (not waitingStatus):
            waitingStatus = True
            showWaiting()
        wait = 1000
    else:
        videoInfo = getVideoInfo(pending[4])
        if (waitingStatus):
            waitingStatus = False
            playVideo(videoInfo[2], pending[0])
        wait = (int(videoInfo[3]) + extraTime) * 1000
    root.after(wait, check)

root.after(1000, check)
root.mainloop()
