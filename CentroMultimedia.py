#CentroMultimedia.py
#Autor: Jonathan Jhosua López Casttillón
#Proyecto Final Centro Multimedia
#Licencia: MIT



#------Librerías a utilizar
from tkinter import * #Para interfáz gráfica
from tkinter import filedialog #Lectura de archivos
import webbrowser #Abrir enlaces de internet
import vlc #Reproductor de medios
import os #Funcionalidades del S.O.
import pygame #Reproducción de audios
from tkVideoPlayer import TkinterVideo #Opcional a utilizar para medios de vídeo


raiz=Tk() #Creamos el widget principal


#--------Configuraciones del widget principal
raiz.call('wm', 'iconphoto', raiz._w, PhotoImage(file='apple.png'))
raiz.title("Centro Multimedia")
raiz.config(bg="blue2") #fondo de la ventana
raiz.config(bd="35")#el grosor de borde
raiz.config(relief="sunken")#para los bordes
raiz.attributes('-fullscreen',True)#pantalla completa

#------Función par abrir enlaces--------
def AbrirPagina(url):
    webbrowser.open(url)


#---------Widget Secundario
miFrame=Frame(raiz)
miFrame.pack()
miFrame.config(bg="blue2")



operacion=0
VentanaElegida=StringVar()

#-------Funciones de la librería pygame---------
pygame.init()
pygame.mixer.init()

#----------------Abrir ventana de usb-----------
#-------Función para lectura de música en usb----------

def abreFicheroMusica():
	ficheroMusica=filedialog.asksaveasfilename(title="Seleccionar Música", initialdir="/media/pi/JOHN/Música", filetypes=(("Todo","*.*"),("mp3", "*.mp3"),
		("wav","*.wav")))
	print(ficheroMusica)
	pygame.mixer.music.load(str(ficheroMusica))# Carga el archivo de audio
	pygame.mixer.music.play()# Se reproduce el archivo cargado

#-------Función para lectura de fotos en usb----------
def abreFicheroFotos():
	ficheroFotos=filedialog.asksaveasfilename(title="Seleccionar Foto", initialdir="/media/pi/JOHN/Fotos", filetypes=(("PNG","*.png"),("Todo","*.*")))
	print(ficheroFotos)
	global media
	media=vlc.MediaPlayer(str(ficheroFotos))
	media.play()

#-------Función para lectura de Vídeos en usb----------
def abreFicheroVideo():
	ficheroVideos=filedialog.asksaveasfilename(title="Seleccionar Vídeo", initialdir="/media/pi/JOHN/Vídeo", filetypes=(("MP4","*.mp4"),("Todo","*.*")))
	print(ficheroVideos)
	global vid
	vid=vlc.MediaPlayer(str(ficheroVideos))
	vid.play()

#--------Función para el botón de pausar y reanudar música--------
def pausarmusica(opcion1):
	if opcion1==1:
		pygame.mixer.music.pause()
	else:
		pygame.mixer.music.unpause()

#--------Función para el botón de pausar y reanudar vídeo--------
def pausarvideo(opcion2):
	global vid
	if opcion2==1:
		vid.stop()
	else:
		vid.play()

#--------Función para el botón de minimizar y maximizar imagen--------
def cerrarimagen(opcion3):
	global media
	if opcion3==1:
		media.stop()
	else:
		media.play()



#----------Título de la ventana-----------
tituloLabel=Label(miFrame, text="Servicios Disponibles")
tituloLabel.grid(row=0,column=1, padx=10, pady=10, columnspan="5")
tituloLabel.config(bg="black", fg="red", justify="center", font="Times 40 italic")

#---------Indicador de servicios de vídeo online---------
imgVideo=PhotoImage(file="logovideo.png")#Se define la variable para guardar una imagen
VídeoLabel=Label(miFrame, image=imgVideo)#Se agrega la imagen de la línea anterior al anuncio del servicio
VídeoLabel.grid(row=1,column=1,sticky="e", padx=10, pady=10)#Se especifica la posición
VídeoLabel.config(bg="black")#Se define el color del fondo
#La lógica de las líneas anteriores se replica en los siguientes servicios

#---------Indicador de servicios de música online---------
imgMusica=PhotoImage(file="logomusica.png")
MúsicaLabel=Label(miFrame, image=imgMusica)
MúsicaLabel.grid(row=1,column=2,sticky="e", padx=10, pady=10)
MúsicaLabel.config(bg="black")

#---------Indicador de servicios de medio externo---------
imgUsb=PhotoImage(file="logousb.png")
ExternoLabel=Label(miFrame, image=imgUsb)
ExternoLabel.grid(row=1,column=3,sticky="e", padx=10, pady=10)
ExternoLabel.config(bg="black")

#---------Indicador de servicio de internet---------
imgInternet=PhotoImage(file="logointernet.png")
InternetLabel=Label(miFrame, image=imgInternet)
InternetLabel.grid(row=1,column=4,sticky="e", padx=10, pady=10)
InternetLabel.config(bg="black")


