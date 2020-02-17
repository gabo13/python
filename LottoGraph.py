# -*- Coding:Utf-8 -*-
# Lotto graphics application
# Created by Horváth Gábor
# Hungary
# 2020. 02. 01.

import urllib
from Tkinter import *

class MainFrame(Frame):
    def __init__(self):
        Frame.__init__(self)
        
        T = Text(self, height=2, width=10)
        
        T.pack()
        T.insert(END, 'This is a text')
        

class LottoGraph():

    
    
    def __init__(self):
        URL = 'https://bet.szerencsejatek.hu/cmsfiles/otos.csv'
        self.data = []
        
        with open('otos.csv','wb') as f:
            f.write(urllib.urlopen(URL).read())
            f.close()

        

        with open('otos.csv','r') as f:
            for line in f:
                temp = list(line.rstrip().split(';'))
                temp2 = map(int,temp[0:2]+temp[11:15])
                self.data.append(temp2)
            f.close()

        #self.show()

    def show(self):
        print(self.data)
        #for lista in data:
            #print(' '.join(map(str,lista)))


if __name__ == '__main__':
    LottoGraph()
    mf=MainFrame()
    mf.mainloop()
