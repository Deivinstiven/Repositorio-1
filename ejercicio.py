from tkinter import *
from tkinter import messagebox

ventana = Tk()
ventana.title("Ejercicio completo")
ventana.geometry("400x400")
ventana.config(bd=25)

def cfloat(numero):
    try:
        result = float(numero)
    except:
        result = 0
        messagebox.showerror("Error", "Introduce bien los datos")

    return result

def sumar():
    resultado.set(cfloat(numero1.get()) + cfloat(numero2.get()))
    mostarresultado()

def restar():
    resultado.set(cfloat(numero1.get()) + cfloat(numero2.get()))
    mostarresultado()   

def multiplicar():
   resultado.set(cfloat(numero1.get()) + cfloat(numero2.get()))
   mostarresultado()

def dividir():
    resultado.set(cfloat(numero1.get()) + cfloat(numero2.get()))
    mostarresultado()   


def mostarresultado():
    messagebox.showinfo("Resultado", f"El resultado de la operacion es: {resultado.get()}")
    numero1.set("")
    numero2.set("")

numero1 = StringVar()
numero2 = StringVar()
resultado = StringVar()

marco = Frame(ventana,width=300, height=200)
marco.config(
    bd=5,
    padx=15,
    pady=15,
    relief=SOLID
)

marco.pack(side=TOP, anchor=CENTER)
marco.pack_propagate(False)



Label(marco, text="Primer numero: ").pack()
Entry(marco, textvariable=numero1, justify="center").pack()

Label(marco, text="Segundo numero: ").pack()
Entry(marco, textvariable=numero2, justify="center").pack()

Label(marco, text="").pack()

Button(marco, text="Sumar", command=sumar).pack(side="left", fill=X, expand=YES)
Button(marco, text="Restar", command=restar).pack(side="left",fill=X, expand=YES)
Button(marco, text="Multiplicar", command=multiplicar).pack(side="left",fill=X, expand=YES)
Button(marco, text="Dividir", command=dividir).pack(side="left",fill=X, expand=YES)


ventana.mainloop()