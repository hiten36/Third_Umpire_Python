from tkinter import *
import cv2
import threading
from PIL import Image,ImageTk
import time
import imutils
from functools import partial
WIDTH=650
HEIGHT=368
stream=cv2.VideoCapture('video.mp4')
flag=True
def play(speed):
    global flag
    print(f'you clicked on play.speed is {speed}')
    frmae1=stream.get(cv2.CAP_PROP_POS_FRAMES)
    stream.set(cv2.CAP_PROP_POS_FRAMES,frmae1+speed)
    grabbed,frame=stream.read()
    frame=imutils.resize(frame,width=WIDTH,height=HEIGHT)
    frame=ImageTk.PhotoImage(image=Image.fromarray(frame))
    canvas.image=frame
    canvas.create_image(0,0,image=frame,anchor=NW)
    if flag:
        canvas.create_text(134,26,fill="black",font="Times 26 bold",text="Decision Pending")
    flag=not flag
def pending(decision):
    frame=cv2.cvtColor(cv2.imread("decision.png"),cv2.COLOR_BGR2RGB)
    frame=imutils.resize(frame,width=WIDTH,height=HEIGHT)
    frame=ImageTk.PhotoImage(image=Image.fromarray(frame))
    canvas.image=frame
    canvas.create_image(0,0,image=frame,anchor=NW)
    time.sleep(1.5)
    frame=cv2.cvtColor(cv2.imread("sponser.png"),cv2.COLOR_BGR2RGB)
    frame=imutils.resize(frame,width=WIDTH,height=HEIGHT)
    frame=ImageTk.PhotoImage(image=Image.fromarray(frame))
    canvas.image=frame
    canvas.create_image(0,0,image=frame,anchor=NW)
    time.sleep(2.5)
    if decision=='out':
        decision_img='out.png'
    else:
        decision_img='not-out.png'
    frame=cv2.cvtColor(cv2.imread(decision_img),cv2.COLOR_BGR2RGB)
    frame=imutils.resize(frame,width=WIDTH,height=HEIGHT)
    frame=ImageTk.PhotoImage(Image.fromarray(frame))
    canvas.image=frame
    canvas.create_image(0,0,image=frame,anchor=NW)
def out():
    thread=threading.Thread(target=pending,args=("out",))
    thread.daemon=1
    thread.start()
    print('player is out')
def not_out():
    thread=threading.Thread(target=pending,args=("not out",))
    thread.daemon=1
    thread.start()
    print('player is not out')

root=Tk()
root.title("hiten advnced video player")
cv_img=cv2.cvtColor(cv2.imread('lords-removebg-preview.png'),cv2.COLOR_BGR2RGB)
canvas=Canvas(root,width=WIDTH,height=HEIGHT)
photo=ImageTk.PhotoImage(Image.fromarray(cv_img))
image_on_canvas=canvas.create_image(0,0,anchor=NW,image=photo)
canvas.pack()
btn=Button(root,text='<< Previous(fast)',width=50,command=partial(play,-25))
btn.pack()
btn=Button(root,text='<< Previous(slow)',width=50,command=partial(play,-5))
btn.pack()
btn=Button(root,text='>> next(fast)',width=50,command=partial(play,25))
btn.pack()
btn=Button(root,text='>> next(slow)',width=50,command=partial(play,5))
btn.pack()
btn=Button(root,text='give out',width=50,command=out)
btn.pack()
btn=Button(root,text='give not out',width=50,command=not_out)
btn.pack()

root.mainloop()
