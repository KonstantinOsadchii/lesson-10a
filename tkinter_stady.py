import tkinter as tk
def change_text_label():
    global a
    a -= 1
    label['text'] = chr(a)
a = 128510
window = tk.Tk()
label = tk.Label(text=chr(a), bg='yellow', font='Arial 64')
label.pack()
button = tk.Button(text = 'нажми')
button.config(command = change_text_label)
button.pack()
#print(type(label))
window.mainloop()
