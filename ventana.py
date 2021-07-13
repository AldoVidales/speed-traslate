
from tkinter import *
from tkinter import ttk


class ventana3:
    def __init__(self):
        self.title="Speed traslate 2021"
        self.size="770x470"
        self.resiable=False
        self.icon='C:/Users/aldov/Documents/Programacion/Python/Curso tkinter/imagenes\internet-speed.ico'
        
        
    
    def suma(self):

     try: 
        self.suma= int(self.E1.get())*(1/1000)*(3600/1)
        return self.var.set(self.suma)

     except:
         print("No se pudo sorry") 

        


  



    
        

    def cargar(self):
        


        self.ventana=Tk()
        self.ventana.title(self.title)
        self.ventana.geometry(self.size)
        self.ventana.resizable(0,0)
        self.ventana.iconbitmap(self.icon)
        self.var=StringVar()
        titulo=Label(self.ventana,text="Convertidor")
        titulo.grid(column=1,row=1)
        co2=Label(self.ventana, text="km/h")
        co2.grid(column=1,row=2)
        co=Label(self.ventana, text="m/s")
        co.grid(column=6,row=5)
        

        self.E1 = Entry(self.ventana)
        self.E1.grid(column=1,row=3)
        # entry1=Entry(self.ventana,text=12)
        # entry1.place(x=50,y=20)
        # oky=Button(self.ventana,text="OK",command=self.convertir)
        # oky.pack()

        oky=Button(self.ventana,text="OK",command=self.suma)
        oky.grid(column=6,row=3)


        self.eq=Label(self.ventana,textvariable=self.var)
           
        self.eq.grid(column=6,row=6)

       
    
        self.ventana.mainloop()


        
        

   
            


           






