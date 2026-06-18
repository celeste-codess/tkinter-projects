import tkinter as tk

contador = 0

def botonGeneral():
    global contador

    lista_Botones = [boton1, boton2, boton3]

    for boton in lista_Botones:
        boton.config(bg="#e6d1d1")
    
    lista_Botones[contador].config(bg= "red")

    contador = (contador + 1) % 3

ventana = tk.Tk()
ventana.title("Botones cabia colores")
ventana.geometry("500x500")
ventana.config(bg="white")

#--Botones que cambian de colores
boton1 = tk.Button(ventana, text="1", width=10, height=8, font="Arial", bg="#ffffff")
boton1.place(x=100, y=100, anchor="c")

boton2 = tk.Button(ventana, text="2", width=10, height=8, font="Arial", bg="#ffffff")
boton2.place(x=250, y=100, anchor="c")

boton3 = tk.Button(ventana, text="3", width=10, height=8, font="Arial", bg="#ffffff")
boton3.place(x=400, y=100, anchor="c")


# boton que cambia los colores
boton_Abajo = tk.Button(ventana, text= "Cambia de color", width=30, height=5, font="Arial", bg="#f6c7f5", command= botonGeneral)
boton_Abajo.place(x=250, y=400, anchor="c")

# --- 5. INICIAR EL PROGRAMA ---
ventana.mainloop()
