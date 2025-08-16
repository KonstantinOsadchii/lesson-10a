import tkinter as tk

root = tk.Tk()
root.title('Калькулятор')

lbl1 = tk.Label(text = 'Введите три числа и нажмите на кнопку для произвения вычислений')
txt1 = tk.Text(width = 20, height = 1)
txt2 = tk.Text(width= 20, height=1)
txt3 = tk.Text(width=20, height=1)
btn1 = tk.Button(text = 'Сложить  три числа')
btn2 = tk.Button(text = 'Умножить ти числа')

lbl1.pack()
txt1.pack()
txt2.pack()
txt3.pack()
btn1.pack()
btn2.pack()

root.mainloop()