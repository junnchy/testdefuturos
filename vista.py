from tkinter import ttk
from tkinter import *
import pandas as pd
import matplotlib.pyplot as plt
from tkinter import messagebox

from prueba import armarListadoDeTrades
from prueba import getListaSimbolos



def main():

    root = Tk()
    app = Ventana1(root)

class Ventana1:

    def __init__(self, master):

        self.master = master
        self.master.title('Precios de Futuros')
        self.master.geometry('500x400+0+0')
        self.mercado = 'DODic19'
        self.trades = armarListadoDeTrades(self.mercado)
        self.symbols = getListaSimbolos()


        #=====================================Treeview===========================================================
        self.tv = ttk.Treeview(self.master)
        self.tv['show'] = 'headings'

        self.tv["columns"]=("one","two")

        vsb = ttk.Scrollbar(self.tv, orient="vertical", command=self.tv.yview)
        vsb.place(x=30+355+2, y=20, height=200)

        #====================================TVColums==============================================================
        self.tv.column("one", width=200 )
        self.tv.column("two", width=100, anchor="e")
        #self.tv.column("three", width=100)
        #self.tv.column("four", width=100)

        #====================================TVHeadings===========================================================
        self.tv.heading("one", text="Fecha")
        self.tv.heading("two", text="Precio")
        #self.tv.heading("three", text="Apellido")
        #self.tv.heading("four", text="DNI")

        #===============================Prueba de insertar datos================================================

        '''
        cdNegocio = NegocioSocio()
        socios = cdNegocio.todos()

        print('Prueba')
        for s in socios:
            self.tv.insert("" , 0, values=(s.id,s.nombre,s.apellido,s.dni))

        self.tv.pack()
        '''

        self.listar()


        self.frame = Frame(self.master, bg='gray')
        self.frame.pack()

        self.tv.bind('<ButtonRelease-1>', self.selectItem)

        #====================================Variables===========================================================



        #=====================================Frames================================================================

        self.buscador = Frame(self.frame, width= 300, height= 50)
        self.buscador.grid(row=0, column=1)

        self.detalleI = Frame(self.frame, width= 300, height= 50)
        self.detalleI.grid(row=1, column=1)

        self.listado = Frame(self.frame, width= 300, height= 50)
        self.listado.grid(row=2, column=1)

        self.botones = Frame(self.frame, width= 100, height = 50, relief='ridge', bd= 2)
        self.botones.grid(row=5, column=1)

        #======================================Labels=================================================================
        self.datoOp = Label(self.detalleI, text='Instrumento: ')
        self.datoOp.grid(row= 0, column=0)

        self.datoOp2 = Label(self.detalleI, text=self.mercado)
        self.datoOp2.grid(row= 0, column=2)

        #===========================================Botones============================================================

        self.btnDetalles = Button(self.botones, text='Detalles', command = lambda: self.showDetails())
        self.btnDetalles.grid(row=1, column= 1)

        self.btnGraficar = Button(self.botones, text='Graficar', command = lambda: self.plot(self.trades))
        self.btnGraficar.grid(row=1, column= 2)

        self.btnSalir = Button(self.botones, text='Salir', background= 'red', command = self.master.destroy)
        self.btnSalir.grid(row=1, column= 3)

        #=====================================Buscador===========================================================
        self.comboExample = ttk.Combobox(self.buscador,
                                    values= self.symbols
                                    )
        print(dict(self.comboExample))
        self.comboExample.grid(column=0, row=1)
        self.comboExample.current(1)

        self.comboExample.bind("<<ComboboxSelected>>", self.callbackFunc)

        print('Valor del combo: ', self.comboExample.get())


        self.master.mainloop()

    def showDetails(self):
        self.new_window()

    def listar(self):

        self.tv.delete(*self.tv.get_children())

        print(self.trades)

        for t in self.trades['trades']:
            self.tv.insert("" , 0, values=(t['datetime'],t['price']))

        self.tv.pack()

    def selectItem(self, a):
        curItem = self.tv.focus()
        item = self.tv.item(curItem)
        self.itemAc = item['values']

    def new_window(self):
        # t es un parametro de tipo que me permite conocer por que metodo se solicito la nueva ventana
        self.newWindow = Toplevel(self.master)
        self.app = Ventana2(self.newWindow, self.itemAc, self.trades)

    def plot(self, t):
        l = pd.DataFrame(t['trades'])[['price','datetime']]
        l.plot(x = 'datetime', y ='price' )
        plt.gcf().autofmt_xdate()
        plt.show()

    def callbackFunc(self, event):
        print("New Element Selected")
        print('Valor del combo: ', self.comboExample.get())
        self.mercado = self.comboExample.get()
        self.trades = armarListadoDeTrades(self.mercado)
        self.listar()

        self.datoOp2.destroy()

        self.datoOp2 = Label(self.detalleI, text=self.mercado)
        self.datoOp2.grid(row= 0, column=2)




