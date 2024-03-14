import os
from random import randint
import time
from tkinter import *

# ----------------
# pour éteindre un ordinateur sous linux:
#       os.system("shutdown 0")

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
        

# ⚠️ Version INOFENSIVE POUR LE MOMENT⚠️ #

# Variables:
pagerrnumber = 0

### ------------- Fenetre Tkinter --------------###

def pageprincipale():
    global ws, frame1

    ws = Tk()
    ws.title("TrucaV3")
    #ws.iconbitmap("Trucalogo.ico")
    ws.geometry("550x300")
    ws.minsize(400,300)
    ws.config(background='#19f07e')


    frame1 = Frame(ws, bg="#19f07e", padx=10)

    label = Label(ws, text="Bonjour, à quel jeu souhaitez vous jouer?", bg="#19f07e",fg='black', font=("Courrier", 12))
    label.pack()

    boutonfermer = Button(frame1, text="Fermer", bg='red' ,command=ws.destroy)
    boutonfermer.pack(pady=10)
    boutonretour = Button(frame1, text="Retour", bg='blue', command=fonctionquit)
    boutonretour.pack()

#------------- Boutons jeux:

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




def getEntry():
    global number_entrybrut, res
    res = number_entrybrut.get()


    
    
def fonctionquit():
    global ws, pagerrnumber
    ws.destroy()
    pagerrnumber -= 1
    return pageprincipale()
        
        



#------------- Roulette Russe ----------------------


def pagerr():
    global ws, framerr, number_entrybrut, res, pagerrnumber

    pagerrnumber += 1

    if pagerrnumber > 1:
        framerr.destroy()
        pagerrnumber -= 2
        return pagerr()


    framerr = Frame(ws, bg="#19f07e")

    label = Label(framerr, text="Choisi un nombre de 1 à 6:")
    label.pack()

    number_entrybrut = Entry(framerr)
    number_entrybrut.pack()

    Boutonrr = Button(framerr, text="Valider ce chiffre", command=validationpagerr)
    Boutonrr.pack()


    framerr.pack()


    
def validationpagerr():
    global number_entrybrut, framerr, Textefinpagerr
    a = number_entrybrut.get()
    b= randint(1,6)
    a = int(a)
    if a == b:
        print("Vous êtes foutu!")
        Perdupagerr()
    else:
        print("Vous avez de la chance")
        Gagnerpagerr()

def Perdupagerr():
    Textefinpagerr = Label(framerr, text="Perdu", background='red')
    Textefinpagerr.pack()
    Textefinpagerr.after(1200, Textefinpagerr.destroy)
    time.sleep(1)
    os.system("shutdown 0")

def Gagnerpagerr():
    Textefinpagerr = Label(framerr, text="Gagner", background='#18f11e')
    Textefinpagerr.pack()
    Textefinpagerr.after(1200, Textefinpagerr.destroy)
    time.sleep(1)
    os.system("shutdown 0")



# ----------------------------------------------------------------
    
        



        
        
        
        

        







#-------------------- Demineur --------------#

gameOver = False
score = 0
carrésAVérifier = 0

def demineurjeu():
    global ws, gameOver, score, carrésAVérifier, pagerrnumber

    pagerrnumber -= 1

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
                # fin du demineur (perdu)
                findemineur()
                return pageprincipale()
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
                    # fin du démineur (gagner)
                    findemineur()
                    return pageprincipale()
    ws.destroy()
    jouer_démineur()

        
def resetdemineur():
    global score, gameOver, carrésAVérifier

    gameOver = False
    score = 0
    carrésAVérifier = 0

def findemineur():
    global fenêtre, gameOver

    fenêtre.destroy()

    enddemineurws = Tk()
    enddemineurws.title("Résultat Demineur:")
    enddemineurws.geometry("300x300")
    enddemineurws.minsize(300,300)

    if gameOver == False:
        enddemineurws.config(background='green')
        text11 = Label(enddemineurws, text="Bravo, tu as trouvé tous les carrés non minés!")
        text11.pack()
        text12 = Label(enddemineurws, text="Tu ne seras pas éliminée :)")
        text12.pack()
        text13 = Label(enddemineurws, text="Ton score: "+str(score))
        text13.pack()

    elif gameOver == True:
        enddemineurws.config(background='red')
        text21 = Label(enddemineurws, text="GAME OVER ! Tu as touché une bombe !")
        text21.pack()
        text22 = Label(enddemineurws, text="Ton score: "+str(score))
        text22.pack()
        text23 = Label(enddemineurws, text="maintenant c'est ciao")
        text23.pack()
        time.sleep(1)
        os.system("shutdown 0")
    
    enddemineurws.after(10500, enddemineurws.destroy)
    enddemineurws.mainloop()
    resetdemineur()
    

#------------------------------------------------------------------------------------------------
            




pageprincipale()



# Version réaliser par Baptiste et Nyle #