#------------Botón de Netflix----------------
imgNetflix=PhotoImage(file="logonetflix.png")#Se define la variable para guardar una imagen
botonNetflix=Button(miFrame, image=imgNetflix, command=lambda: AbrirPagina('https://www.netflix.com/mx-en/login'))#Se crea el botón, se le asigna la imagen de la línea anterior y se le agrega acción
botonNetflix.grid(row=2, column=1)#Se define posición del botón
botonNetflix.config(cursor="hand2",bg="black")#Configuración de fondo y señalamiento
#Se repite la lógica anterior para los demás botones

#------------Botón de HBO----------------
imgHBO=PhotoImage(file="logohbo.png")
botonHBO=Button(miFrame, text="HBO", image=imgHBO, command=lambda: AbrirPagina('https://www.hbolatam.com/us/account/login'))
botonHBO.grid(row=3, column=1)
botonHBO.config(cursor="hand2",bg="black")

#------------Botón de Blim----------------
imgBlim=PhotoImage(file="logoblim.png")
botonBlim=Button(miFrame, text="Blim", image=imgBlim, command=lambda: AbrirPagina('https://www.blim.com/cuenta/ingresar'))
botonBlim.grid(row=4, column=1)
botonBlim.config(cursor="hand2",bg="black")

#------------Música en línea----------------
#------------Botón de Spotify----------------
imgSpotify=PhotoImage(file="logospotify.png")
botonSpotify=Button(miFrame, image=imgSpotify, command=lambda: AbrirPagina('https://open.spotify.com'))
botonSpotify.grid(row=2, column=2)
botonSpotify.config(cursor="hand2",bg="black")

#------------Botón de Deezer----------------
imgDeezer=PhotoImage(file="logodeezer.png")
botonDeezer=Button(miFrame, image=imgDeezer, command=lambda: AbrirPagina('https://www.deezer.com/mx/'))
botonDeezer.grid(row=3, column=2)
botonDeezer.config(cursor="hand2",bg="black")

#------------Botón de YoutubeMusic----------------
imgYTM=PhotoImage(file="logoytmusic.png")
botonYTM=Button(miFrame, image=imgYTM, command=lambda: AbrirPagina('https://music.youtube.com'))
botonYTM.grid(row=4, column=2)
botonYTM.config(cursor="hand2",bg="black")

#------------Externo----------------
#------------Botón de Fotos USB----------------
imgFotosUSB=PhotoImage(file="logofotos.png")
botonFotosUSB=Button(miFrame, image=imgFotosUSB,command=abreFicheroFotos)
botonFotosUSB.grid(row=2, column=3)
botonFotosUSB.config(cursor="hand2",bg="black")

#------------Botón de Imágenes USB----------------
imgMusicaUSB=PhotoImage(file="logomusicausb.png")
botonMusicaUSB=Button(miFrame, image=imgMusicaUSB,command=abreFicheroMusica)
botonMusicaUSB.grid(row=3, column=3)
botonMusicaUSB.config(cursor="hand2",bg="black")

#------------Botón de Vídeos USB----------------
imgVideosUSB=PhotoImage(file="logovideousb.png")
botonVideosUSB=Button(miFrame, image=imgVideosUSB, command=abreFicheroVideo)
botonVideosUSB.grid(row=4, column=3)
botonVideosUSB.config(cursor="hand2",bg="black")

#----------------Asistente Internet-----------------
#------------Botón de Navegador Internet----------------
imgChrome=PhotoImage(file="logochrome.png")
botonInternet=Button(miFrame, image=imgChrome, command=lambda: AbrirPagina('https://google.com'))
botonInternet.grid(row=2, column=4)
botonInternet.config(cursor="hand2",bg="black")


#----------Botones para pausar medios externos---------------
botondetenermusica=Button(miFrame, text="Música ▌▐", command=lambda:pausarmusica(1))#Se configura lo que aparecerá en el botón y su acción
botondetenermusica.grid(row=3, column=4)#Se posiciona el botón
botondetenermusica.config(cursor="hand2", bg="black", fg="#03f943")#Configuraciones del fondo, color de letra y el cómo se señala
#Se repite la misma lógica de líneas anteriores en los demás botones

botonreanudarmusica=Button(miFrame, text="Música >", command=lambda:pausarmusica(0))
botonreanudarmusica.grid(row=4, column=4)
botonreanudarmusica.config(cursor="hand2", bg="black", fg="#03f943")

botondetenervideo=Button(miFrame, text="Vídeo ▌▐", command=lambda:pausarvideo(1) )
botondetenervideo.grid(row=1, column=5)
botondetenervideo.config(cursor="hand2", bg="black", fg="#03f943")

botonreanudarvideo=Button(miFrame, text="Vídeo >", command=lambda:pausarvideo(0))
botonreanudarvideo.grid(row=2, column=5)
botonreanudarvideo.config(cursor="hand2", bg="black", fg="#03f943")

botoncerrarimagen=Button(miFrame, text="Imagen ↓", command=lambda:cerrarimagen(1) )
botoncerrarimagen.grid(row=3, column=5)
botoncerrarimagen.config(cursor="hand2", bg="black", fg="#03f943")

botonreanudarimagen=Button(miFrame, text="Imagen ↑", command=lambda:cerrarimagen(0))
botonreanudarimagen.grid(row=4, column=5)
botonreanudarimagen.config(cursor="hand2", bg="black", fg="#03f943")


raiz.mainloop()#Mantiene el programa o interfáz siempre abierta