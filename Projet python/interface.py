# -*- coding: utf-8 -*-
"""
Created on Tue Jan 10 23:16:19 2023

@author: HP
"""

import tkinter
from tkinter import *
from tkinter.ttk import *
from PIL import ImageTk, Image

fenetre =Tk()
    # Ajout de widgets à la fenêtre
label = Label(fenetre, text="Tapez un mot clé")
label.config(font=('Arial', 20))#Le font et la taille du titre
label.pack()


    
    #b= Button(fenetre,text="Rechercher",command="",bg='yellow')
    #b.pack()
    
    # Créer un objet photoimage pour utiliser l'image
#photo =Image.open("mot-clé.png")
#test = ImageTk.PhotoImage(photo)
    
#panel = tkinter.Label(fenetre, image = photo)
#panel.pack(side = "bottom", fill = "both", expand = "yes")
    
    
fenetre.mainloop()
mainloop()
