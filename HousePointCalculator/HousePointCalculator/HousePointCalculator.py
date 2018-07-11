import tkinter
from tkinter import *

options = ['Lowell','Mather','Winthrop']
window = Tk()
window.title('House point calculator')

def writeFile():
    
    if(v.get() == 'Lowell'):
       
        file1 = open('lowell.txt','r')
        firstLine = file1.readline()
        x.set(firstLine)
        total = int(x.get())  
        file = open('lowell.txt','w')

    if(v.get() == 'Mather'):

        file1 = open('mather.txt','r')
        firstLine = file1.readline()
        x.set(firstLine)
        total = int(x.get())    
        file = open('mather.txt','w')
        
    if(v.get() == 'Winthrop'):

        file1 = open('winthrop.txt','r')
        firstLine = file1.readline()
        x.set(firstLine)
        total = int(x.get())  
        file = open('winthrop.txt','w')
        
    file1.close()
    file.write(str(total + int(pointEntry.get())))
    file.close()

    file = open('log.txt','a')
    if(int(pointEntry.get()) >= 0):
        file.write(v.get() + ' won ' + pointEntry.get() + ' points for ' + textEntry.get() + '\n')
    if(int(pointEntry.get()) < 0):
        file.write(v.get() + ' lost ' + str(abs(int(pointEntry.get()))) + ' points for ' + textEntry.get() + '\n')
   
x = StringVar()
v = StringVar(window)
v.set(options[0])
optionMenu = OptionMenu(window,v,*options)
optionMenu.grid(row = 1, column = 0, sticky = W)

pointEntry = Entry(window, width = 5)
pointEntry.grid(row = 1, column = 1)

textEntry = Entry(window, width = 10)
textEntry.grid(row = 2, column = 0, sticky = W)

goButton = Button(window,text = 'Write',command = writeFile)
goButton.grid(row = 2, column = 1)
window.mainloop()
