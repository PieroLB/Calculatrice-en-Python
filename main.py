###########################IMPORTATION DES BIBLIOTHEQUES############################

from tkinter import *
import tkinter.font as font
from math import sqrt
from fractions import Fraction
 


###########################CARACTERISTIQUES DE LA FENETRE###########################

window = Tk()               #Créér de la fenetre d'application
window.title("Calculatrice")   #Déterminer le titre de la fenetre d'application
window.geometry("240x220")   #Déterminer la taille de la fenetre d'application
 



######################################FONCTIONS######################################


parenth = False   #Déterminer les parentheses comme fermé
 
calcul_avt = str()    #Déterminer le type de la variable calcul_avt comme un string
result_avt = str()    #Déterminer le type de la variable result_avt comme un string
 
fract_active = False  #Déterminer la fraction comme désactivée

def ajoute(txt):     #Début de la fonction 'ajoute()' avec l'argument 'txt'
  global parenth     #Récupèrer la variable 'parenth' situé en dehors de la mémoire de la fonction
  if txt == "sqrt(":    #si l'argument 'txt' est égale à 'sqrt()'
      entr.insert(END, txt) #Insérer la valeur contenu dans l'argument'txt', à la fin de la valeur contenu dans le Entry 'entr'
      parenth = True  #Déterminer les parentheses comme ouvertes
  elif txt == "()":  #Sinon si l'argument 'txt' est égale à '()'
    if parenth == True:  #si la valeur de la variable 'parenth' est égale à True, c'est-a-dire si les parentheses sont ouvertes
      entr.insert(END, ")") #Insérer la valeur ')', à la fin de la valeur contenu dans le Entry 'entr'
      parenth = False  #Déterminer les parentheses comme fermées
    else:             #Sinon
      entr.insert(END, "(")  #Insérer la valeur '(', à la fin de la valeur contenu dans le Enrty 'entr'
      parenth = True    #Déterminer les parentheses comme ouvertes
  elif txt == "²":   #Sinon si l'argument 'txt' est égale à '²'
      entr.insert(END, "**")  #Insérer la valeur '**2', à la fin de la valeur contenu dans le Entry 'entr'
  else:     #Sinon
    entr.insert(END, txt)  #Insérer la valeur contenu dans l'argument'txt', à la fin de la valeur contenu dans le Enrty 'entr'
 
def supr_all():     #Début de la fonction 'supr_all()'
  entr.delete(0, END)  #Supprimer la valeur contenu dans le Entry 'entr' de la valeur 0 à la dernière valeur (='END')
 
def supr_entr():     #Début de la fonction 'supr_entr()'
  supr_all()    #Executer la fonction 'supr_all()'
  back['text'] = '' #Déterminer la valeur dans le Label 'back', correspodant à l'argument 'text', comme ''
  window.geometry("200x220")  ##Déterminer la taille de la fenetre d'application

def supr():   #Début de la fonction 'supr()'
  entr.delete(len(entr.get())-1)   #Supprimer la dernière valeur contenu dans le Entry 'entr'
 
