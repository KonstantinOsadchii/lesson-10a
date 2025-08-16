import tkinter as tk
def change_text_label():
    global agit
    a += 1
    label['text'] = chr(a)
def get_text (entry_name):
    text_from_entry = entry_name.get()
    print(text_from_entry)

a = 128510
print ('start')
window = tk.Tk()
window.geometry('560x368')
w = window.winfo_screenwidth()
h = window.winfo_screenheight()
print(w, 'x', h)
frame = tk.Frame()
frame.pack()
frame2 = tk.Frame()
frame2.pack()
label = tk.Label(frame, text=chr(a), bg='yellow', font='Arial 64')
label.pack()
entry1 = tk.Entry(frame)
entry1.pack()
entry2 = tk.Entry(frame2)
entry2.pack()
button = tk.Button(frame, text = 'нажми')
button.config(command = change_text_label)
button.pack()
print(a)
window.mainloop()
