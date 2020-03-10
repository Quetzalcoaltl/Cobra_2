"""fontes:
    https://www.youtube.com/watch?v=rbasThWVb-c
    https://docs.python.org/2/library/curses.html
    """
import random as rd
import curses 

i=curses.initscr()

curses.curs_set(0) # não quero nenhum pont inicial na minha tela
sh, sw=i.getmaxyx()
tela=curses.newwin(sh,sw,0,0)
tela.keypad(1)
tela.timeout(100)

delay=input("aperte enter:")
