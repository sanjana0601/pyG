import pygame
import random
import time

pygame.init()

screen_width=500
screen_height=400
screen=pygame.display.set_mode((screen_width,screen_height))
class snake:
    def __init__(self,x,y,width,height):
    
        self.green_color=(0,255,0)
        self.x=x
        self.y=y
        self.width=width
        self.height=height
        self.speed=5
        self.dir_x=0
        self.dir_y=0
        self.direction="RIGHT"
        self.snake_list=[]
        self.snake_length=1
        
    def change_direction(self,user_dir):
        if user_dir=="RIGHT" and self.direction!="LEFT":
            self.direction="RIGHT"
        elif user_dir=="LEFT" and self.direction!="RIGHT":
            self.direction="LEFT"
        elif user_dir=="UP" and self.direction!="DOWN":
            self.direction="UP"
        elif user_dir=="DOWN" and self.direction!="UP":
            self.direction="DOWN"
            
    def move_snake(self):
        if self.direction=="RIGHT":
            self.dir_x=0
            self.dir_x=self.dir_x+self.speed
            self.dir_y=0
        elif self.direction=="LEFT":
            self.dir_x=0
            self.dir_x=self.dir_x-self.speed
            self.dir_y=0
        elif self.direction=="DOWN":
            self.dir_y=0
            self.dir_y=self.dir_y+self.speed
            self.dir_x=0
        elif self.direction=="UP":
            self.dir_y=0
            self.dir_y=self.dir_y-self.speed
            self.dir_x=0
    def check_boarder(self):
        if self.x>screen_width:
            self.x=0
        elif self.x<0:
            self.x=screen_width
        elif self.y>screen_height:
            self.y=0
        elif self.y<0:
            self.y=screen_height

class Food:
    def __init__(self,size):
        self.x=random.randint(0,screen_width)
        self.y=random.randint(0,screen_height)
        self.size=size
        self.red_color=(255,0,0)
snake=snake(50,100,15,15)
food=Food(8)
clock=pygame.time.Clock()
font=pygame.font.SysFont(None,20)

while True:
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            pygame.quit()
            exit()
    keys=pygame.key.get_pressed()
    if keys[pygame.K_RIGHT]:
        snake.change_direction("RIGHT")
    elif keys[pygame.K_LEFT]:
        snake.change_direction("LEFT")
    elif keys[pygame.K_UP]:
        snake.change_direction("UP")
    elif keys[pygame.K_DOWN]: 
        snake.change_direction("DOWN")
        
    snake.move_snake()
    snake.check_boarder()
    snake.x=snake.x+snake.dir_x
    snake.y=snake.y+snake.dir_y
    screen.fill((0,0,0))
    for x,y in snake.snake_list:
        snake_box=pygame.draw.rect(screen,snake.green_color,(x,y,snake.width,snake.height))
        food_box=pygame.draw.circle(screen,food.red_color,(food.x,food.y),food.size)
        if snake_box.colliderect(food_box):
            food=Food(8)
            snake.snake_length+=1
          

    snake.snake_list.append([snake.x,snake.y])
    if len(snake.snake_list)>snake.snake_length:
        snake.snake_list.pop(0)

    if snake.snake_list[-1] in snake.snake_list[:-1]:
        time.sleep(2)
        snake.snake_list.clear()
        snake.snake_length=1
        
    screen_text=font.render(f"Score-{snake.snake_length-1}",True,(255,255,255))
    screen.blit(screen_text,(10,10))
    pygame.display.update()
    clock.tick(60)
