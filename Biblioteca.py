from tkinter import *
from PIL import Image,ImageTk
import random

#----------------------------------------------------------------------------------------------------------
#codigo ventana principal

raiz = Tk()
raiz.resizable(0,0)
raiz.iconbitmap("icon.ico")
raiz.title("VIDEOJUEGOS")
raiz.config(width=800,height=600,background="black")

#----------------------------------------------------------------------------------------------------------
#codigo menu principal

def videojuegos_menu():
    menu = Frame()
    menu.config(background="black")
    menu.place(width=800,height=600)

    imagen = Image.open("biblioteca.jpg")
    imagenR = imagen.resize((510,400))
    imagenTk = ImageTk.PhotoImage(imagenR)
    
    pantalla = Label(menu,image=imagenTk)
    pantalla.image = imagenTk
    pantalla.place(x=140,y=80)

    numero_sistemas()

    Label(menu,bg="black",fg="white",text="BIBLIOTECA DE VIDEOJUEGOS",font=("Arial","20")).place(x=200,y=20)
    Label(menu,bg="black",fg="white",text="SISTEMAS TOTALES: ",font=("Arial","12")).place(x=140,y=500)
    Label(menu,text=t_s,bg="black",fg="white",font=("Arial","12")).place(x=310,y=500)
    Label(menu,bg="black",fg="white",text="JUEGOS TOTALES: ",font=("Arial","12")).place(x=450,y=500)
    Label(menu,text=juegos_totales,bg="black",fg="white",font=("Arial","12")).place(x=600,y=500)
    Button(menu,text="AÑADIR JUEGOS",justify="left",command=add_juegos).place(x=40,y=550)
    Button(menu,text="LISTAR",justify="left",command=listar_juegos).place(x=155,y=550)
    Button(menu,text="BORRAR",justify="left",command=borrar_juegos).place(x=220,y=550)
    Button(menu,text="SALIR",justify="left",command=salir_juegos).place(x=720,y=550)
    Button(menu,text="JUEGO Y CARATULA",justify="left",command=j_c).place(x=295,y=550)
    Button(menu,text="JUEGO AL HAZAR",justify="left",command=j_h).place(x=435,y=550)

#funcion para saber todos los sistemas y juegos que tienes almacenados 
def numero_sistemas():
    global t_s,juegos_totales
    index=0
    total_sistemas = []
    juegos_totales = 0

    try:
        with open ("datos.txt","r") as file:
            for f in file:
                index = index + 1
                if index == 1:
                    juegos_totales = juegos_totales + 1
                if index == 2:
                    try:
                        total_sistemas.index(f)
                    except:
                        total_sistemas.append(f)
                if index == 6:
                    index = 0
        t_s = str(len(total_sistemas))
    except:
        t_s = "0"

                
#----------------------------------------------------------------------------------------------------------
#codigo añadir juegos

def add_juegos():
    #creo la ventane de añadir juegos
    añadir = Frame()
    añadir.config(background="black",width=800,height=600)
    añadir.place(x=0,y=0)  
    
    #variables de de entrada de texto las hago globales para compartirlas con otras funciones
    global consola_entry,nombre_entry,genero_entry,imagen_entry
    global texto_text

    consola_entry = StringVar()
    nombre_entry = StringVar()
    genero_entry = StringVar()
    imagen_entry = StringVar()

    #creo el menu para añadir juegos. para insertar el juego escrito en los entris hay que pulsar grabar   
    Button(añadir,text="MENU PRINCIPAL",justify="left",command=videojuegos_menu).place(x=340,y=550)
    Button(añadir,text=" GRABAR ",justify="left",command=grabar).place(x=510,y=220)
    Label(añadir,bg="black",fg="white",text="AÑADIR VIDEOJUEGOS",font=("Arial","20")).place(x=230,y=20)
    Label(añadir,bg="black",fg="white",text="CONSOLA VIDEO JUEGOS",font=("Arial","12")).place(x=40,y=70)
    Label(añadir,bg="black",fg="white",text="JUEGO",font=("Arial","12")).place(x=40,y=100)
    Label(añadir,bg="black",fg="white",text="GENERO",font=("Arial","12")).place(x=40,y=130)
    Label(añadir,bg="black",fg="white",text="IMAGEN",font=("Arial","12")).place(x=510,y=160)
    Label(añadir,bg="black",fg="white",text="SINOPSIS",font=("Arial","12")).place(x=40,y=160)
    Entry(añadir,textvariable=consola_entry).place(x=260,y=70)
    Entry(añadir,textvariable=nombre_entry).place(x=260,y=100)
    Entry(añadir,textvariable=genero_entry).place(x=260,y=130)
    Entry(añadir,textvariable=imagen_entry).place(x=510,y=190)

    #CREO UNA VENTANA PARA AÑADIR LA DESCRIPCION DEL JUEGO DENTRO DE LA VENTANA AÑADIR   
    texto = Frame()
    texto.config(background="white")
    texto.place(x=40,y=190,width=450,height=350)
    #creo el texto dentro de la ventana texto que lo ocupa todo
    texto_text = Text(texto)
    texto_text.pack()

