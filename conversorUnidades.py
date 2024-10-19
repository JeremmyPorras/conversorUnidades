import tkinter as tk
from tkinter import messagebox

# Tasa de conversión a dia 18/10/2024
USD_CRC = 513.70  

# Validar que la entrada sea un número
def validar_entrada(entrada):
    try:
        return float(entrada)
    except ValueError:
        return None  # Si no es un número retorna un error
    
# Conversión
def convertir_moneda():
    monto_usd = validar_entrada(entry_usd.get())
    
    if monto_usd is None:
        messagebox.showerror("Error", "Por favor, ingrese un monto válido en USD.")
        return
    
    monto_crc = monto_usd * USD_CRC
    label_resultado.config(text=f"{monto_usd} USD = {monto_crc:.2f} CRC")

# Limpiar
def limpiar_campos():
    entry_usd.delete(0, tk.END)
    label_resultado.config(text="")

# Salir de la ventana
def confirmar_salida():
    respuesta = messagebox.askyesno("Confirmar", "¿Estás seguro de que quieres salir?")
    if respuesta:
        ventana_principal.destroy()

# Ventana 
def ventana():
    ventana_principal.title("Conversor de USD a CRC")
    ventana_principal.geometry("400x200")  # Tamaño de la ventana

# Widgets
def crear_widgets():
    label_usd = tk.Label(ventana_principal, text="Ingrese monto en USD:")
    label_usd.grid(row=0, column=0, padx=10, pady=10)
    
    entry_usd.grid(row=0, column=1, padx=10, pady=10)
    
    # Botón_conversión
    boton_convertir = tk.Button(ventana_principal, text="Convertir", command=convertir_moneda)
    boton_convertir.grid(row=1, column=0, padx=10, pady=10)
    
    # Botón_limpiar
    boton_limpiar = tk.Button(ventana_principal, text="Limpiar", command=limpiar_campos)
    boton_limpiar.grid(row=1, column=1, padx=10, pady=10)
    
    # Resultado
    label_resultado.grid(row=2, column=0, columnspan=2, padx=10, pady=10)

ventana_principal = tk.Tk()
ventana()

entry_usd = tk.Entry(ventana_principal)
label_resultado = tk.Label(ventana_principal, text="")

crear_widgets()

# Cierre de la ventana
ventana_principal.protocol("WM_DELETE_WINDOW", confirmar_salida)

# Iniciar aplicación
ventana_principal.mainloop()