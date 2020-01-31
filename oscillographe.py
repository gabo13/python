#-*- Coding:Utf-8 -*-
from Tkinter import *
from math import sin, pi

class OscilloGraph(Canvas):
    """kitérés görbe rajzoló vászon"""
    def __init__(self, boss=None, width_=200, height_=150):
        """Grafika konstruktora"""
        Canvas.__init__(self)
        self.configure(width=width_, height=height_)
        self.width_, self.height_ = width_, height_
        self.create_line(10, height_/2, width_, height_/2, arrow=LAST)
        self.create_line(10, height_-5, 10, 5, arrow=LAST)
        step = (width_-25)/8.
        for t in range(1,9):
            stx = 10 + t*step
            self.create_line(stx, height_/2-4, stx, height_/2+4)

    def drawCurve(self, freq=1, phase=0, ampl=10, colo='red'):
        """1sec-re eső időgörbe rajzolása"""
        curve = []
        step = (self.width_-25)/1000.
        for t in range(0,1001,5):
            e = ampl*sin(2*pi*freq*t/1000-phase)
            x = 10 + t*step
            y = self.height_/2-e*self.height_/25
            curve.append((x,y))
        n = self.create_line(curve, fill=colo, smooth=1)
        return n

if __name__ == '__main__':
    root = Tk()
    gra = OscilloGraph(root, 250, 180)
    gra.pack()
    gra.configure(bg = 'ivory', bd = 2, relief = SUNKEN)
    gra.drawCurve(2, 1.2, 10, 'purple')
    root.mainloop()
