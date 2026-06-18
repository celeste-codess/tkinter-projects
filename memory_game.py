import tkinter as tk
import random

ventana = tk.Tk()
ventana.title("Memorama")
ventana.geometry("1000x1000")
ventana.config(bg="#DBA55F")

class Crear_Tarjeta(tk.Button):

    primera = None
    segunda = None
    bloqueado = False

    #creamos los numeros del 1 al 12  y los duplicamos, barajeamos con .shuffle
    numeros_cartas = list(range(1,13)) * 2
    random.shuffle(numeros_cartas)

    #creamos columnas y filas en el ranque que queremos las hacemos variable 
    #LAS METEMOS EN UNA LISTA !!!!! y varajeamos la lista
    posiciones = []

    for fila in range (4):
            for columna in range (6):
                
                luagar_de_acomodo = (fila, columna) 
                posiciones.append(luagar_de_acomodo)

    random.shuffle(posiciones)

    def __init__(self, ventana, color_fondo ="#C0D8FF" ):

        #hacemos las variables, con crear tarjeta ya que lo que usamos pertenece a crear tarjeta y llamamos 
        # a las variables que hicimos, asignamos las que ya hicimos y con .pop las borramos y nos aseguramoes de no repetirloooo

        self.numero_de_carta = Crear_Tarjeta.numeros_cartas.pop() # es porque es informacion a la que recurrimos y necesitamos que esta en la memoria 
        lugar_en_tablero = Crear_Tarjeta.posiciones.pop() #info desechable x eso falta self
        
        super().__init__(
            ventana,
            text = "",  #self.numeros_cartas
            command= self.voltear_Tarjeta,
            width = 12,
            height = 9,
            font = ("Arial", 12),  
            bg = color_fondo,
            fg = "white",
            relief = "solid",  
        )
        self.grid(row = lugar_en_tablero[0], column = lugar_en_tablero[1], padx=12, pady=12, sticky="nsew")

    def voltear_Tarjeta(self):
        if Crear_Tarjeta.bloqueado:
            return
        if self == Crear_Tarjeta.primera:
            return

        self.config(bg = "#1F3963", fg = "white", text = str(self.numero_de_carta), font = ("Arial", 12))
                 
        if Crear_Tarjeta.primera == None:
            Crear_Tarjeta.primera = self
        else:
            Crear_Tarjeta.segunda = self
            Crear_Tarjeta.bloqueado = True
            self.after(800, self.Si_pares) #temporizador

    def Si_pares(self):
            if Crear_Tarjeta.primera.numero_de_carta == Crear_Tarjeta.segunda.numero_de_carta:
                Crear_Tarjeta.primera.config(bg = "green", fg = "white")
                Crear_Tarjeta.segunda.config(bg = "green", fg = "white")

            else:
                Crear_Tarjeta.primera.config(text = "", bg ="#C0D8FF")
                Crear_Tarjeta.segunda.config(text = "", bg ="#C0D8FF")
       
            Crear_Tarjeta.primera = None
            Crear_Tarjeta.segunda = None
            Crear_Tarjeta.bloqueado = False
                
 #def __init__(self, ventana )       

for i in range(24):
     Crear_Tarjeta(ventana) 
     
ventana.mainloop()