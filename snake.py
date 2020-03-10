import curses 
import random

s= curses.initscr() #iniciando uma tela com curses
curses.curs_set(0) #colocando o cursor em 0, ou seuja na posioo zero do meu role
sh, sw =s.getmaxyx() #pegando atraves de getmaxyx a profundidade e a altura da tela
w= curses.newwin(sh, sw, 0, 0)
w.keypad(1)
w.timeout(100) #refresh the screen a cada 100 milisegundos 

snk_x= sw/4 #posio inicial x da cobrinha
snk_y= sw/2 #posio inicial y da cobrinha
 
#desenvolvedo a cobra, o interessante aqui  que ele criou uma lista para a cobra, suponha que a cada vez que a cobra ingerir um alimento ela ira adicionar um elemento a lista
snake=[
	[snk_y,snk_x],
	[snk_y,snk_x-1],
	[snk_y,snk_x-2]]

food=[sh/2, sw/2]# posio da comida da cobra
'''print (food[0], '\n')
print (food[1], '\n')
quit()'''
w.addch(int(food[0]), int(food[1]), "o") # addch adicona um caracter na tela (x, y, tipo de caracter)
key=curses.KEY_RIGHT #caminho inicial da cobra
while True:
	next_key =w.getch() # proxima tecla para descobrir a direo da cobrinha
	key =key if next_key == -1 else next_key # retorna nada ou a proxima tecla
	
	if snake[0][0] in [0,sh] or snake[0][1] in [0,sw] or snake[0] in snake[1:]:
		curses.endwin()
		quit()
		
	new_head=[snake[0][0],snake[0][1]]
	if key == curses.KEY_DOWN:	new_head[0] +=1
	if key == curses.KEY_UP: 	new_head[0] -=1
	if key == curses.KEY_LEFT:	new_head[1] -=1
	if key == curses.KEY_RIGHT: 	new_head[1] +=1
	
	snake.insert(0,new_head)	
	if snake[0] ==food:
		food= None
		while food is None:
			nf=[	
				random.randint(1,sh-1),
				random.randint(1,sw-1)
			]
			food =nf if nf not in snake else None
		w.addch(food[0], food[1], curses.ACS_PI) 
	else:
		tail =snake.pop()
		w.addch(int(tail[0]), int(tail[1]),'')
	w.addch(snake[0][0], snake[0][1], curses.ACS_CKBOARD)	
	
	


