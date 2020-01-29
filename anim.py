# -*- coding:Utf-8 -*-
# animációs program
from Tkinter import *

def move():
	"a labda elmozdulása"
	global x1, y1, dx, dy, flag
	x1, y1 = x1 +dx, y1 + dy
	if x1>360:
		x1, dx, dy = 360, 0, 15
	if y1>360:
		y1, dx, dy = 360, -15, 0
	if x1<10:
		x1, dx, dy = 10, 0, -15
	if y1<10:
		y1, dx, dy = 10, 15, 0
	can1.coords(oval1, x1, y1, x1+30, y1+30)
	if flag>0:
		abl1.after(50, move)

def stop_it():
	"az animáció leáll"
	global flag
	flag =0

def start_it():
	"az animáció elindul"
	global flag
	flag = flag + 1
	if flag == 1:
		move()

# főprogram
x1, y1 = 10, 10
dx, dy = 15, 0
flag = 0

abl1 = Tk()
abl1.title("Animációs gyakorlat Tkinter-rel")

can1 = Canvas(abl1,bg='dark grey', height=400, width=400)
can1.pack(side=LEFT)
oval1 = can1.create_oval(x1,y1,x1+30,y1+30,width=2, fill='red')
Button(abl1,text='Kilép',command=abl1.quit).pack(side=BOTTOM)
Button(abl1,text='Indít',command=start_it).pack()
Button(abl1,text='Leállít',command=stop_it).pack()

abl1.mainloop()
