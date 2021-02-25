from tkinter import *

root = Tk()

#myLabel1 = Label(root, text = 'hello world!').grid(row = 1, column = 1)
#myLabel2 = Label(root, text = 'My name is Thomas Swagerman').grid(row = 0, column = 2)

def myClick():
	myLabel = Label(root, text = 'hello world!')
	myLabel.pack()

myButton = Button(root, text = "Click Me!", pady = 50, padx = 50, command = myClick, fg="blue")
myButton.pack()


root.mainloop()
