"""
EV3 program that binds my keyboard to the robot which can then be remotely controlled
Author: Daniel Luu
Date: 20 May 2016
"""

import time
import termios
import tty
import ev3dev.ev3 as ev3
import sys, os
from ev3dev.auto import *

motor_right = LargeMotor(OUTPUT_D)
motor_left = LargeMotor(OUTPUT_A)
lift = MediumMotor(OUTPUT_B)

#==============================================

def getch():
   fd = sys.stdin.fileno()
   old_settings = termios.tcgetattr(fd)
   try:
      tty.setraw(fd)
      ch = sys.stdin.read(1)
   finally:
      termios.tcsetattr(fd, termios.TCSADRAIN, old_settings)
   
   return ch

#==============================================

def destroy():
	while lift.position > -700:
		lift.run_to_abs_pos(duty_cycle_sp=100,position_sp=-700)
def reset():	
	while lift.position <-10:
		lift.run_to_abs_pos(duty_cycle_sp=100,position_sp=-10)

#==============================================

def forward():
   motor_left.run_direct(duty_cycle_sp=70)
   motor_right.run_direct(duty_cycle_sp=70)

#==============================================

def back():
   motor_left.run_direct(duty_cycle_sp=-70)
   motor_right.run_direct(duty_cycle_sp=-70)

#==============================================

def left():
   motor_left.run_direct( duty_cycle_sp=-30)
   motor_right.run_direct( duty_cycle_sp=30)

#==============================================

def right():
   motor_left.run_direct( duty_cycle_sp=30)
   motor_right.run_direct( duty_cycle_sp=-30)

#==============================================

def stop():
   motor_left.run_direct( duty_cycle_sp=0)
   motor_right.run_direct( duty_cycle_sp=-0)
   
def isClosed():
    if(lift.position > -600):
        return False
    else:
        return True

#==============================================

while True:
   k = getch()
   print(k)
   print isClosed()
   if k == 'w':
      forward()
   if k == 's':
      back()
   if k == 'a':
      left()
   if k == 'd':
      right()
   if k == 'q':
      destroy()
   if k == 'e':
      reset()
   if k == ' ':
      stop()
   if k == 'p':
      exit()