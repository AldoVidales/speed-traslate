
from tkinter import *
from tkinter import ttk


class ventana3:
    def __init__(self):
        self.title="Speed traslate 2021"
        self.size="770x470"
        self.resiable=False
        self.icon='imagenes\internet-speed.ico'
        
        
    
    def suma(self):

     try: 
        self.suma= int(self.E1.get())*(1/1000)*(3600/1)
        return self.var.set(self.suma)

     except:
         print("No se pudo sorry") 

        


  


    def vol(self):
        try:
            self.volumen= int(self.Entry_Volumen.get())*(0.00026417205235815)
            print(self.volumen)
            return self.var2.set(self.volumen)
        except:
            print("No se pudo sorry")
    
        

    def cargar(self):
        


        self.ventana=Tk()
        self.ventana.title(self.title)
        self.ventana.geometry(self.size)
        self.ventana.resizable(0,0)
        self.ventana.iconbitmap(self.icon)
        self.var=StringVar()
        self.var2=StringVar()
        titulo=Label(self.ventana,text="Convertidor")
        titulo.pack(padx=10,pady=10)
        co2=Label(self.ventana, text="km/h")
        co2.pack(padx=10,pady=10)
        co=Label(self.ventana, text="m/s")
        co.pack(padx=10,pady=10)
        

        self.E1 = Entry(self.ventana)
        self.E1.pack(padx=10,pady=10)
        # entry1=Entry(self.ventana,text=12)
        # entry1.place(x=50,y=20)
        # oky=Button(self.ventana,text="OK",command=self.convertir)
        # oky.pack()

        oky=Button(self.ventana,text="OK",command=self.suma,)
        oky.pack(padx=10,pady=10)


        self.eq=Label(self.ventana,textvariable=self.var)
           
        self.eq.pack(padx=10,pady=10)



        self.volumen=Label(self.ventana,text="Convertir cm3 a Galones")
        self.volumen.pack(padx=10,pady=10)


        self.Entry_Volumen=Entry(self.ventana)
        self.Entry_Volumen.pack (padx=10,pady=10)
        oky2=Button(self.ventana,text="OK",command=self.vol)
        oky2.pack(padx=10,pady=10)
        self.eq2=Label(self.ventana,textvariable=self.var2)
        self.eq2.pack(padx=10,pady=10)


       
    
        self.ventana.mainloop()


        
        

   
            


           






