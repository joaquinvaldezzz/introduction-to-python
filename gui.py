import tkinter as tk

window = tk.Tk()
window.geometry("400x400")

greeting = tk.Label(text="Hello, Tkinter")

greeting.pack()
window.mainloop()
