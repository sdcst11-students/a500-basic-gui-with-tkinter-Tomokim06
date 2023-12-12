import tkinter as tk

window = tk.Tk()
window.title("T-Town veterinary Clinic Database ")
window.geometry("565x190")

dogphoto = tk.PhotoImage(file="dog.png")
button1 = tk.Button(window,text="Search by Name")
textbox = tk.Entry(window, width=10)
button2 = tk.Button(window,text="< Previous")
button3 = tk.Button(window,text="Next >")

label = tk.Label(window, image=dogphoto)

text1 = tk.Label(window, text="Name")
text2 = tk.Label(window, text="Type")
text3 = tk.Label(window, text="Breed")
text4 = tk.Label(window, text="Owner")
text5 = tk.Label(window, text="Birthdate")

button1.grid(row = 1, column = 9)
button2.grid(row = 4, column = 1)
button3.grid(row = 4, column = 10)
textbox.grid(row = 1, column = 10)
label.grid(row = 1, column = 1)

text1.grid(row = 3, column = 1)
text2.grid(row = 3, column = 2)
text3.grid(row = 3, column = 3)
text4.grid(row = 3, column = 4)
text5.grid(row = 3, column = 10)

window.mainloop()

