from tkinter import *
from tkinter import messagebox

pencere = Tk()
pencere.title("Simple CSS")
pencere.geometry("1080x720")

def temizle():
    degistirilecek_yazi.delete(0, END)


def change():
    degistirilecek_yazi.delete(0, END)
    degistirilecek_yazi.insert(0, metin.get())
    metin.delete(0, END)

def goster():
    messagebox.showinfo(f"Tip: {degistirilecek_yazi}", type(degistirilecek_yazi.get()))




label = Label(pencere, text="Değiştirilecek Yazı", bg="white", fg="black", font=("Seoge UI", 14))
label.place(x=5,y=5)

button = Button(pencere, text="Değiştir", bg="purple", fg="white", font=("Seoge UI", 14), command=change)
button.place(x=5,y=125)

button2 = Button(pencere, text="Temizle", bg="purple", fg="white", font=("Seoge UI", 14), command=temizle)
button2.place(x=105,y=125)

button3 = Button(pencere, text="Tip Göster", bg="purple", fg="white", font=("Seoge UI", 14), command=goster)
button3.place(x=205,y=125)

metin = Entry(pencere, text="Heryerde ara...", font=("Consolas", 14), width=35)
metin.place(x=5,y=95)

degistirilecek_yazi = Entry(pencere, text="Heryerde ara..", font=("Consolas", 14), width=35)
degistirilecek_yazi.place(x=5,y=35)

label2 = Label(pencere, text="Yeni Yazı", bg="white", fg="black", font=("Seoge UI", 14))
label2.place(x=5,y=65)


pencere.mainloop()