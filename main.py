import asyncio
import sys
import pygame
import turtle as trtl
from turtle import *
from random import randint

# screen and variables
wn = trtl.Screen()
num = 0
wn.setup(width=800, height=600)
wn.bgpic("help.png")
screen = Screen()
barrier = True
next = 0
value = 1
value2 = 1
value3 = 1
Scene1 = "SCENE1.png"
Scene2 = "SCENE2.png"
Scene3 = "SCENE3.png"
Scene4 = "end.png"
choice_value = 0
L = 1
R = 1
red = '\033[31m'
invalid = True
repeat = 0

player_options_still_right = ["catstillR.gif", "armadillostillR.gif", "foxstillR.gif"]
player_options_walk_right = ["catwalkR.gif", "armadillowalkR.gif", "foxwalkR.gif"]
player_options_still_left = ["catstillL.gif", "armadillostillL.gif", "foxstillL.gif"]
player_options_walk_left = ["catwalkL.gif", "armadillowalkL.gif", "foxwalkL.gif"]


# enemy
enemy = "spider_full.gif"
wn.addshape(enemy)
enemy2 = "spider_full.gif"
wn.addshape(enemy2)
enemy3 = "spider_full.gif"
wn.addshape(enemy3)
spider = trtl.Turtle()
spider.shape(enemy)
spider.penup()
spider2 = trtl.Turtle()
spider2.shape(enemy2)
spider2.penup()
spider3 = trtl.Turtle()
spider3.shape(enemy3)
spider3.penup()


# functions
def rand_pos():
  for enemies in range(1):
    x = randint(-300,-140)
    y = -230
    spider.goto(x, y)
    spider_pos = spider.pos()
    x = randint(-130,0)
    spider2.goto(x, y)
    spider2_pos = spider2.pos()
    x = randint(50,300)
    spider3.goto(x, y)
    spider3_pos = spider3.pos()
    
    player_options_still_right = ["catstillR.gif", "armadillostillR.gif", "foxstillR.gif"]
    player_options_walk_right = ["catwalkR.gif", "armadillowalkR.gif", "foxwalkR.gif"]
    player_options_still_left = ["catstillL.gif", "armadillostillL.gif", "foxstillL.gif"]
    player_options_walk_left = ["catwalkL.gif", "armadillowalkL.gif", "foxwalkL.gif"]
    
def reset():
  global player_options_still_right
  global player_options_walk_right
  global player_options_still_left
  global player_options_walk_left
  player_options_still_right = ["catstillR.gif", "armadillostillR.gif", "foxstillR.gif"]
  player_options_walk_right = ["catwalkR.gif", "armadillowalkR.gif", "foxwalkR.gif"]
  player_options_still_left = ["catstillL.gif", "armadillostillL.gif", "foxstillL.gif"]
  player_options_walk_left = ["catwalkL.gif", "armadillowalkL.gif", "foxwalkL.gif"]
  enemy = "spider_full.gif"
  wn.addshape(enemy)
  enemy2 = "spider_full.gif"
  wn.addshape(enemy2)
  enemy3 = "spider_full.gif"
  wn.addshape(enemy3)
  spider.shape(enemy)
  spider2.shape(enemy2)
  spider3.shape(enemy3)
  penup()
  goto(-400, -230)
  
def start_up(choice):
  global still_right
  global walk_right
  global still_left
  global walk_left
  global player_var1
  global player_var2
  global player_var3
  global player_var4
  global invalid
  global repeat
  global value
  global value2
  global value3
  global next
  
  wn.bgpic("help.png")
  if next == 0:
    value = 0
    value2 = 0
    value3 = 0
    spider.showturtle()
    spider2.showturtle()
    spider3.showturtle()
    invalid = True
  rand_pos()
  reset()
  
  while invalid == True:
    if repeat == 1:
      print(red + "Please type animal exactly as given Ex: Cat not cat \033[39m")
      choice = input("What animal do you want to be? Cat/Armadillo/Fox")
    repeat = 1
    if choice == "Cat":
      invalid = False
      choice_value = 0
    elif choice == "Armadillo":
      choice_value = 1
      invalid = False
    elif choice == "Fox":
      choice_value = 2
      invalid = False
    else:
      invalid = True
  
  if invalid == False:
    player_selected = player_options_still_right.pop(choice_value)
    player_var = player_selected
    still_right = player_var
    
    player_selected2 = player_options_walk_right.pop(choice_value)
    player_var2 = player_selected2
    walk_right = player_var2
    
    player_selected3 = player_options_still_left.pop(choice_value)
    player_var3 = player_selected3
    still_left = player_var3
    
    player_selected4 = player_options_walk_left.pop(choice_value)
    player_var4 = player_selected4
    walk_left = player_var4

print(red + "Please type animal exactly as given Ex: Cat not cat \033[39m")
choice = input("What animal do you want to be? Cat/Armadillo/Fox")
start_up(choice)
  
while invalid == True:
  start_up(choice)
  