class Ventana2:

    def __init__(self, master, itemA, trades):
        self.master = master
        self.master.title('Detalle')
        self.master.geometry('450x200')
        self.frame = Frame(self.master)
        self.frame.pack()
        self.trades = trades

        if itemA != None:
            self.itemA = itemA


        #====================================Variables===========================================================

        #=====================================Frames================================================================
        self.muestraDatos = Frame(self.frame, width= 100, height = 50, relief='ridge', bd= 2)
        self.muestraDatos.grid(row= 2, column=0)

        self.etiquetas = Frame(self.muestraDatos, width= 100, height = 50,)
        self.etiquetas.grid(row= 1, column=1)

        self.botones = Frame(self.frame, width= 100, height = 50)
        self.botones.grid(row= 12, column=0)

        #=======================================Botones================================================================

        self.btnSalir = Button(self.botones, text='Cancelar', background= 'red', command = self.master.destroy)
        self.btnSalir.grid(row=0, column= 2)

        #=====================================Etiquetas==========================================================

        self.mostrarDetales()


    def buscarDetalles(self):
        for t in self.trades['trades']:
            print(t)
            print(t['datetime'])
            if t['datetime'] == self.itemA[0]:
                print('Datos del registro actual: ', t)
                return t
            else:
                pass

    def mostrarDetales(self):
        if self.itemA != None:
            d = self.buscarDetalles()

            self.etDate = Label(self.etiquetas, text= 'Fecha de la Operacion:',)
            self.etDate.config(font=("Arial", 11, 'bold'))
            self.etDate.grid(row=1, column= 0)
            self.etDate2 = Label(self.etiquetas, text= d['datetime'], )
            self.etDate2.config(font=("Arial", 11))
            self.etDate2.grid(row=1, column= 1)

            self.etPrice = Label(self.etiquetas, text= 'Precio:', )
            self.etPrice.config(font=("Arial", 11, 'bold'))
            self.etPrice.grid(row=2, column= 0)
            self.etPrice2 = Label(self.etiquetas, text= d['price'], )
            self.etPrice2.config(font=("Arial", 11))
            self.etPrice2.grid(row=2, column= 1)

            self.etSvT = Label(self.etiquetas, text= 'Tiempo de Servidor:', )
            self.etSvT.config(font=("Arial", 11, 'bold'))
            self.etSvT.grid(row=3, column= 0)
            self.etSvT2 = Label(self.etiquetas, text= d['servertime'], )
            self.etSvT2.config(font=("Arial", 11))
            self.etSvT2.grid(row=3, column= 1)

            self.etSimbol = Label(self.etiquetas, text= 'Simbolo:', )
            self.etSimbol.config(font=("Arial", 11, 'bold'))
            self.etSimbol.grid(row=4, column= 0)
            self.etSimbol2 = Label(self.etiquetas, text= d['symbol'], )
            self.etSimbol2.config(font=("Arial", 11))
            self.etSimbol2.grid(row=4, column= 1)

main()
