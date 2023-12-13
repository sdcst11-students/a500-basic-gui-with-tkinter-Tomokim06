import tkinter as tk

window = tk.Tk()
window.title("Example")
window.geometry("315x140")

dogphoto = tk.PhotoImage(file="dog.png")
label = tk.Label(window, image=dogphoto)
bluetext = tk.Label(window,text="A cuddly little puppy! This is from the same creators who   \n brought you Keropi and Kero Kero", bg="#A3FFFF")

clientdb = tk.Label(window, text="Pochacco!")

label.grid(row=2, column=2, columnspan=5, rowspan=3)
clientdb.grid(row=2, column=4, columnspan=5, rowspan=3)
bluetext.grid(row=5, column=3, columnspan=5, rowspan=3)

window.mainloop()