def grabar():
    #llamo a la funcion posicion la cual retorna el numero de indice del ultimo juego introducido, el cual en un str
    # y le sumo 1 para escribir el nuevo juego
    index = posicion()
    if index != 1:
        index = int(index)+1
        index = str(index)
    else:
        index = str(index)

    #miro cada entry para colocarlo en su variable correspondiente
    consola=consola_entry.get()
    nombre=nombre_entry.get()
    genero=genero_entry.get()
    imagen=imagen_entry.get()
    sinopsis = texto_text.get("1.0","end")
    
    #compruebo que almenos se halla introducido el nombre del juego y la consola
    if consola != "" and nombre != "":
        #abro el fichero y escribo las variables ya asignadas
        with open("datos.txt","a") as file:
            file.write(f"{index}\n")
            file.write(f"{consola}\n")
            file.write(f"{nombre}\n")
            file.write(f"{genero}\n")
            file.write(f"{imagen}\n")
            file.write(f"{sinopsis}")
            consola_entry.set("")
            nombre_entry.set("")
            genero_entry.set("")
            imagen_entry.set("")
            texto_text.delete("1.0","end")

# funcion para saber la posicion del ultimo juego
def posicion():
    index = 0
    try:
        with open("datos.txt","r") as file:
            for f in file:
                index = index + 1
                if index == 1:
                    posicion = f
                if index == 6:
                    index = 0
    except:
        posicion=1
            
    return (posicion)        

#----------------------------------------------------------------------------------------------------------
#codigo listar juegos

def listar_juegos():
    #declaro la variables del entry y del radiobutton globales para utilizarlas en otra funcion
    global varEntry,varOpcion
    
    varOpcion = IntVar()
    varEntry = StringVar()
    #creo la ventana de lista con las opciones. una vez seleccionado las opciones , cuando le das al boton listar 
    #va a la funcion listadF
    listar = Frame()
    listar.config(background="black",width=800,height=600)
    listar.place(x=0,y=0) 
    Label(listar,bg="black",fg="white",text="LISTAR VIDEOJUEGOS",font=("Arial","20")).place(x=230,y=20)
    Button(listar,text="LISTAR",command=listadoF).place(x=380,y=120)
    Label(listar,bg="black",fg="white",text="COMO QUIERES VER EL LISTADO ? :",font=("Arial","12")).place(x=30,y=70)
    Entry(listar,textvariable=varEntry,font=("Arial","12")).place(x=600,y=70)
    Radiobutton(listar,text="TODO",variable=varOpcion,value=1).place(x=320,y=70)
    Radiobutton(listar,text="CONSOLA",variable=varOpcion,value=2).place(x=400,y=70)
    Radiobutton(listar,text="GENERO",variable=varOpcion,value=3).place(x=500,y=70)
    Button(text="MENU PRINCIPAL",justify="left",command=videojuegos_menu).place(x=340,y=550)

