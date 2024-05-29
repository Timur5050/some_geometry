
# -*- coding: windows-1251 -*-

import tkinter as tk
from tkinter import filedialog, messagebox
from point import Point
from line import Line


def read_from_file():
    file_path = filedialog.askopenfilename(title="������� ����",
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
                    messagebox.showerror("�������", "���� ������� ������ ���� 6 �����.")
        except Exception as e:
            messagebox.showerror("�������", f"�� ������� ������� ����: {e}")


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
            messagebox.showinfo("������ ���", f"�� �����: {numbers}")
        except ValueError:
            messagebox.showerror("�������", "�� ������ �������� ������ ���� �������.")
    else:
        messagebox.showwarning("������������", "�� ���� ������ ���� ��������!")


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
                messagebox.showinfo("����������", f"������ ��������� �� {save_path}")
            except ValueError:
                messagebox.showerror("�������", "�� ������ �������� ������ ���� �������.")
        else:
            messagebox.showwarning("������������", "�� ���� ������ ���� ��������!")


root = tk.Tk()
root.title("�������� ����� ��� �����")

entries = []
for i in range(3):
    frame = tk.Frame(root)
    frame.pack(pady=5)
    tk.Label(frame, text=f"����� {i + 1}").pack(side=tk.LEFT)
    entry_x = tk.Entry(frame, width=10)
    entry_x.pack(side=tk.LEFT, padx=5)
    entry_y = tk.Entry(frame, width=10)
    entry_y.pack(side=tk.LEFT)
    entries.extend([entry_x, entry_y])

btn_read_file = tk.Button(root, text="������� � �����", command=read_from_file)
btn_read_file.pack(pady=5)

btn_submit = tk.Button(root, text="������ ���", command=submit_data)
btn_submit.pack(pady=5)

btn_save_graphic = tk.Button(root, text="�������� ������", command=save_graphic)
btn_save_graphic.pack(pady=5)

root.mainloop()
