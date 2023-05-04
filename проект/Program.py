from tkinter import *
from tkinter import filedialog 
from tkinter.ttk import Progressbar



def clicked():
    lbl.configure(text="Редактор фото")


window = Tk()
window.title("Добро пожаловать в приложение PhotoRec")
window.geometry('400x250')


lbl = Label(window, text="PhotoRec", font=("Arial Bold", 30))
lbl.grid(column=0, row=0)


btn = Button(window, text="Редактировать фото", command=clicked)
btn.grid(column=0, row=1)


rad1 = Radiobutton(window,text='Контрастность', value=1)
rad2 = Radiobutton(window, text='Яркость', value=2)  
rad3 = Radiobutton(window, text='Размытость', value=3) 
rad1.grid(column=5, row=6)  
rad2.grid(column=4, row=6)  
rad3.grid(column=3, row=6)

file = filedialog.askopenfilename()




window.mainloop()