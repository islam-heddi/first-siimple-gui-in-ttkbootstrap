import ttkbootstrap as ttk
from ttkbootstrap.constants import *

root = ttk.Window(themename="darkly")

my_label = ttk.Label(text="hello programming", font=("arial",30),bootstyle="white")
my_label.pack(side=LEFT, padx=5, pady=10)

my_button = ttk.Button(text="Click me!",bootstyle="Default-outline-light")
my_button.pack(side=RIGHT,padx=50,pady=100)

checkme = ttk.Checkbutton(text="Ready to get job", bootstyle="Default")
checkme.pack(side=RIGHT,padx=60,pady=110)

root.mainloop()