# -*- coding: Utf-8 -*-
try:
    from Tkinter import *
except ImportError:
    from tkinter import *
from random import randrange

class Draw(Frame):
    "A program főablakát definiáló osztály"
    def __init__(self):
        Frame.__init__(self)
        # A vászon létrehozása
        self.c = Canvas(self, width=400, height=300, bg='ivory')
        self.c.pack(padx=5, pady=3)
        for i in range(15):
            # Véletlenszerüen kisorsolunk egy színt
            coul=['brown','red','orange','yellow','green','cyan','blue','violet','purple',][randrange(9)]
            # Véletlen koordinátájú elipszis rajzolása
            x1, y1 = randrange(300), randrange(200)
            x2, y2 = x1 + randrange(10,150), y1 +randrange(10,150)
            self.c.create_oval(x1, y1, x2, y2, fill=coul)

        # Az <egéresemények hozzákapcsolása a <canvas> widgethez
        self.c.bind("<Button-1>", self.mouseDown)
        self.c.bind("<Button1-Motion>", self.mouseMove)
        self.c.bind("<Button1-ButtonRelease>", self.mouseUp)
        # A kilépésgomb létrehozása
        b_fin = Button(self, text='Befejezés', bg='royal blue', fg='white',  font=('Helvetica',10,'bold'), command=self.quit)
        b_fin.pack(pady=2)
        self.pack()

    def mouseDown(self, event):
        "Bal egérgomb lenyomására végrehajtandó művelet"
        self.currObject = None
        self.x1, self.y1 = event.x, event.y
        self.selObject = self.c.find_closest(self.x1, self.y1)
        self.c.itemconfig(self.selObject, width=3)
        self.c.lift(self.selObject)

    def mouseMove(self, event):
        "Lenyomott bal gomb mozgó egérrel végrehajtandó művelet"
        x2, y2 = event.x, event.y
        dx, dy = x2-self.x1, y2-self.y1
        if self.selObject:
            self.c.move(self.selObject, dx, dy)
            self.x1, self.y1 = x2, y2

    def mouseUp(self, event):
        "A bal egérgomb fölengedésekor végrehajtandó művelet"
        if self.selObject:
            self.c.itemconfig(self.selObject, width=1)
            self.selObject = None

if __name__ == '__main__':
    Draw().mainloop()