def listadoF():
    index = 0
    consola=""
    nombre=""
    genero=""
    imagen=""
    total_sistemas =[]
    
    #miro que opciones estan escogidas y las assigno a variables
    opcion = varOpcion.get()
    entrada = varEntry.get()
    
    #creo la ventana y el witget texto dentro de la ventana de listar
    texto = Frame()
    texto.config(background="white")
    texto.place(x=100,y=160,width=600,height=350)
    texto_text = Text(texto)
    texto_text.pack()
    
    if opcion==1 and entrada=="":
        try:
            with open("datos.txt","r") as file:
                for f in file:
                    index=index+1
                    if index == 1:
                        posicion = f
                    if index == 2:
                        consola = f
                    if index == 3:
                        nombre = f
                    if index == 4:
                        genero = f
                    if index == 5:
                        imagen = f
                    if  index == 6:
                        index = 0
                        texto_text.insert("end",f"-----------------------------------------------------------------------\n")
                        texto_text.insert("end",f"INDICE: {posicion}\nCONSOLA: {consola}\nNOMBRE: {nombre}\nGENERO: {genero}\nIMAGEN: {imagen}\n")
                texto_text.insert("end",f"                            HE LLEGADO AL FINAL ")
                
        except:
                texto_text.insert("end",f"                            NO HAY DATOS ")
    
    # opcion de radiobutton es 2 que significa consola.creo una variable num ,para contar los datos grabados
    # capturo todos los sistemas que estan en el archivo datos
    
    if opcion==2:
        num = 0
        try:
            with open ("datos.txt","r") as file:
                for f in file:
                    num = num + 1
                    if num == 2:
                        try:
                            total_sistemas.index(f)
                        except:
                            total_sistemas.append(f)
                    if num == 6:
                        num = 0
        except:
            texto_text.insert("end",f"                            NO HAY DATOS ")
        
        #ahora miro sistema por sistema. si la entrada puesta en el entry coicide con t abro el archibo y cargo
        # cada valor en su variable 
        contador = 0
        try:
            for t in total_sistemas:
                if t == f"{entrada}\n":
                    with open("datos.txt","r") as file:
                        for f in file:
                            index=index+1
                            if index == 1:
                                posicion = f
                            if index == 2:
                                consola = f
                            if index == 3:
                                nombre = f
                            if index == 4:
                                genero = f
                            if index == 5:
                                imagen = f
                            if  index == 6:
                                index = 0

                                # muestro solo los datos que coiciden con la entrada
                                if consola == f"{entrada}\n":
                                    contador = contador +1
                                    texto_text.insert("end",f"-----------------------------------------------------------------------\n")
                                    texto_text.insert("end",f"INDICE: {posicion}\nCONSOLA: {consola}\nNOMBRE: {nombre}\nGENERO: {genero}\nIMAGEN: {imagen}\n")
                        
                    texto_text.insert("end",f"                            HE LLEGADO AL FINAL ")
                    texto_text.insert("end",f"\n             TIENES UN TOTAL DE {contador} JUEGO/S EN LA CONSOLA {entrada}.  ")
        except:
                texto_text.insert("end",f"                            NO HAY DATOS ")
    
    total_genero = []

    if opcion==3:
        num = 0
        try:
            with open ("datos.txt","r") as file:
                for f in file:
                    num = num + 1
                    if num == 4:
                        try:
                            total_genero.index(f)
                        except:
                            total_genero.append(f)
                    if num == 6:
                        num = 0
        except:
            texto_text.insert("end",f"                            NO HAY DATOS ")
        
        contador = 0
        try:
            for t in total_genero:
                if t == f"{entrada}\n":
                    with open("datos.txt","r") as file:
                        for f in file:
                            index=index+1
                            if index == 1:
                                posicion = f
                            if index == 2:
                                consola = f
                            if index == 3:
                                nombre = f
                            if index == 4:
                                genero = f
                            if index == 5:
                                imagen = f
                            if  index == 6:
                                index = 0
                                # muestro solo los datos que coiciden con la entrada
                                if genero == f"{entrada}\n":
                                    contador = contador + 1
                                    texto_text.insert("end",f"-----------------------------------------------------------------------\n")
                                    texto_text.insert("end",f"INDICE: {posicion}\nCONSOLA: {consola}\nNOMBRE: {nombre}\nGENERO: {genero}\nIMAGEN: {imagen}\n")
                        
                    texto_text.insert("end",f"                            HE LLEGADO AL FINAL ")
                    texto_text.insert("end",f"\n                TIENES UN TOTAL DE {contador} JUEGO/S DE {entrada}.  ")
        except:
                texto_text.insert("end",f"                            NO HAY DATOS ")

#----------------------------------------------------------------------------------------------------------
#codigo borrar juegos

