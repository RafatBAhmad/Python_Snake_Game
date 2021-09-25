import random
import curses

screen = curses.initscr() #initailze the screen
curses.curs_set(0) #set the cursor state, 0 invisible, 1 normal, 2 very visible
screen_hight, screen_width = screen.getmaxyx()  # getmaxyx Tuple of y and x of the Screen
windoow = curses.newwin(screen_hight,screen_width,0,0) #to make a window in the screen
windoow.keypad(1) #to let the window nows that it will be receved data from kaypad to enable this function
windoow.timeout(100) # refresh the secren evry 100 mileSecond

#the destination of the snake
snk_x = screen_width//4  # // to make the value integer
snk_y = screen_hight//2
snake = [
    [snk_y, snk_x], # y axis , x axis
    [snk_y, snk_x-1],
    [snk_y, snk_x-2],
    [snk_y, snk_x-3]
]

food = [screen_hight//2, screen_width//2]
windoow.addch(food[0], food[1], "*")

key = curses.KEY_RIGHT # key holds which butten we prees, and we assume it's to the right for first time

while True:
    next_key = windoow.getch() # get the next character from the user
    key = key if next_key == -1 else next_key #-1 means that the user still not press any character(butten)

    if snake[0][0] in [0, screen_hight] or snake[0][1] in [0, screen_width] or snake[0] in snake[1:]: #to see if the snake hit anything or itself
        curses.endwin() #snake[0] its the first row ie the head of snake if it hit any part of the snake body snake[1:] 
        quit()

    new_head = [snake[0][0], snake[0][1]] # define the head to be the first part of the snake

    #to move the snake head in order what the user enter
    if key == curses.KEY_DOWN:
        new_head[0] += 1 #y axis +1 so the head go down

    if key == curses.KEY_UP:
        new_head[0] -= 1  # y axis -1 so the head go up

    if key == curses.KEY_RIGHT:
        new_head[1] += 1  # x axis +1 so the head go right

    if key == curses.KEY_LEFT:
        new_head[1] -= 1  # x axis -1 so the head go left

    snake.insert(0, new_head) #insert the new position to the snake list (body) in position 0 which is the head 

    if snake[0] == food:  # if the head position equals the food position
        food = None #make the food is none
        while food is None: #if there is no food make a new food with random libary, we cohice from 1 to screen_hight -1 cause if snake hit the hight you will loss 
            new_food = [ 
                random.randint(1, screen_hight-1),
                random.randint(1, screen_width-1)
            ]
            food = new_food if new_food not in snake else None
        windoow.addch(food[0], food[1], "*")
    else: #we pop the tail so to ensure the snake body does not grow when the user hit an input
        tail = snake.pop()
        windoow.addch(tail[0], tail[1], ' ')

    windoow.addch(snake[0][0], snake[0][1], curses.ACS_CKBOARD)   #display the head as check board         