def calcul():  #Début de la fonction 'calcul()'
  global result_avt   #Récupèrer la variable 'result_avt' situé en dehors de la mémoire de la fonction
  global calcul_avt   #Récupèrer la variable 'calcul_avt' situé en dehors de la mémoire de la fonction
  zero_apar = [False,0]   #Déterminer la liste 'zero_apar' comme égale à '[False,0]'
  racine_apar = [False,0]   #Déterminer la liste 'racine_apar' comme égale à '[False,0]'
  u = -1    #Déterminer la variable 'u' comme égale à -1
  for i in entr.get():   #boucle qui récupère chaque valeur contenue dans le ENTRY 'entr'
    u += 1   #AJouter 1 à la variable 'u'
    if i == "0":    #si la variable 'i' est égale à '0'
      zero_apar = [True, u]   #Déterminer la liste 'zero_apar' comme égale à '[True,u]'
    elif i == "s":  #sinon si la variable 'i' est égale à 's'
      racine_apar = [True, u]   #Déterminer la liste 'racine_apar' comme égale à '[True,u]'
    elif racine_apar[0] == True:  #sinon si la variable 'racine_apar' est égale à 'True'
      if i == ")":  #si la variable 'i' est égale à ')'
        racine_apar.append(u)  #AJouter à la liste racine_apar la valeur contenue dans la variable 'u'
    else:   #sinon
      continue  #continue d'analyser le contenu du ENTRY 'entr'
  if zero_apar[0] == True:  #Si le premier élément de la liste 'zero_apar' est égale à True, c'est-a-dire si il y a un 0 dans le calcul
    if entr.get()[zero_apar[1]-1] == "/":  #si la valeur juste avant le zero est une division
      back.config(text="ERREUR (division par 0)")  #Déterminer la valeur contenue dans l'argument 'text' contenue dans le Label 'back' comme égale à "ERREUR (division par 0)"
      entr.delete(0, END) #Supprimer la valeur, de 0 à la fin, contenue dans le Entry 'entr' 
    else:
      back.config(text=str(entr.get())+"="+str(eval(entr.get())))  #Déterminer la valeur contenue dans l'argument 'text' contenue dans le Label 'back' comme l'addition du contenu du Label 'entr', du string '=', et du calcul du contenu du Label 'entr'
      result_avt = str(eval(entr.get()))  #Déterminer la variable 'result_avt' comme égal au calcul du contenu du Label 'entr'
      calcul_avt = str(entr.get())  #Déterminer la variable 'calcul_avt' comme égal au contenu du Label 'entr'
      entr.delete(0, END)   #Supprimer la valeur, de 0 à la fin, contenue dans le Entry 'entr'
  elif racine_apar[0] == True:  #Si le premier élément de la liste 'racine_apar' est égale à True, c'est-a-dire si il y a un racine carrée dans le calcul
    if eval(str(entr.get()[racine_apar[1]+5:racine_apar[2]])) < 0:
      entr.delete(0,END)  #Supprimer la valeur, de 0 à la fin, contenue dans le Entry 'entr' 
      window.geometry("200x240")  #Déterminer la taille de la fenetre d'application
      back.config(text="ERREUR (racine carré \nd'un nombre négatif)") #Déterminer la valeur contenue dans l'argument 'text' contenue dans le Label 'back' comme égale à "ERREUR (racine carré \nd'un nombre négatif)"
    else:
      if len(str(eval(entr.get()))) > 8:
        back.config(text=str(entr.get())+"="+str(eval(entr.get()))[0:8])  #Déterminer la valeur contenue dans l'argument 'text' contenue dans le Label 'back' comme l'addition du contenu du Label 'entr', du string '=', et du calcul du contenu du Label 'entr'
        result_avt = str(eval(entr.get()))[0:8]  #Déterminer la variable 'result_avt' comme égal au calcul du contenu du Label 'entr'
      else:
        back.config(text=str(entr.get())+"="+str(eval(entr.get())))  #Déterminer la valeur contenue dans l'argument 'text' contenue dans le Label 'back' comme l'addition du contenu du Label 'entr', du string '=', et du calcul du contenu du Label 'entr'
        result_avt = str(eval(entr.get()))  #Déterminer la variable 'result_avt' comme égal au calcul du contenu du Label 'entr'
      calcul_avt = str(entr.get())  #Déterminer la variable 'calcul_avt' comme égal au contenu du Label 'entr'
      entr.delete(0, END)   #Supprimer la valeur, de 0 à la fin, contenue dans le Entry 'entr' 
  elif entr.get() == '':   #si la valeur contenue dans le ENTRY 'entr' est égale à ''
    entr.delete(0,END)    #Supprimer la valeur, de 0 à la fin, contenue dans le Entry 'entr' 
    back.config(text="ERREUR (aucun calcul écrit)")  #Déterminer la valeur contenue dans l'argument 'text' contenue dans le Label 'back' comme égale à "ERREUR (aucun calcul écrit)"
  elif entr.get() == "clear":  #Si la valeur contenue dans le Enrty 'entr' est égale à 'clear'
    entr.delete(0, END) #Supprimer la valeur, de 0 à la fin, contenue dans le Entry 'entr' 
  elif entr.get() == "quit":  #Si la valeur contenue dans le Enrty 'entr' est égale à 'quit'
    window.destroy()  #Executer la fonction 'destroy' pour le fenetre d'application, c'est-a-dire femer la fenetre d'application
  else:     #sinon
    if len(str(eval(entr.get()))) > 8:
      back.config(text=str(entr.get())+"="+str(eval(entr.get()))[0:8])  #Déterminer la valeur contenue dans l'argument 'text' contenue dans le Label 'back' comme l'addition du contenu du Label 'entr', du string '=', et du calcul du contenu du Label 'entr'
      result_avt = str(eval(entr.get()))[0:8]  #Déterminer la variable 'result_avt' comme égal au calcul du contenu du Label 'entr'
    else:
      back.config(text=str(entr.get())+"="+str(eval(entr.get())))  #Déterminer la valeur contenue dans l'argument 'text' contenue dans le Label 'back' comme l'addition du contenu du Label 'entr', du string '=', et du calcul du contenu du Label 'entr'
      result_avt = str(eval(entr.get()))  #Déterminer la variable 'result_avt' comme égal au calcul du contenu du Label 'entr'

    calcul_avt = str(entr.get())  #Déterminer la variable 'calcul_avt' comme égal au contenu du Label 'entr'
    entr.delete(0, END)   #Supprimer la valeur, de 0 à la fin, contenue dans le Entry 'entr' 
 
