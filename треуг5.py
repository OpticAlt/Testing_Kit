import tkinter as tk
from tkinter import ttk
from tkinter import messagebox


def check_triangle():
    try:
        side1 = int(entry1.get())
        side2 = int(entry2.get())
        side3 = int(entry3.get())

        # чтобы проверить, что треугольник существует
        if side1 + side2 > side3 and side1 + side3 > side2 and side2 + side3 > side1:
            if side1 == side2 == side3:
                result = "Равносторонний треугольник"
                if side1 == 6 and side2 == 6 and  side3 == 6:
                    result = "Адский треугольник"
                if side1 == 7 and side2 == 7 and side3 == 7:
                    result = "Треугольник, благословляющий на удачу в Ваших начинаниях"

            elif side1 == side2 or side2 == side3 or side1 == side3:
                result = "Равнобедренный треугольник"
            else:
                result = "Разносторонний треугольник"
        else:
            result = "Треугольник не существует"
    except ValueError:
        result = "Пожалуйста, введите корректные числовые значения для сторон треугольника."

    # Создал всплывающее окно с результатом
    messagebox.showinfo("Результат", result)

# Создал главное окно
root = tk.Tk()
root.title("Проверка треугольника")
root.geometry("400x300")  # Задать размер окна

# Настроил стиль для виджетов
style = ttk.Style()
style.configure("TFrame", background="#008CBA")
style.configure("TLabel", background="#008CBA", foreground="white", font=("Arial", 12))
style.configure("TButton", background="#4CAF50", foreground="white", font=("Arial", 12))

# Создал и разместил фрейм для ввода
entry_frame = ttk.Frame(root)
entry_frame.pack(fill=tk.BOTH, expand=True, padx=20, pady=20)

label1 = ttk.Label(entry_frame, text="Сторона 1:")
label1.grid(row=0, column=0, padx=10, pady=5)
entry1 = ttk.Entry(entry_frame)
entry1.grid(row=0, column=1, padx=10, pady=5)

label2 = ttk.Label(entry_frame, text="Сторона 2:")
label2.grid(row=1, column=0, padx=10, pady=5)
entry2 = ttk.Entry(entry_frame)
entry2.grid(row=1, column=1, padx=10, pady=5)

label3 = ttk.Label(entry_frame, text="Сторона 3:")
label3.grid(row=2, column=0, padx=10, pady=5)
entry3 = ttk.Entry(entry_frame)
entry3.grid(row=2, column=1, padx=10, pady=5)


# Создал кнопку "Проверить" и привязал к ней функцию check_triangle
check_button = ttk.Button(root, text="Проверить", command=check_triangle)
check_button.pack(padx=10, pady=10)

# Задал градиентный фон для главного окна
canvas = tk.Canvas(root, width=400, height=300)
canvas.pack()
canvas.create_rectangle(0, 0, 400, 150, fill="#008CBA", outline="#008CBA")
canvas.create_rectangle(0, 150, 400, 300, fill="#4CAF50", outline="#4CAF50")

# Запустил цикл обработки событий
root.mainloop()