def borrar_juegos():
    borrar = Frame()
    borrar.config(background="black",width=800,height=600)
    borrar.place(x=0,y=0)  
    
    global indice_borrar,consola_borrar,nombre_borrar

    indice_borrar = StringVar()
    consola_borrar = StringVar()
    nombre_borrar = StringVar()
    
    Button(text="MENU PRINCIPAL",justify="left",command=videojuegos_menu).place(x=340,y=550)
    Label(borrar,bg="black",fg="white",text="BORRAR JUEGO ",font=("Arial","20")).place(x=300,y=40)
    Label(borrar,bg="black",fg="white",text="DIME EL INDICE: ",font=("Arial","12")).place(x=100,y=130)
    Label(borrar,bg="black",fg="white",text="CONSOLA ",font=("Arial","12")).place(x=100,y=160)
    Label(borrar,bg="black",fg="white",text="NOMBRE ",font=("Arial","12")).place(x=450,y=160)
    Entry(borrar,textvariable=indice_borrar).place(x=230,y=130)
    Entry(borrar,textvariable=consola_borrar).place(x=230,y=160)
    Entry(borrar,textvariable=nombre_borrar).place(x=550,y=160)
    Button(text=" BUSCAR ",justify="left",command=borrar_buscar).place(x=370,y=200)

def borrar_buscar():
    index = 0
    indice = indice_borrar.get()
    Button(bg="white",fg="black",text="NO ENCUENTRO EL INDICE",justify="left").place(x=331,y=300)
    try:
        with open("datos.txt","r") as file:
            for f in file:
                index=index+1
                if index == 1:
                    posicion = f
                if index == 2:
                    consola = f
                if index == 3:
                    nombre = f
                if  index == 6:
                    index = 0
                    if posicion == f"{indice}\n":
                        consola_borrar.set(consola)
                        nombre_borrar.set(nombre)
                        Button(fg="red",text=" ¡¡ BORRAR ESTOS DATOS !! ",justify="left",command=borrar_def).place(x=330,y=300)
    except:
        pass  

def borrar_def():
    index = 0
    indice = indice_borrar.get()
    try:
        with open ("datos.txt","r") as file_uno:
            with open ("datos.tmp","w") as file_dos:
                for f_uno in file_uno:
                    index = index + 1
                    if index == 1:
                        posicion = f_uno
                    if index == 2:
                        consola = f_uno
                    if index == 3:
                        nombre = f_uno
                    if index == 4:
                        genero = f_uno
                    if index == 5:
                        imagen = f_uno
                    if index == 6:
                        sinopsis = f_uno
                        index = 0
                        if posicion != f"{indice}\n":
                            file_dos.write(posicion)
                            file_dos.write(consola)
                            file_dos.write(nombre)
                            file_dos.write(genero)
                            file_dos.write(imagen)
                            file_dos.write(sinopsis)
        index = 0
        with open ("datos.tmp","r") as file_uno:
            with open ("datos.txt","w") as file_dos:
                for f_uno in file_uno:
                    index = index + 1
                    if index == 1:
                        posicion = f_uno
                    if index == 2:
                        consola = f_uno
                    if index == 3:
                        nombre = f_uno
                    if index == 4:
                        genero = f_uno
                    if index == 5:
                        imagen = f_uno
                    if index == 6:
                        sinopsis = f_uno
                        index = 0
                        file_dos.write(posicion)
                        file_dos.write(consola)
                        file_dos.write(nombre)
                        file_dos.write(genero)
                        file_dos.write(imagen)
                        file_dos.write(sinopsis)
    except:
        pass
    
    indice_borrar.set("")
    nombre_borrar.set("")
    consola_borrar.set("")

#----------------------------------------------------------------------------------------------------------
#codigo mostrar juegos y caratulas