def rep_function():  #Début de la fonction 'rep_function()'
    entr.insert(END, str(result_avt))  #Insérer la valeur contenu dans la variable 'result_avt', à la fin (='END') de la valeur contenu dans le Enrty 'entr'
 
 
def fraction():  #Début de la fonction 'fraction()'
    global fract_active  #Récupèrer la variable 'fract_active' situé en dehors de la mémoire de la fonction
    if fract_active == False: #Si la variable 'fract_active' est égale à False, c'est-a-dire si le resultat est en décimal et pas en fraction
        back.config(text=calcul_avt+"="+str(Fraction(result_avt))) #Déterminer la valeur contenue dans l'argument 'text' contenue dans le Label 'back' comme l'addition du contenu de la variable 'calcul_avt', du string '=', et du contenu de la variable 'result_avt', convertie en fraction grâce à la fonction Fraction()
        fract_active = True  #Déterminer la variable 'fract_active' comme égale à True, c'est-a-dire que le résultat est en fraction et pas en décimal
    else:  #sinon
        back.config(text=calcul_avt+"="+str(eval(result_avt))) #Déterminer la valeur contenue dans l'argument 'text' contenue dans le Label 'back' comme l'addition du contenu de la variable 'calcul_avt', du string '=', et du calcul du contenu de la variable 'result_avt'
        fract_active = False  #Déterminer la variable 'fract_active' comme égale à False, c'est-a-dire que le résultat est en décimal et pas en fraction

def negatif():  #Début de la fonction 'negatif()'
      entr.insert(END, '(-')  #Insérer la valeur '(-', à la fin (='END') de la valeur contenu dans le Enrty 'entr'
      global parenth  #Récupèrer la variable 'parenth' situé en dehors de la mémoire de la fonction
      parenth = True #Déterminer les parentheses comme ouvertes


##################################INTERFACE GRAPHIQUE######################################
 
entr = Entry(window, text="")    #Déterminer la variable 'entr' comme un Entry de la fenetre 'window', avec un text égale à ''
entr.grid(row=1, column=0, columnspan=4, ipadx=3)  #Déterminer la position dans la grille de l' Entry 'entr', qui est situé dans à la ligne 1 (='row'), dans la colonne 0 (='column') et avec une taille de 4 colonnes de largeur
 
 
back = Label(window, text="")   #Déterminer la variable 'back' comme un Label de la fenetre 'window', avec un text égale à ''
back.grid(row=0, column=1, columnspan=4)    #Déterminer la position dans la grille du Label 'back', qui est situé dans à la ligne 0 (='row'), dans la colonne 0 (='column') et avec une taille de 4 colonnes de largeur
 
