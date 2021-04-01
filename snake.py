import time as tps
import curses
titolo="PythonSnake"
titre =['  _______     _________ _    _  ____  _   _    _____ _   _          _  ________ ',
        ' |  __ \ \   / |__   __| |  | |/ __ \| \ | |  / ____| \ | |   /\   | |/ |  ____|',
        ' | |__) \ \_/ /   | |  | |__| | |  | |  \| | | (___ |  \| |  /  \  |   /| |__   ',
        ' |  ___/ \   /    | |  |  __  | |  | | . ` |  \___ \| . ` | / /\ \ |  < |  __|  ',
        ' | |      | |     | |  | |  | | |__| | |\  |  ____) | |\  |/ ____ \| . \| |____ ',
        ' |_|      |_|     |_|  |_|  |_|\____/|_| \_| |_____/|_| \_/_/    \_|_|\_|______|']
def title():
  for title in titre:
    print(title)
  tps.sleep(2)
  print("\n\n\n")




def affichage_aire_de_jeu(hauteur, largeur, tit):

    # Création d'une nouvelle fenètre en 0, 0
    win = curses.newwin(hauteur,largeur,0,0)
    # Les séquences d'échapement sont générés par certaines touches, les autres n'ont aucun effet
    win.keypad(True)
    # L'écho des caractères saisis est désactivé
    curses.noecho(True)
    # Pas de curseur visible
    curses.curs_set(0)
    # La saisie de caractère est non bloquante
    win.nodelay(1)
    # La fenètre a une bordure standard
    win.box
    # Définition d'une couleur pour le titre : texte en rouge sur fond blanc
    # Voir dans la documentation la table "lists the predefined colors"
    curses.init_pair(1, curses.red, curses.white)
    # Affichage du titre
    win.addstr(0, 27, titre, curses.color_pair(1))
    # Raffraichissement de la fenêtre
    win.refresh()
    # Emission d'un beep
    curses.beep()
    # retourner la fenêtre
    return win

def control(win, key, keys = [____]):
	'''
	Controles de jeu
	paramètres :
	  win : fenètre en cours
	  key : dernière touche reconnue
	  keys: liste des touches acceptées par défaut
	retour :
	  code de la touche reconnue
	'''
	# Sauvegarde de la dernière touche reconnue
	old_key = key

	# Aquisition d'un nouveau caractère depuis le clavier
	key = win.getch()

	# Si aucune touche actionnée (pas de nouveau caractère)
	# ou pas dans la liste des touches acceptées
	# key prend la valeur de la dernière touche connue
	if key == None or key not in keys :
		key = old_key

	# Raffaichissement de la fenètre
	win.refresh()

	# retourne le code la touche
	return key















title()
curses.initscr()
curses.start_color()
affichage_aire_de_jeu(20, 60, titolo)
curses.napms(10000)
curses.endwin()























