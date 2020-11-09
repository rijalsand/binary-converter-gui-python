from tkinter import *
root = Tk()
root.title("Binary Converter")
root.geometry('200x200')
e = Entry(root, width = 10, )
e.pack()
def function():
	try:

		y=int(e.get())
		
		x= bin(y)
		label = Label(root,text=x)
		label.pack()
	except ValueError:
		print("Please Enter Number")

 

btn = Button(root, text='Enter'  ,command=function)
btn.pack()


	
root.mainloop()
