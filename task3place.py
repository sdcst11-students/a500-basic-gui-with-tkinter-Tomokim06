import tkinter as tk

window = tk.Tk()
window.title("Example")
window.geometry("315x140")

dogphoto = tk.PhotoImage(file="dog.png")
label = tk.Label(window, image=dogphoto)
bluetext = tk.Label(window,text="A cuddly little puppy! This is from the same creators who   \n brought you Keropi and Kero Kero", bg="#A3FFFF")

clientdb = tk.Label(window, text="Pochacco!")

label.place(x=90, y=1)
clientdb.place(x= 170, y=50)
bluetext.place(x=1, y=105)

window.mainloop()