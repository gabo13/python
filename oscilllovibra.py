# -*- Coding:Utf-8 -*-

from choicevibra import *
from oscillographe import *

class ShowVibra(Frame):
    def __init__(self, boss=None):
        Frame.__init__(self)
        self.colour = ['dark green', 'red', 'purple']
        self.trace = [0]*3
        self.control = [0]*3

        self.gra = OscilloGraph(self, width_=400, height_=200)
        self.gra.configure(bg='white', bd=2, relief=SOLID)
        self.gra.pack(side=TOP, pady=5)

        for i in range(3):
            self.control[i] = ChoiceVibra(self, self.colour[i])
            self.control[i].pack()

        self.master.bind('<Control-Z>', self.showCurves)
        self.master.title('Harmónikus rezgőmozgások')
        self.pack()

    def showCurves(self, event):

        for i in range(3):
            self.gra.delete(self.trace[i])

            if self.control[i].chk.get():
                self.trace[i] = self.gra.drawCurve(
                    colo = self.colour[i],
                    freq = self.control[i].freq,
                    phase = self.control[i].phase,
                    ampl = self.control[i].ampl)

if __name__ == '__main__':
    ShowVibra().mainloop()