zero = Button(window, text="0", command=lambda:ajoute("0"), background='dodger blue', borderwidth=0, width=3)  #Déterminer la variable 'zero' comme un Button de la fenetre 'window', avec un text égale à '0', avec une commande d'éxécution qui est la fonction 'ajoute("0")', avec un arrière plan de couleur 'dodger blue' et avec une taille de bordure égale à 0
zero.grid(row=6, column=1)    #Déterminer la position dans la grille du Label 'zero', qui est situé dans à la ligne 6 (='row') et dans la colonne 1 (='column')
 
un = Button(window, text="1", command=lambda:ajoute("1"), background='dodger blue', borderwidth=0, width=3)  #Déterminer la variable 'un' comme un Button de la fenetre 'window', avec un text égale à '1', avec une commande d'éxécution qui est la fonction 'ajoute("1")', avec un arrière plan de couleur 'dodger blue' et avec une taille de bordure égale à 0
un.grid(row=5, column=0) #Déterminer la position dans la grille du Label 'un', qui est situé dans à la ligne 5 (='row') et dans la colonne 0 (='column')
 
deux = Button(window, text="2", command=lambda:ajoute("2"), background='dodger blue', borderwidth=0, width=3)  #Déterminer la variable 'deux' comme un Button de la fenetre 'window', avec un text égale à '2', avec une commande d'éxécution qui est la fonction 'ajoute("2")', avec un arrière plan de couleur 'dodger blue' et avec une taille de bordure égale à 0
deux.grid(row=5, column=1) #Déterminer la position dans la grille du Label 'deux', qui est situé dans à la ligne 5 (='row') et dans la colonne 1 (='column')
 
trois = Button(window, text="3", command=lambda:ajoute("3"), background='dodger blue', borderwidth=0, width=3)  #Déterminer la variable 'trois' comme un Button de la fenetre 'window', avec un text égale à '3', avec une commande d'éxécution qui est la fonction 'ajoute("03)', avec un arrière plan de couleur 'dodger blue' et avec une taille de bordure égale à 0
trois.grid(row=5, column=2) #Déterminer la position dans la grille du Label 'trois', qui est situé dans à la ligne 5 (='row') et dans la colonne 2 (='column')
 
quatre = Button(window, text="4", command=lambda:ajoute("4"), background='dodger blue', borderwidth=0, width=3)  #Déterminer la variable 'quatre' comme un Button de la fenetre 'window', avec un text égale à '4', avec une commande d'éxécution qui est la fonction 'ajoute("4")', avec un arrière plan de couleur 'dodger blue' et avec une taille de bordure égale à 0
quatre.grid(row=4, column=0) #Déterminer la position dans la grille du Label 'quatre', qui est situé dans à la ligne 4 (='row') et dans la colonne 0 (='column')
 
cinq = Button(window, text="5", command=lambda:ajoute("5"), background='dodger blue', borderwidth=0, width=3)  #Déterminer la variable 'cinq' comme un Button de la fenetre 'window', avec un text égale à '5', avec une commande d'éxécution qui est la fonction 'ajoute("5")', avec un arrière plan de couleur 'dodger blue' et avec une taille de bordure égale à 0
cinq.grid(row=4, column=1) #Déterminer la position dans la grille du Label 'cinq', qui est situé dans à la ligne 4 (='row') et dans la colonne 1 (='column')
 
six = Button(window, text="6", command=lambda:ajoute("6"), background='dodger blue', borderwidth=0, width=3)  #Déterminer la variable 'six' comme un Button de la fenetre 'window', avec un text égale à '6', avec une commande d'éxécution qui est la fonction 'ajoute("6")', avec un arrière plan de couleur 'dodger blue' et avec une taille de bordure égale à 0
six.grid(row=4, column=2) #Déterminer la position dans la grille du Label 'six', qui est situé dans à la ligne 4 (='row') et dans la colonne 2 (='column')
 