def position_check():
  global num
  global barrier
  global next
  global invalid
  if next == 1:
    barrier = False
    if barrier == False:
      if (400,-230) < pos():
        wn.bgpic(Scene1)
        goto(-400,-230)
        spider.showturtle()
        spider2.showturtle()
        spider3.showturtle()
        rand_pos()
        reset()
        next = next + 1
        barrier = True
  if next == 3:
    barrier = False
    if barrier == False:
      if (400,-230) < pos():
        wn.bgpic(Scene2)
        goto(-400,-230)
        spider.showturtle()
        spider2.showturtle()
        spider3.showturtle()
        rand_pos()
        reset()
        next = next + 1
        barrier = True
  if next == 5:
    barrier = False
    if barrier == False:
      if (400,-230) < pos():
        wn.bgpic(Scene3)
        goto(-400,-230)
        spider.showturtle()
        spider2.showturtle()
        spider3.showturtle()
        rand_pos()
        reset()
        next = next + 1
        barrier = True
  if next == 7:
    if (400,-230) < pos():
      play_again = input("Congratulations you defeated all the spiders! Would you like to play again? y/n")
      next = 8
    if next == 8:
      if play_again == "y":
        invalid = True
        next = 0
        start_up(choice)
      else:
        print("The End")
        wn.bgpic(Scene4)
  
  if pos() > (400,-230):
    while barrier == True and pos() > (400,-230):
      goto(400, -230)
      
  while pos() < (-400,-230):
    goto(-400,-230)
    
# collision
def pos_check2():
  if pos() <= spider.pos() + (50,0) and pos() >= spider.pos() - (50,0):
    screen.onkey(attack, 'space')
  elif pos() <= spider2.pos() + (50,0) and pos() >= spider2.pos() - (50,0):
    screen.onkey(attack, 'space')
  elif pos() <= spider3.pos() + (50,0) and pos() >= spider3.pos() - (50,0):
    screen.onkey(attack, 'space')  
  else:
    screen.onkey(null, 'space')
    
def null():
  null = True
  
def go():
  global R
  cat.forward = forward(15)
  position_check()
  pos_check2()
  if (R % 2) == 0:
    wn.addshape(walk_right)
    shape(walk_right)
    R = R + 1
  else:
    wn.addshape(still_right)
    shape(still_right)
    R = R + 1
    clear()

def back():
  global L 
  cat.backward = backward(15)
  position_check()
  pos_check2()
  if (L % 2) == 0:
    wn.addshape(walk_left)
    shape(walk_left)
    L = L + 1
  else:
    wn.addshape(still_left)
    shape(still_left)
    L = L + 1
    clear()
    
def attack():
  if pos() <= spider.pos() + (10,0) and pos() >= spider.pos() - (10,0):
    global enemy
    global value
    if value == 1:
      enemy = "spider_3rd.gif"
      wn.addshape(enemy)
      spider.shape(enemy)
    if value == 2:
      enemy = "spider_half.gif"
      wn.addshape(enemy)
      spider.shape(enemy)
    if value == 3:
      enemy = "spider_1 4th.gif"
      wn.addshape(enemy)
      spider.shape(enemy)
    if value == 4:
      spider.hideturtle()
      value = 0
    value = value + 1
    
  if pos() <= spider2.pos() + (10,0) and pos() >= spider2.pos() - (10,0):
    global enemy2
    global value2
    if value2 == 1:
      enemy2 = "spider_3rd.gif"
      wn.addshape(enemy2)
      spider2.shape(enemy2)
    if value2 == 2:
      enemy2 = "spider_half.gif"
      wn.addshape(enemy2)
      spider2.shape(enemy2)
    if value2 == 3:
      enemy2 = "spider_1 4th.gif"
      wn.addshape(enemy2)
      spider2.shape(enemy2)
    if value2 == 4:
      spider2.hideturtle()
      value2 = 0
    value2 = value2 + 1
    
  if pos() <= spider3.pos() + (10,0) and pos() >= spider3.pos() - (10,0):
    global enemy3
    global value3
    global next
    if value3 == 1:
      enemy3 = "spider_3rd.gif"
      wn.addshape(enemy3)
      spider3.shape(enemy3)
    if value3 == 2:
      enemy3 = "spider_half.gif"
      wn.addshape(enemy3)
      spider3.shape(enemy3)
    if value3 == 3:
      enemy3 = "spider_1 4th.gif"
      wn.addshape(enemy3)
      spider3.shape(enemy3)
    if value3 == 4:
      next = next + 1
      spider3.hideturtle()
      value3 = 0
    value3 = value3 + 1


  
wn.addshape(still_right)
shape(still_right)
cat = trtl.Turtle(shape=still_right)
penup()
speed(0)
goto(-400,-230)
cat.hideturtle()  

screen.onkey(back, 'a')
screen.onkey(go, 'd')
screen.listen()

async def main():
  wn.mainloop()
  await asyncio.sleep(0)

asyncio.run(main())

