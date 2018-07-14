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
   
def reset():
    file = open('mather.txt','w')
    file.write('0')
    file = open('winthrop.txt','w')
    file.write('0')
    file = open('lowell.txt','w')
    file.write('0')
    file = open('log.txt','w')
    file.write("")
    file.close()

def exit():
    window.destroy()

def showLog():
    logWindow = Tk()
    logWindow.title('log')
    file = open('log.txt','r')
    text = Text(logWindow,font = 'Arial,12',height = 20, width = 25 )
    text.grid(row = 0, column = 0)
    line = ''
    for i in file:
        line += i
        text.delete(0.0,END)
        text.insert(END,line)
    line = ''
    logWindow.mainloop()

def getTotal():
    if(v.get() == 'Lowell'):
        file = open('lowell.txt','r')
        
    if(v.get() == 'Mather'):
        file = open('mather.txt','r')

    if(v.get() == 'Winthrop'):
        file = open('winthrop.txt','r')
        
    t = file.readline()
    totalLabel = Label(window,text = t, font = 'Arial,12')
    totalLabel.grid(row = 3, column = 1)


t = StringVar()
x = StringVar()
v = StringVar(window)
v.set(options[0])
t = open('lowell.txt','r').readline()
optionMenu = OptionMenu(window,v,*options)
optionMenu.grid(row = 1, column = 0, sticky = W)

pointEntry = Entry(window, width = 5)
pointEntry.grid(row = 1, column = 1)

textEntry = Entry(window, width = 10)
textEntry.grid(row = 2, column = 0, sticky = W)

goButton = Button(window,text = 'Write',command = writeFile)
goButton.grid(row = 2, column = 1)

logButton = Button(window,text = 'Log', command = showLog)
logButton.grid(row = 1, column = 2)

totalButton = Button(window,text = 'get total', command = getTotal)
totalButton.grid(row = 3, column = 0)

totalLabel = Label(window,text = t, font = 'Arial,12')
totalLabel.grid(row = 3, column = 1)


resetButton = Button(window, text = 'Reset', command = reset)
resetButton.grid(row = 2, column = 2)


window.mainloop()
