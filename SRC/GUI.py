# gui.py
import tkinter as tk
from tkinter import messagebox
from PIL import Image, ImageTk
import os

from SRC import UTILS

def fight_button_click():
    name1 = entry_name1.get()
    name2 = entry_name2.get()

    if name1 == "" or name2 == "":
        messagebox.showwarning("Chyba", "Zadejte prosím obě jména zápasníků.")
        return

    sound_file = os.path.join("assets", "bruce.mp3")
    UTILS.play_sound(sound_file)

    result = UTILS.generation_result(name1, name2)

    result_window = tk.Toplevel(root)
    result_window.title("Výsledek zápasu")

    label_result = tk.Label(result_window, text=result, font=("Helvetica", 14))
    label_result.pack(padx=20, pady=20)

    image_file = os.path.join("assets", "logo.png")
    image = Image.open(image_file)
    image = image.resize((200, 200), Image.ANTIALIAS)
    image = ImageTk.PhotoImage(image)

    label_image = tk.Label(result_window, image=image)
    label_image.pack(pady=20)

    label_image.image = image

root = tk.Tk()
root.title("MMA Simulator")

image_file = os.path.join("assets", "logo.png")
image = Image.open(image_file)
image = image.resize((200, 200), Image.LANCZOS)
image = ImageTk.PhotoImage(image)
label_image = tk.Label(root, image=image)
label_image.pack(pady=20)

label_name1 = tk.Label(root, text="Zápasník 1:")
label_name1.pack(pady=(20, 5))

entry_name1 = tk.Entry(root)
entry_name1.pack()

label_name2 = tk.Label(root, text="Zápasník 2:")
label_name2.pack(pady=(20, 5))

entry_name2 = tk.Entry(root)
entry_name2.pack()

button_fight = tk.Button(root, text="FIGHT!", command=fight_button_click)
button_fight.pack(pady=20)

label_image.image = image

root.mainloop()
