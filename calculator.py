import tkinter as tk

#funciones y clases
class hacerBoton(tk.Button):
    def __init__(self, ventana, texto, comando, fila, columna, color_fondo="#525254"):
        super().__init__(
            ventana, 
            text=texto, 
            command = comando,           
            width=5, 
            height=2, 
            font=("Arial", 14, "bold"),
            bg=color_fondo, # Usará el gris O el que tú decidas mandar
            fg="white",     
            relief="flat"
        )
        self.grid(row=fila, column=columna, padx=5, pady=5, sticky="nsew")
#MiBoton(DondeVa, "Texto", Función_Al_Presionar, Fila, Columna, color si quieres cambiarlo )

#para sacar a pantalla y limpiar
class Pantalla_Calculadora(tk.Label):
    def __init__(self, ventana):

        super().__init__(
            ventana,
            text="0",
            bg="#778271",
            font=("Arial", 24),
            anchor="e",
            fg="black"
        )
        self.place(x=30, y=80, width=440, height=130)
    
    def mostrarEnPantalla(self, valor_del_boton):
        if valor_del_boton != " ":
            texto_actual = self.cget("text")

            if texto_actual == "0":
                texto_actual = ""

        self.config(text = texto_actual + valor_del_boton)

    def calcular(self):
        texto_a_resolver = self.cget("text")
        resultado = eval(texto_a_resolver)  ##eval hace lo de la suma resta y de mas 
        self.config(text=str(resultado))

    def limpiar(self):
        self.config(text="0")

#basess
ventana = tk.Tk()
ventana.title("CalculadoraPro")
ventana.geometry("500x730")
ventana.config(bg= "#2E2E2E")

# creamos el objetoooo
pantalla = Pantalla_Calculadora(ventana)
#
# donde contener los botones y que se camufle para facilital el grill
contenedor_botones = tk.Frame(ventana, bg="#2E2E2E")
contenedor_botones.place(x=30, y=250, width=440, height=400)

#Generales
hacerBoton(contenedor_botones, "7", lambda: pantalla.mostrarEnPantalla("7"), 0, 1)
hacerBoton(contenedor_botones, "8", lambda: pantalla.mostrarEnPantalla("8"), 0, 2)
hacerBoton(contenedor_botones, "9", lambda: pantalla.mostrarEnPantalla("9"), 0, 3)
hacerBoton(contenedor_botones, "4", lambda: pantalla.mostrarEnPantalla("4"), 1, 1)
hacerBoton(contenedor_botones, "5", lambda: pantalla.mostrarEnPantalla("5"), 1, 2)
hacerBoton(contenedor_botones, "6", lambda: pantalla.mostrarEnPantalla("6"), 1, 3)
hacerBoton(contenedor_botones, "1", lambda: pantalla.mostrarEnPantalla("1"), 2, 1)
hacerBoton(contenedor_botones, "2", lambda: pantalla.mostrarEnPantalla("2"), 2, 2)
hacerBoton(contenedor_botones, "3", lambda: pantalla.mostrarEnPantalla("3"), 2, 3)
hacerBoton(contenedor_botones, "0", lambda: pantalla.mostrarEnPantalla("0"), 3, 1)
hacerBoton(contenedor_botones, ".", lambda: pantalla.mostrarEnPantalla("."), 3, 2)

#especificos
hacerBoton(contenedor_botones, "C", lambda: pantalla.limpiar(), 3, 0, "orange")
hacerBoton(contenedor_botones, "=", lambda: pantalla.calcular(), 3, 3, "#181818")

#operadores
hacerBoton(contenedor_botones, "%", lambda: pantalla.mostrarEnPantalla("/"), 0, 4,  "#181818")
hacerBoton(contenedor_botones, "x", lambda: pantalla.mostrarEnPantalla("*"), 1, 4,  "#181818")
hacerBoton(contenedor_botones, "-", lambda: pantalla.mostrarEnPantalla("-"), 2, 4,  "#181818")
hacerBoton(contenedor_botones, "+", lambda: pantalla.mostrarEnPantalla("+"), 3, 4,  "#181818")
###
ventana.mainloop()