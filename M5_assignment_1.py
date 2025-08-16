import tkinter as tk



root = tk.Tk()

frm1 = tk.Frame()
frm2 = tk.Frame()
frm3 = tk.Frame()
lbl1 = tk.Label(frm1, text = 'Имя:',  width = 10, justify = 'center')
lbl2 = tk.Label(frm2, text = 'Фамилия:', width = 10, justify = 'center')
lbl3 = tk.Label(frm3, text = 'Отчество:', width = 10, justify = 'center')
txt1 = tk.Text(frm1, width = 20, height = 1)
txt2 = tk.Text(frm2, width= 20, height=1)
txt3 = tk.Text(frm3, width=20, height=1)
btn1 = tk.Button(frm1, text = 'подтвердите ввод')
btn2 = tk.Button(frm2, text = 'подтвердите ввод')
btn3 = tk.Button(frm3, text = 'подтвердите ввод')

frm1.pack()
lbl1.pack(side='left')
txt1.pack(side = 'left')
btn1.pack(side='left')

frm2.pack()
lbl2.pack(side = 'left')
txt2.pack(side ='left')
btn2.pack(side='left')

frm3.pack()
lbl3.pack(side ='left')
txt3.pack(side = 'left')
btn3.pack(side='left')

root.mainloop()