# -*- coding:Utf-8 -*-
class Application:
    def __init__(self):
        """A főablak konstruktora"""
        self.root =Tk()
        self.root.title('Szinkódok')
        self.drawResistor()
        Label(self.root, text='Írja be az ellenállás értékét ohm-ban:').grid(row = 2)
        Button(self.root, text='Mutat', command=self.changeColours).grid(row=3, sticky= W)
        Button(self.root, text='Kilép', command=self.root.quit).grid(row=3, sticky=E)
        self.entry= Entry(self.root, width=14)
        self.entry.grid(row=3)
        #0-9 érték színkódjai:
        self.cc= ['black','brown','red','orange','yellow','green','blue','purple','grey','white']
        self.root.mainloop()

    def drawResistor(self):
        """Vászon ellenállás modellel"""
        self.can = Canvas(self.root, width=250, height=100, bg='ivory')
        self.can.grid(row=1, pady=5, padx=5)
        self.can.create_line(10, 50, 240, 50, width=5)
        self.can.create_rectangle(65, 30, 185, 70, fill='light grey', width=2)
        self.line=[]
        for x in range(85,150,24):
            self.line.append(self.can.create_rectangle(x,30,x+12,70,fill='black',width=0))
            
        print("draw Resistor")

    def changeColours(self):
        """A beírt értékekenek megfelelő 3 szín kiiratása"""
        self.v1ch= self.entry.get()
        try:
            v=float(self.v1ch)
        except:
            err = 1
        else:
            err = 0
        if err == 1 or v < 10 or v > 1e11:
            self.reportError()
        else:
            li = [0]*3
            logv = int(log10(v))
            ordgr = 10**logv
            li[0] = int (v/ordgr)
            decim = v/ordgr -li[0]

            li[1] = int (decim*10+.5)

            li[2] = logv-1
            for n in range(3):
                self.can.itemconfigure(self.line[n], fill=self.cc[li[n]])
    def reportError(self):
        self.entry.configure(bg = 'red')
        self.root.after(1000, self.emptyEntry)
    def emptyEntry(self):
        self.entry.configure(bg = 'white')
        self.entry.delete(0, len(self.v1ch))
        print("changeColour")

# Főprogram:
try:
    from Tkinter import *
except ImportError:
    from tkinter import *
from math import log10
f = Application()