sept = Button(window, text="7", command=lambda:ajoute("7"), background='dodger blue', borderwidth=0, width=3)  #Déterminer la variable 'sept' comme un Button de la fenetre 'window', avec un text égale à '7', avec une commande d'éxécution qui est la fonction 'ajoute("7")', avec un arrière plan de couleur 'dodger blue' et avec une taille de bordure égale à 0
sept.grid(row=3, column=0) #Déterminer la position dans la grille du Label 'sept', qui est situé dans à la ligne 3 (='row') et dans la colonne 0 (='column')
 
huit = Button(window, text="8", command=lambda:ajoute("8"), background='dodger blue', borderwidth=0, width=3) #Déterminer la variable 'huit' comme un Button de la fenetre 'window', avec un text égale à '8', avec une commande d'éxécution qui est la fonction 'ajoute("8")', avec un arrière plan de couleur 'dodger blue' et avec une taille de bordure égale à 0
huit.grid(row=3, column=1) #Déterminer la position dans la grille du Label 'huit', qui est situé dans à la ligne 3 (='row') et dans la colonne 1 (='column')
 
neuf = Button(window, text="9", command=lambda:ajoute("9"), background='dodger blue', borderwidth=0, width=3)  #Déterminer la variable 'neuf' comme un Button de la fenetre 'window', avec un text égale à '9', avec une commande d'éxécution qui est la fonction 'ajoute("9")', avec un arrière plan de couleur 'dodger blue' et avec une taille de bordure égale à 0
neuf.grid(row=3, column=2) #Déterminer la position dans la grille du Label 'neuf', qui est situé dans à la ligne 3 (='row') et dans la colonne 2 (='column')
 
plus = Button(window, text="+", command=lambda:ajoute("+"), background='dodger blue', borderwidth=0, width=3)  #Déterminer la variable 'plus' comme un Button de la fenetre 'window', avec un text égale à '+', avec une commande d'éxécution qui est la fonction 'ajoute("+")', avec un arrière plan de couleur 'dodger blue' et avec une taille de bordure égale à 0
plus.grid(row=6, column=3) #Déterminer la position dans la grille du Label 'plus', qui est situé dans à la ligne 6 (='row') et dans la colonne 3 (='column')
 
moins = Button(window, text="-", command=lambda:ajoute("-"), background='dodger blue', borderwidth=0, width=3)  #Déterminer la variable 'moins' comme un Button de la fenetre 'window', avec un text égale à '-', avec une commande d'éxécution qui est la fonction 'ajoute("-")', avec un arrière plan de couleur 'dodger blue' et avec une taille de bordure égale à 0
moins.grid(row=5, column=3) #Déterminer la position dans la grille du Label 'moins', qui est situé dans à la ligne 5 (='row') et dans la colonne 3 (='column')
 
fois = Button(window, text="*", command=lambda:ajoute("*"), background='dodger blue', borderwidth=0, width=3)  #Déterminer la variable 'fois' comme un Button de la fenetre 'window', avec un text égale à '*', avec une commande d'éxécution qui est la fonction 'ajoute("*")', avec un arrière plan de couleur 'dodger blue' et avec une taille de bordure égale à 0
fois.grid(row=4, column=3) #Déterminer la position dans la grille du Label 'fois', qui est situé dans à la ligne 4 (='row'), dans la colonne 2 (='column') et une largeur de 2 (='ipadx')
 
div = Button(window, text="/", command=lambda:ajoute("/"), background='dodger blue', borderwidth=0, width=3)  #Déterminer la variable 'div' comme un Button de la fenetre 'window', avec un text égale à '/', avec une commande d'éxécution qui est la fonction 'ajoute("/")', avec un arrière plan de couleur 'dodger blue' et avec une taille de bordure égale à 0
div.grid(row=3, column=3) #Déterminer la position dans la grille du Label 'div', qui est situé dans à la ligne 3 (='row'), dans la colonne 3 (='column') et une largeur de 3 (='ipadx')
 