def j_c():
    ventana = Frame()
    ventana.config(background="black",width=800,height=600)
    ventana.place(x=0,y=0)  
    
    #variables de de entrada de texto las hago globales para compartirlas con otras funciones
    #global consola_jc,nombre_jc,genero_jc,imagen_jc
    #global texto_text
    global consola_jc,nombre_jc,genero_jc
    global texto_jc
    
    consola_jc = StringVar()
    nombre_jc = StringVar()
    genero_jc = StringVar()

    #creo el menu para ventana juegos. para insertar el juego escrito en los entris hay que pulsar grabar   
    Button(ventana,text="MENU PRINCIPAL",justify="left",command=videojuegos_menu).place(x=340,y=550)
    Label(ventana,bg="black",fg="white",text=" JUEGO Y CARATULAS ",font=("Arial","20")).place(x=240,y=20)
    Label(ventana,bg="black",fg="white",text="CONSOLA VIDEO JUEGOS",font=("Arial","12")).place(x=40,y=70)
    Label(ventana,bg="black",fg="white",text="JUEGO",font=("Arial","12")).place(x=40,y=100)
    Label(ventana,bg="black",fg="white",text="GENERO",font=("Arial","12")).place(x=40,y=130)
    Label(ventana,bg="black",fg="white",text="IMAGEN",font=("Arial","12")).place(x=510,y=160)
    Label(ventana,bg="black",fg="white",text="SINOPSIS",font=("Arial","12")).place(x=40,y=160)
    Entry(ventana,textvariable=consola_jc).place(x=260,y=70)
    Entry(ventana,textvariable=nombre_jc).place(x=260,y=100)
    Entry(ventana,textvariable=genero_jc).place(x=260,y=130)
    Button(ventana,text="MOSTRAR TODOS >",justify="left",command=j_cMostrartodos).place(x=570,y=80)
    Button(ventana,text="BUSCAR JUEGO",justify="left",command=bj_jc).place(x=585,y=110)
    
    #creo la ventana de sinopsis dentro menu de juego y caratulas 
    texto = Frame()
    texto.config(background="white")
    texto.place(x=40,y=190,width=450,height=350)
    #creo el whitget texto dentro de la la ventana texto
    texto_jc = Text(texto)
    texto_jc.pack()
    #cargo la imagen dentro de una variable y creo la ventana de la caratula con esa variable
    imagen = Image.open("biblioteca.jpg")
    imagenR = imagen.resize((250,345))
    imagenTk = ImageTk.PhotoImage(imagenR)
    pantalla = Label(ventana,image=imagenTk)
    pantalla.image = imagenTk
    pantalla.place(x=500,y=190)
    #declaro el achivo abierto como comun para poder utilizarlos en otra funcion
    global file
    try:
        file = open ("datos.txt","r")
    except:
        pass

def j_cMostrartodos():
    try:
        #leo cada liniea del archivo y la guardo en cada variable . son 6 datos guardados por cada juego
        nume=file.readline()
        consola=file.readline()
        nombre=file.readline()
        genero=file.readline()
        imagen=file.readline()
        sinopsis=file.readline()
        #muestro por pantalla cada dato guardado dentro de sus veriables        
        consola_jc.set(consola)
        nombre_jc.set(nombre)
        genero_jc.set(genero)
        texto_jc.delete("1.0","end")
        texto_jc.insert("1.0",sinopsis)
        #creo la ventena que va a contener la caatula del juego y leo la imagen
        vent = Frame()
        vent.config(background="white",width=250,height=350)
        vent.place(x=500,y=190)
        try:
            print (imagen)
            with open(imagen[:len(imagen)-1],"r") as datos_imag:
                pass
            im = Image.open(imagen[:len(imagen)-1])
        except:
            im = Image.open("biblioteca.jpg")

        imR = im.resize((250,350))
        imTk = ImageTk.PhotoImage(imR)
        pan = Label(vent,image=imTk)
        pan.image = imTk
        pan.place(x=0,y=0) 

        #cuando da un error de lectura devido al final del archibo cierro el archibo
        
        if nume == "":
            print (nume)
            file.close()
    except:
        pass

