
# -*- coding: windows-1251 -*-

import tkinter as tk
from tkinter import filedialog, messagebox
from point import Point
from line import Line


def read_from_file():
    file_path = filedialog.askopenfilename(title="Виберіть файл",
                                           filetypes=(("Text files", "*.txt"), ("All files", "*.*")))
    if file_path:
        try:
            with open(file_path, 'r') as file:
                data = file.read().split()
                if len(data) == 6:
                    for i in range(6):
                        entries[i].delete(0, tk.END)
                        entries[i].insert(0, data[i])
                else:
                    messagebox.showerror("Помилка", "Файл повинен містити рівно 6 чисел.")
        except Exception as e:
            messagebox.showerror("Помилка", f"Не вдалося зчитати файл: {e}")


def submit_data():
    data = [entry.get() for entry in entries]
    if all(data):
        try:
            numbers = list(map(float, data))
            A = Point(numbers[0], numbers[1])
            B = Point(numbers[2], numbers[3])
            C = Point(numbers[4], numbers[5])
            line = Line(A, B)
            line.solve(C)
            line.position(C)
            messagebox.showinfo("Введені дані", f"Ви ввели: {numbers}")
        except ValueError:
            messagebox.showerror("Помилка", "Всі введені значення повинні бути числами.")
    else:
        messagebox.showwarning("Попередження", "Всі поля повинні бути заповнені!")


def save_graphic():
    save_path = filedialog.asksaveasfilename(defaultextension=".png",
                                             filetypes=(("PNG files", "*.png"), ("All files", "*.*")))
    if save_path:
        data = [entry.get() for entry in entries]
        if all(data):
            try:
                numbers = list(map(float, data))
                A = Point(numbers[0], numbers[1])
                B = Point(numbers[2], numbers[3])
                C = Point(numbers[4], numbers[5])
                line = Line(A, B)
                line.build_graphic(Line(C, C), save_path)
                messagebox.showinfo("Збереження", f"Графік збережено як {save_path}")
            except ValueError:
                messagebox.showerror("Помилка", "Всі введені значення повинні бути числами.")
        else:
            messagebox.showwarning("Попередження", "Всі поля повинні бути заповнені!")


root = tk.Tk()
root.title("Введення даних для точок")

entries = []
for i in range(3):
    frame = tk.Frame(root)
    frame.pack(pady=5)
    tk.Label(frame, text=f"Точка {i + 1}").pack(side=tk.LEFT)
    entry_x = tk.Entry(frame, width=10)
    entry_x.pack(side=tk.LEFT, padx=5)
    entry_y = tk.Entry(frame, width=10)
    entry_y.pack(side=tk.LEFT)
    entries.extend([entry_x, entry_y])

btn_read_file = tk.Button(root, text="Зчитати з файлу", command=read_from_file)
btn_read_file.pack(pady=5)

btn_submit = tk.Button(root, text="Ввести дані", command=submit_data)
btn_submit.pack(pady=5)

btn_save_graphic = tk.Button(root, text="Зберегти графік", command=save_graphic)
btn_save_graphic.pack(pady=5)

root.mainloop()
