import tkinter as tk

def calcular_resultado():
    valor_a = float(entry_a.get())
    valor_b = float(entry_b.get())
    resultado=0
    for x in range(int(valor_b)):
        resultado+=valor_a

    resultado_label.config(text="Resultado: " + str(resultado))

# Crear la ventana
ventana = tk.Tk()
ventana.title("Calculadora")

# Etiqueta y campo de escritura para A
label_a = tk.Label(ventana, text="A:")
label_a.grid(row=0, column=0, padx=5, pady=5)
entry_a = tk.Entry(ventana)
entry_a.grid(row=0, column=1, padx=5, pady=5)

# Etiqueta y campo de escritura para B
label_b = tk.Label(ventana, text="B:")
label_b.grid(row=1, column=0, padx=5, pady=5)
entry_b = tk.Entry(ventana)
entry_b.grid(row=1, column=1, padx=5, pady=5)

# Etiqueta para mostrar el resultado
resultado_label = tk.Label(ventana, text="Resultado:")
resultado_label.grid(row=2, column=0, columnspan=2, padx=5, pady=5)

# Botón para ejecutar el ejercicio1
boton_ejecutar = tk.Button(ventana, text="Ejercicio 1", command=calcular_resultado)
boton_ejecutar.grid(row=3, column=0, columnspan=2, padx=5, pady=5)

# Botón para ejecutar el ejercicio2
boton_ejecutar = tk.Button(ventana, text="Ejercicio 2", command=calcular_resultado)
boton_ejecutar.grid(row=3, column=1, columnspan=2, padx=20, pady=5)

# # Botón para ejecutar el ejercicio3
# boton_ejecutar = tk.Button(ventana, text="Ejercicio 3", command=calcular_resultado)
# boton_ejecutar.grid(row=3, column=2, columnspan=6, padx=5, pady=5)
#
# # Botón para ejecutar el ejercicio4
# boton_ejecutar = tk.Button(ventana, text="Ejercicio 4", command=calcular_resultado)
# boton_ejecutar.grid(row=3, column=3, columnspan=8, padx=5, pady=5)
#
# # Botón para ejecutar el ejercicio5
# boton_ejecutar = tk.Button(ventana, text="Ejercicio 5", command=calcular_resultado)
# boton_ejecutar.grid(row=3, column=4, columnspan=2, padx=5, pady=5)
#
# # Botón para ejecutar el ejercicio6
# boton_ejecutar = tk.Button(ventana, text="Ejercicio 6", command=calcular_resultado)
# boton_ejecutar.grid(row=3, column=5, columnspan=2, padx=5, pady=5)



# Ejecutar la ventana
ventana.mainloop()
