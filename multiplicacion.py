import tkinter

from tkinter import messagebox

def calcular():
    n1=txtnumero1.get()
    n2 = txtnumero2.get()
    if(len(n1)==0):
        messagebox.showinfo(message="ingrese el primer numero !!",title="Mensaje")
        txtnumero1.focus()
    elif(len(n2)==0):
        messagebox.showinfo(message="ingrese el segundo numero !!", title="Mensaje")
        txtnumero2.focus()
    else:
        n1=int(n1)
        n2=int(n2)
        producto = n1 * n2
        area.insert(1.0,"\nELProducto :{}".format(producto))



ventana=tkinter.Tk()
ventana.title("ventana basica")
ventana.geometry("600x500")

ventana.configure(background='green')
lblnumero1=tkinter.Label(ventana,text='Etiqueta')
lblnumero1.place(x=100,y=50)
txtnumero1=tkinter.Entry(ventana,width=20)
txtnumero1.place(x=200,y=50)


lblnumero2=tkinter.Label(ventana,text='Etiqueta')
lblnumero2.place(x=100,y=80)
txtnumero2=tkinter.Entry(ventana,width=20)
txtnumero2.place(x=200,y=80)



boton=tkinter.Button(ventana,text='Calcular', command=calcular)
boton.place(x=200,y=120)

area=tkinter.Text(ventana)
area.config(width=30,height=10,font=("Consola",12),padx=15,pady=15,selectbackground="red")
area.place(x=100,y=150)

paises=tkinter.StringVar(ventana)
paises.set("----------")
combo=tkinter.OptionMenu(ventana,paises,"----------","Peru","Chile","Mexico")
combo.place(x=100,y=480)





ventana.mainloop()


