#import os
from random import randint
import time
from tkinter import *


# Alea ne sert à rien pour info :)

def alea():
    balle=int(input("Insère ton numéro de 1 à 6:"))
    if randint(1,1)==balle:
        print("Tu est foutu :()")
        time.sleep(2)
        print("ARRET SYSTEM!!!!")
        #os.system("shutdown 0")
    else:
        print("Ta eu de la chance")
        

# ⚠️ Version INOFENSIVE ⚠️ #


### ------------- Fenetre Tkinter --------------###

def pageprincipale():
    global ws

    ws = Tk()
    ws.title("TrucaV3")
    #ws.iconbitmap("Trucalogo.ico")
    ws.geometry("300x300")
    ws.minsize(400,300)
    ws.config(background='#19f07e')


    frame1 = Frame(ws, bg="#19f07e", padx=10)

    label = Label(ws, text="Bonjour, à quel jeu souhaitez vous jouer?", bg="#19f07e",fg='black', font=("Courrier", 12))
    label.pack()

    boutonfermer = Button(frame1, text="Fermer", bg='red' ,command=ws.quit)
    boutonfermer.pack(pady=10)
    boutonretour = Button(frame1, text="Retour", bg='blue', command=fonctionquit)
    boutonretour.pack()


    Bouton1 = Button(frame1, text="Roullete Russe:", bg="#2eebf1", command=pagerr)
    Bouton1.pack(pady=20, side=LEFT)

    Bouton2 = Button(frame1, text="Pendu:", bg="#2eebf1")
    Bouton2.pack(pady=20, padx=8, side=LEFT)

    Bouton3 = Button(frame1, text="Pierre, Feuille, Ciseaux:", bg="#2eebf1")
    Bouton3.pack(pady=20, side=LEFT)

    Bouton4 = Button(frame1, text="Demineur:", bg="#2eebf1", command=demineurjeu)
    Bouton4.pack(pady=20, padx=8, side=LEFT)

    frame1.pack()


    ws.mainloop()
        
        
def pagerr():
    global ws, framerr, number_entrybrut, res

    framerr = Frame(ws, bg="#19f07e")

    label = Label(framerr, text="Choisi un nombre de 1 à 6:")
    label.pack()

    number_entrybrut = Entry(framerr)
    number_entrybrut.pack()

    Boutonrr = Button(framerr, text="Valider ce chiffre", command=validationpagerr)
    Boutonrr.pack()

    framerr.pack()



    
def validationpagerr():
    global number_entrybrut
    a = number_entrybrut.get()
    print(type(a))
    print(a)
    b= randint(1,6)
    a = int(a)
    if a == b:
        print("Vous êtes foutu!")
    else:
        print("Vous avez de la chance")
        return


def getEntry():
    global number_entrybrut, res
    res = number_entrybrut.get()


    
    
def fonctionquit():
    global ws
    ws.destroy()
    return pageprincipale()
        
        
        
        
        

        







#-------------------- Demineur Nyle --------------#

gameOver = False
score = 0
carrésAVérifier = 0

def demineurjeu():
    global ws, gameOver, score, carrésAVérifier



    def jouer_démineur():
        global fenêtre
        créer_terrainMiné(terrainMiné)
        fenêtre = Tk()
        configuration_fenêtre(fenêtre)
        fenêtre.mainloop()
        
    terrainMiné = []

    def créer_terrainMiné(terrainMiné):
        global carrésAVérifier
        for rangée in range(0,10):
            listeRangée = []
            for colonne in range(0,10):
                if randint(1,100) < 20:
                    listeRangée.append(1)
                else:
                    listeRangée.append(0)
                    carrésAVérifier = carrésAVérifier + 1
            terrainMiné.append(listeRangée)
        #printTerrain(terrainMiné)
        
    def printTerrain(terrainMiné):
        for listeRangée in terrainMiné:
            print(listeRangée)
            
    def configuration_fenêtre(fenêtre):
        for numéroRangée, listeRangée in enumerate(terrainMiné):
            for numéroColonne, entréeColonne in enumerate(listeRangée):
                if randint(1,100) < 25:
                    carré = Label(fenêtre, text = "    ", bg = "darkgreen")
                elif randint(1,100) < 75:
                    carré = Label(fenêtre, text = "    ", bg = "seagreen")
                else:
                    carré = Label(fenêtre, text = "    ", bg = "green")
                carré.grid(row = numéroRangée, column = numéroColonne)
                carré.bind("<Button-1>", quand_cliqué)
    def quand_cliqué(event):
        global score
        global gameOver
        global carrésAVérifier
        global fenêtre

        carré = event.widget
        rangée = int(carré.grid_info()["row"])
        colonne = int(carré.grid_info()["column"])
        texteActuel = carré.cget("text")
        if gameOver == False:
            if terrainMiné[rangée][colonne] == 1:
                gameOver = True
                carré.config(bg = "red")
                print("GAME OVER ! Tu as touché une bombe !")
                print("Ton score :", score)
                print("Maintenant c est ciao ")
                time.sleep(1)
                fenêtre.destroy()
                resetdemineur()
                return pageprincipale()
                #-------------------os.system("shutdown 0")
            elif texteActuel == "    ":
                carré.config(bg = "brown")
                totalBombes = 0

                if rangée < 9:
                    if terrainMiné[rangée+1][colonne] == 1:
                        totalBombes = totalBombes + 1

                if rangée > 0:
                    if terrainMiné[rangée-1][colonne] == 1:
                        totalBombes = totalBombes + 1

                if colonne > 0:
                    if terrainMiné[rangée][colonne-1] == 1:
                        totalBombes = totalBombes + 1

                if colonne < 9:
                    if terrainMiné[rangée][colonne+1] == 1:
                        totalBombes = totalBombes + 1

                if rangée > 0 and colonne > 0:
                    if terrainMiné[rangée-1][colonne-1] == 1:
                        totalBombes = totalBombes + 1

                if rangée < 9 and colonne > 0:
                    if terrainMiné[rangée+1][colonne-1] == 1:
                        totalBombes = totalBombes + 1

                if rangée > 0 and colonne < 9:
                    if terrainMiné[rangée-1][colonne+1] == 1:
                        totalBombes = totalBombes + 1

                if rangée < 9 and colonne < 9:
                    if terrainMiné[rangée+1][colonne+1] == 1:
                        totalBombes = totalBombes + 1

                carré.config(text = " " + str(totalBombes) + " ")

                carrésAVérifier = carrésAVérifier - 1

                score = score + 1

                if carrésAVérifier == 0:
                    gameOver = True
                    print("Bravo, tu as trouvé tous les carrés non minés.Tu ne seras pas éliminée")
                    print("Ton score :", score)
                    time.sleep(5)
                    fenêtre.destroy()
                    resetdemineur()
                    return pageprincipale()
    ws.destroy()
    jouer_démineur()

        
def resetdemineur():
    global score, gameOver, carrésAVérifier

    gameOver = False
    score = 0
    carrésAVérifier = 0
            




pageprincipale()



# Version réaliser par Baptiste et Nyle #