egal = Button(window, text="=", command=lambda:calcul(), background='dodger blue', borderwidth=0, width=3)  #Déterminer la variable 'egal' comme un Button de la fenetre 'window', avec un text égale à '=', avec une commande d'éxécution qui est la fonction 'ajoute("=")', avec un arrière plan de couleur 'dodger blue' et avec une taille de bordure égale à 0
egal.grid(row=7, column=3) #Déterminer la position dans la grille du Label 'egal', qui est situé dans à la ligne 7 (='row'), dans la colonne 3 (='column') et une largeur de 0.4 (='ipadx')
 
c = Button(window, text="C", command=supr_entr, background='dodger blue', borderwidth=0, width=3)  #Déterminer la variable 'c' comme un Button de la fenetre 'window', avec un text égale à 'C', avec une commande d'éxécution qui est la fonction 'supr_entr', avec un arrière plan de couleur 'dodger blue' et avec une taille de bordure égale à 0
c.grid(row=2, column=0) #Déterminer la position dans la grille du Label 'c', qui est situé dans à la ligne 0 (='row') et dans la colonne 0 (='column')
 
ce = Button(window, text="CE", command=supr_all, background='dodger blue', borderwidth=0, width=3)  #Déterminer la variable 'ce' comme un Button de la fenetre 'window', avec un text égale à 'CE', avec une commande d'éxécution qui est la fonction 'supr_all', avec un arrière plan de couleur 'dodger blue' et avec une taille de bordure égale à 0
ce.grid(row=2, column=1) #Déterminer la position dans la grille du Label 'ce', qui est situé dans à la ligne 2 (='row') et dans la colonne 1 (='column')
 
racine = Button(window, text="√", command=lambda:ajoute("sqrt("), background='dodger blue', borderwidth=0, width=3)  #Déterminer la variable 'racine' comme un Button de la fenetre 'window', avec un text égale à '√', avec une commande d'éxécution qui est la fonction 'ajoute("sqrt(")', avec un arrière plan de couleur 'dodger blue' et avec une taille de bordure égale à 0
racine.grid(row=2, column=2) #Déterminer la position dans la grille du Label 'racine', qui est situé dans à la ligne 2 (='row') et dans la colonne 2 (='column')
 
opp = Button(window, text="±", command=lambda:negatif(), background='dodger blue', borderwidth=0, width=3)  #Déterminer la variable 'opp' comme un Button de la fenetre 'window', avec un text égale à '±', avec une commande d'éxécution qui est la fonction 'negatif()', avec un arrière plan de couleur 'dodger blue' et avec une taille de bordure égale à 0
opp.grid(row=6 ,column=0) #Déterminer la position dans la grille du Label 'opp', qui est situé dans à la ligne 6 (='row') et dans la colonne 0 (='column')
 
virgule = Button(window, text=".", command=lambda:ajoute("."), background='dodger blue', borderwidth=0, width=3)  #Déterminer la variable 'virgule' comme un Button de la fenetre 'window', avec un text égale à '.', avec une commande d'éxécution qui est la fonction 'ajoute(".")', avec un arrière plan de couleur 'dodger blue' et avec une taille de bordure égale à 0
virgule.grid(row=6, column=2) #Déterminer la position dans la grille du Label 'virgule', qui est situé dans à la ligne 6 (='row') et dans la colonne 2 (='column') et une largeur de 2 (='ipadx')
 
carré = Button(window, text="x²", command=lambda:ajoute("²"), background='dodger blue', borderwidth=0, width=3)  #Déterminer la variable 'carré' comme un Button de la fenetre 'window', avec un text égale à '²', avec une commande d'éxécution qui est la fonction 'ajoute("²")', avec un arrière plan de couleur 'dodger blue' et avec une taille de bordure égale à 0
carré.grid(row=2, column=3) #Déterminer la position dans la grille du Label 'carré', qui est situé dans à la ligne 2 (='row') et dans la colonne 3 (='column') et une largeur de 1 (='ipadx')
 
rep = Button(window, text="rep", command=lambda:rep_function(), background='dodger blue', borderwidth=0, width=3)  #Déterminer la variable 'rep' comme un Button de la fenetre 'window', avec un text égale à 'rep', avec une commande d'éxécution qui est la fonction 'rep_function()', avec un arrière plan de couleur 'dodger blue', avec une taille de bordure égale à 0 et avec une taille de texte de 7
rep.grid(row=7, column=0) #Déterminer la position dans la grille du Label 'rep', qui est situé dans à la ligne 7 (='row') et dans la colonne 0 (='column') et une largeur de 1.5 (='ipadx')
 
