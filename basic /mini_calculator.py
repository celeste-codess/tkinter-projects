import tkinter as tk

window = tk.Tk()
window.title("My Calculator")
window.geometry("400x250") 
window.config(bg="pink")


def add():
    try:
        result = float(field1.get()) + float(field2.get())
        
        if result.is_integer():
            result = int(result)
        show_result.config(text=f"Result: {result}")
    except ValueError:
        show_result.config(text='To add, only write numbers.')


def borrar():
    field1.delete(0, "end")
    field2.delete(0, "end")
    show_result.config(text="Esperando números...")


field1 = tk.Entry(window, font=("Arial", 12), bg="white", fg="black", justify="center")
field1.pack(pady=5)

field2 = tk.Entry(window, font=("Arial",12), bg="white", fg="black", justify="center")
field2.pack(pady=5)

add_button = tk.Button(window, text="Add", command=add)
add_button.pack(pady=5)

show_result = tk.Label(window, text="Esperando números...", font=("Arial",13), bg="white", fg="black")
show_result.pack(pady=5)

borrar_button = tk.Button(window, text="Borrar", command=borrar)
borrar_button.pack(pady=5)

window.mainloop()
