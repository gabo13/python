#-*- coding: Utf-8 -*-

from Tkinter import *
from random import randrange

class LottoCanvas(Canvas):
    """Lotto diagram 90 elemü tömbhöz"""
    def __init__(self, boss=None, w_=200, h_=150):
        Canvas.__init__(self)
        self.configure(width= w_, height=h_)
        self.width_, self.height_ = w_, h_
        self.create_line(10, h_-5, w_, h_-5, arrow=LAST)
        self.create_line(10, h_-5, 10, 5, arrow=LAST)
        self.bind("<Button-1>", self.mouseDown)
        self.bind("<ButtonRelease-1>", self.mouseUp)
        
    def setValueLabel(self, label=None):
        """ Add Label to show value"""
        self.valuelabel= label

    def drawGraph(self, l=None, color='red'):
        """Draw graphics"""
        self.color = color
        self.l = l
        self.lines=[]
        if self.l and len(self.l)<self.width_-5:
            for i in range(len(self.l)):
                self.lines.append(self.create_line(i*2+11, self.height_-5, i*2+11, self.height_-(5+self.l[i]), fill=color, width=2))

    def mouseDown(self, event):
        """Mouse Button-1 event handler"""
        if event.x > 11 and event.x < len(self.l)*2+11:
            self.index = int((event.x-11)/2)
            #print(self.l[self.index])
            self.itemconfigure(self.lines[self.index],fill = 'green')
            if self.valuelabel !=None:
                self.valuelabel.configure(
                text='index: '+str(self.index+1)+', '+'value: '+str(self.l[self.index]))
    def mouseUp(self, event):
        """Mouse ButtonRelease-1 event handler"""
        self.itemconfigure(self.lines[self.index], fill = self.color)


class lottoStatistic():
    def __init__(self, l, boss=None, title='Title'):
        self.label=Label(boss, text=title)
        self.label.pack()
        self.canvas=LottoCanvas(boss)
        self.canvas.pack()
        self.value=Label(boss, text='value')
        self.value.pack()
        self.canvas.setValueLabel(self.value)
        self.canvas.drawGraph(l)
# run module
if __name__ == '__main__':
    l=[0]*90
    for i in range(90):
        l[i]=randrange(1,90)
    root = Tk()
    c = lottoStatistic(l, root, title="Lotto")
    root.mainloop()
