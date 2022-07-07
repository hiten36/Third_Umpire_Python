from tkinter import *
import threading
from PIL import Image,ImageTk
import cv2
from functools import partial
import imutils
import time
WIDTH=600
HEIGHT=348
stream=cv2.VideoCapture('video.mp4')
def play(speed):
    frame1=stream.get(cv2.CAP_PROP_POS_FRAMES)
    stream.set(cv2.CAP_PROP_POS_FRAMES,frame1+speed)
    grabbed,frame=stream.read()
    frame=imutils.resize(frame,width=WIDTH,height=HEIGHT)
    frame=ImageTk.PhotoImage(image=Image.fromarray(frame))
    canvas.image=frame
    canvas.create_image(0,0,image=frame,anchor="nw")
    canvas.create_text(134,26,text="decision pending",fill='black',font='Times 26 bold')

def pending(decision):
    frame=cv2.cvtColor(cv2.imread('decision.png'),cv2.COLOR_BGR2RGB)
    frame=imutils.resize(frame,width=WIDTH,height=HEIGHT)
    frame=ImageTk.PhotoImage(image=Image.fromarray(frame))
    canvas.image=frame
    canvas.create_image(0,0,image=frame,anchor='nw')
    time.sleep(1.5)
    frame=cv2.cvtColor(cv2.imread('sponser.png'),cv2.COLOR_BGR2RGB)
    frame=imutils.resize(frame,width=WIDTH,height=HEIGHT)
    frame=ImageTk.PhotoImage(image=Image.fromarray(frame))
    canvas.image=frame
    canvas.create_image(0,0,image=frame,anchor='nw')
    time.sleep(2.5)
    if decision=='out':
        decision_img='out.png'
    else:
        decision_img='not-out.png'
    frame=cv2.cvtColor(cv2.imread(decision_img),cv2.COLOR_BGR2RGB)
    frame=imutils.resize(frame,width=WIDTH,height=HEIGHT)
    frame=ImageTk.PhotoImage(image=Image.fromarray(frame))
    canvas.image=frame
    canvas.create_image(0,0,image=frame,anchor='nw')
def out():
    thread=threading.Thread(target=pending,args=('out',))
    thread.daemon=1
    thread.start()
def not_out():
    thread=threading.Thread(target=pending,args=('not out',))
    thread.daemon=1
    thread.start()

root=Tk()
root.title('advanced video player by hiten')
frame2=cv2.cvtColor(cv2.imread('lords-removebg-preview.png'),cv2.COLOR_BGR2RGB)
frame=ImageTk.PhotoImage(Image.fromarray(frame2))
canvas=Canvas(root,width=WIDTH,height=HEIGHT)
img=canvas.create_image(0,0,image=frame,anchor='nw')
canvas.pack()
btn=Button(root,text='<< Previous(fast)',width=50,command=partial(play,-25))
btn.pack()
Button(root,text='<< previous(slow)',width=50,command=partial(play,5)).pack()
Button(root,text='>> next(fast)',width=50,command=partial(play,25)).pack()
Button(root,text='>> next(slow)',width=50,command=partial(play,5)).pack()
Button(root,text='give out',width=50,command=out).pack()
Button(root,text='give not out',width=50,command=not_out).pack()

root.mainloop()