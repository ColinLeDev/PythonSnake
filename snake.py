import time as tps
import curses
from curses import binascii as ba
from curses import KEY_RIGHT, KEY_LEFT, KEY_UP, KEY_DOWN
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

def control(win, key, keys = [KEY_RIGHT, KEY_LEFT, KEY_UP, KEY_DOWN, 27]):
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
	if key == "" or key not in keys :
		key = old_key

	# Raffaichissement de la fenètre
	win.refresh()

	# retourne le code la touche
	return key


def jeu(win):
	'''
	Moteur du jeu
	paramètre :
	  win : fenètre en cours
	retour :
	  score à la fin du jeu
	'''

	# initialisation du jeu
	# Le serpent se dirige vers la droite au début du jeu.
	# C'est comme si le joueur avait utilisé la flèche droite au clavier
	key = KEY_RIGHT
	score = 0

	# Definition des coordonnées du serpent
	# Le serpent est une liste de d'anneaux composées de leurs coordonnées ligne, colonne
	# La tête du serpent est en 4,10, l'anneau 1 en 4,9, le 2 en 4,8
	snake = [[4, 10], [4, 9], [4, 8]]

	# La nouriture (pomme) se trouve en 10,20
	food = [10, 20]

	# Affichage la nouriture en vert sur fond noir dans la fenêtre
	curses.init_pair(2, curses.green, curses.black)
	win.addch(food[0], food[1], chr(211), curses.color_pair(2))  # Prints the food

	# Affichage du serpent en bleu sur fond jaune
	curses.init_pair(3, curses.blue, curses.yellow)
	# sur toute la longeur du serpent
	for i in range(1,3):
		# affichage de chaque anneau dans la fenêtre en ligne, colonne
		win.addstr(snake[i][0], snake[i][1], '*', curses.color_pair(3))

	# Emission d'un beep  au début du jeu
	curses.beep()

	# Tant que le joueur n'a pas quitter le jeu
	end = False
	while key != 27 and not end:
		key = controle(win, key)
		snake, score = deplacement(win, score, key, snake, food)
		end = perdu(win, snake)
	return score






def deplacement(win, score, key, snake, food):
	'''
	Déplacements du serpent
	paramètres :
	  win : fenètre en cours
	  score : score en cours
	  key : touche de controle en cours
	  snake : liste des positions en cours des anneaux du serpent
	  food : liste de la position de la pomme
	retourne :
	  tuple contenant la liste des positions en cours des anneaux du serpent et score en cours
	'''
	# Si on appui sur la flèche "à droite",
	# la tête se déplace de 1 caractère vers la droite (colonne + 1)
	if key == KEY_RIGHT:
		snake.insert(0, [snake[0][0], snake[0][1]+1])

	# Sinon si on appui sur la flèche "à gauche",
	# la tête se déplace de 1 caractère vers la gauche (colonne - 1)
	elif key == KEY_LEFT:
		snake.insert(0, [snake[0][0], snake[0][1]-1])

	# Sinon si on appui sur la flèche "en haut",
	# la tête se déplace de 1 caractère vers le haut (ligne - 1)
	elif key == KEY_UP:
		snake.insert(0, [snake[0][0]-1, snake[0][1]])

	# Sinon si on appui sur la flèche "en bas",
	# la tête se déplace de 1 caractère vers le bas (ligne + 1)
	elif key == KEY_DOWN:
		snake.insert(0, [snake[0][0]+1, snake[0][1]])










title()
curses.initscr()
curses.start_color()
affichage_aire_de_jeu(20, 60, titolo)
curses.napms(10000)
curses.endwin()