def bj_jc():
    index = 0
    nombre = nombre_jc.get()
    try:   
        with open ("datos.txt","r") as file:
            for f in file:
                index = index + 1
                if index == 2 :
                    consola_f = f 
                if index == 3:
                    nombre_f = f
                if index == 4:
                    genero_f = f
                if index == 5:
                    imagen_f = f
                if index == 6:
                    index = 0
                    sinopsis_f = f
                    if nombre_f == f"{nombre}\n":
                        consola_jc.set(consola_f)
                        nombre_jc.set(nombre_f)
                        genero_jc.set(genero_f)
                        texto_jc.delete("1.0","end")
                        texto_jc.insert("1.0",sinopsis_f)
                        vent = Frame()
                        vent.config(background="white",width=250,height=350)
                        vent.place(x=500,y=190)
                        try:
                            im = Image.open(imagen_f[:len(imagen_f)-1])
                            imR = im.resize((250,350))
                            imTk = ImageTk.PhotoImage(imR)
                            pan = Label(vent,image=imTk)
                            pan.image = imTk
                            pan.place(x=0,y=0) 
                        except:
                            pass
    except:
        pass

#----------------------------------------------------------------------------------------------------------
#codigo juego al hazar

def j_h():
    index = 0
    ventana = Frame()
    ventana.config(background="black",width=800,height=600)
    ventana.place(x=0,y=0)  
    
    consola_jh = StringVar()
    nombre_jh = StringVar()
    genero_jh = StringVar()

    #creo el menu para ventana juegos. para insertar el juego escrito en los entris hay que pulsar grabar   
    Button(ventana,text="MENU PRINCIPAL",justify="left",command=videojuegos_menu).place(x=340,y=550)
    Label(ventana,bg="black",fg="white",text=" JUEGO Y CARATULAS ",font=("Arial","20")).place(x=240,y=20)
    Label(ventana,bg="black",fg="white",text="CONSOLA VIDEO JUEGOS",font=("Arial","12")).place(x=40,y=70)
    Label(ventana,bg="black",fg="white",text="JUEGO",font=("Arial","12")).place(x=40,y=100)
    Label(ventana,bg="black",fg="white",text="GENERO",font=("Arial","12")).place(x=40,y=130)
    Label(ventana,bg="black",fg="white",text="IMAGEN",font=("Arial","12")).place(x=510,y=160)
    Label(ventana,bg="black",fg="white",text="SINOPSIS",font=("Arial","12")).place(x=40,y=160)
    Entry(ventana,textvariable=consola_jh).place(x=260,y=70)
    Entry(ventana,textvariable=nombre_jh).place(x=260,y=100)
    Entry(ventana,textvariable=genero_jh).place(x=260,y=130)
    
    
    #creo la ventana de sinopsis dentro menu de juego y caratulas 
    texto = Frame()
    texto.config(background="white")
    texto.place(x=40,y=190,width=450,height=350)
    #creo el whitget texto dentro de la la ventana texto
    texto_jh = Text(texto)
    texto_jh.pack()
    #miro los dato que hay en el archibo y lo divido entre seis. lo que me da los juegos que hay
    try:
        with open ("datos.txt","r") as file:
            for f in file :
                index = index + 1 
            num =  index / 6
        
        #calculo un numero a azar en los juegos que hay , le sumo uno para calcular todos
        hazar = random.randint(1,int(num))

        index = 0
        datos = 0
        with open ("datos.txt","r") as file:
            for f in file :
                index = index + 1 
                if index == 1:
                    #en el primer dato del juego sumo uno a datos
                    datos = datos + 1
                if index == 2:
                    consola = f
                if index == 3:
                    nombre = f
                if index == 4:
                    genero = f
                if index == 5:
                    im = f
                if index == 6:
                    sinopsis = f
                    index = 0
                    #miro al final de cada juego si coiciden hazar y el juego para mostralo
                    if hazar == datos: 
                        consola_jh.set(consola)
                        nombre_jh.set(nombre)
                        genero_jh.set(genero)
                        
                        #cargo la imagen dentro de una variable y creo la ventana de la caratula con esa variable
                        imagen = Image.open(im[:len(im)-1])
                        imagenR = imagen.resize((250,345))
                        imagenTk = ImageTk.PhotoImage(imagenR)
                        pantalla = Label(ventana,image=imagenTk)
                        pantalla.image = imagenTk
                        pantalla.place(x=500,y=190)
                        #inserto la sinopsis de juego en el texto
                        texto_jh.insert("1.0",sinopsis)
    except:
        pass

#----------------------------------------------------------------------------------------------------------
#codigo salir

def salir_juegos():
    try:
        file.close()
    except:
        pass
    raiz.quit()

#inicio el programa llamando a la funcion videojuegos_menu
videojuegos_menu()

raiz.mainloop()