fract = Button(window, text="<>", command=lambda:fraction(), background='dodger blue', borderwidth=0, width=3)  #Déterminer la variable 'fract' comme un Button de la fenetre 'window', avec un text égale à '<>', avec une commande d'éxécution qui est la fonction 'fraction()', avec un arrière plan de couleur 'dodger blue', avec une taille de bordure égale à 0 et avec une taille de texte de 8
fract.grid(row=7, column=1) #Déterminer la position dans la grille du Label 'fract', qui est situé dans à la ligne 7 (='row') et dans la colonne 1 (='column')
 
parentheses = Button(window, text="()", command=lambda:ajoute("()"), background='dodger blue', borderwidth=0, width=3)  #Déterminer la variable 'parentheses' comme un Button de la fenetre 'window', avec un text égale à '()', avec une commande d'éxécution qui est la fonction 'ajoute("()")', avec un arrière plan de couleur 'dodger blue', avec une taille de bordure égale à 0 et avec une taille de texte de 9
parentheses.grid(row=7, column=2) #Déterminer la position dans la grille du Label 'parentheses', qui est situé dans à la ligne 7 (='row') et dans la colonne 2 (='column')

hlp = Button(window, text="?", borderwidth=0, font=font.Font(size=8))
hlp.grid(row=7, column=4)
 


###################################TOUCHES AU CLAVIER######################################

window.bind('1', un['command'])    #si la touche '1' sur le clavier est préssée, alors efectuer la commande du Boutton 'un'
window.bind('2', deux['command'])    #si la touche '2' sur le clavier est préssée, alors efectuer la commande du Boutton 'deux'
window.bind('3', trois['command'])    #si la touche '3' sur le clavier est préssée, alors efectuer la commande du Boutton 'trois'
window.bind('4', quatre['command'])    #si la touche '4' sur le clavier est préssée, alors efectuer la commande du Boutton 'quatre'
window.bind('5', cinq['command'])    #si la touche '5' sur le clavier est préssée, alors efectuer la commande du Boutton 'cinq'
window.bind('6', six['command'])    #si la touche '6' sur le clavier est préssée, alors efectuer la commande du Boutton 'six'
window.bind('7', sept['command'])    #si la touche '7' sur le clavier est préssée, alors efectuer la commande du Boutton 'sept'
window.bind('8', huit['command'])    #si la touche '8' sur le clavier est préssée, alors efectuer la commande du Boutton 'huit'
window.bind('9', neuf['command'])    #si la touche '9' sur le clavier est préssée, alors efectuer la commande du Boutton 'neuf'
window.bind('+', plus['command'])    #si la touche '+' sur le clavier est préssée, alors efectuer la commande du Boutton 'dix'
window.bind('-', moins['command'])    #si la touche '-' sur le clavier est préssée, alors efectuer la commande du Boutton 'moins'
window.bind('*', fois['command'])    #si la touche '*' sur le clavier est préssée, alors efectuer la commande du Boutton 'fois'
window.bind('/', div['command'])    #si la touche '/' sur le clavier est préssée, alors efectuer la commande du Boutton 'div'
window.bind('=', egal['command'])    #si la touche '=' sur le clavier est préssée, alors efectuer la commande du Boutton 'egal'
window.bind('.', virgule['command'])    #si la touche '.' sur le clavier est préssée, alors efectuer la commande du Boutton 'virgule'
window.bind('c', c['command'])    #si la touche 'c' sur le clavier est préssée, alors efectuer la commande du Boutton 'c'
window.bind('C', c['command'])    #si la touche 'C' sur le clavier est préssée, alors efectuer la commande du Boutton 'c'
window.bind('<Alt-KeyPress-c>', ce['command'])    #si la touche '<Alt-KeyPress-c>' sur le clavier est préssée, alors efectuer la commande du Boutton 'ce'




window.mainloop()
