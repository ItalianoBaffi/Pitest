#!/usr/bin/python

from Tkinter import *
import ttk
import RPi.GPIO as GPIO
import time
import os, random

rootWindow = Tk()
rootWindow.title('Countdown Timer')
#rootWindow.geometry("1680x1050") BK
rootWindow.geometry("1680x800")
rootWindow.resizable(0,0)

defaultColour = rootWindow.cget("bg")

topBar1 = ttk.Frame(rootWindow, border=2, relief=RAISED, padding="410 350 410 380")
topBar1.grid(row=1, column=1, columnspan=1050, rowspan=5)

time1 = ''
prevSec = ''
mins = 0
secs = 10
hours = 0
running = True
start = 17 # Broadcom pin 17 (P1 pin 11)
stop = 27
restart = 22
GPIO.setmode(GPIO.BCM) # Broadcom pin-numbering scheme
GPIO.setup(start, GPIO.IN, pull_up_down=GPIO.PUD_UP) # Button pin set as input w/ pull-up
GPIO.setup(stop, GPIO.IN, pull_up_down=GPIO.PUD_UP) # Button pin set as input w/ pull-up
GPIO.setup(restart, GPIO.IN, pull_up_down=GPIO.PUD_UP) # Button pin set as input w/ pull-up


clock = Label(topBar1, font=('fixed', 200, 'bold'))
#clock = Label(rootWindow, font=('fixed', 300))
clock.grid(row = 4, column = 4, padx = 5, pady = (5,2))
#Row changes horizontal location		BK

def tick():
    global prevSec, time1, secs, mins, hours, running, done, undo, redo
    # get the current local time from the PC
    time2 = time.strftime('%Y/%m/%d %H:%M:%S')
    if running:
        newSec = time.strftime('%S')
    else:
        newSec = ''
        prevSec = ''
    if newSec != prevSec:
	if mins>0 and secs == 0:
		secs=60
		mins=mins-1
		#done=GPIO.input(start)
		#if done==False:
		#	start_btn()
		#redo=GPIO.input(stop)
		#if redo==False:
		#	pause()
		#undo=GPIO.input(restart)
		#if undo==False:
		#	reset()
			
	if secs>=1:
		secs=secs-1
		done=GPIO.input(start)
		if done==False:
			rndmp3 ()
			start_btn
		#if done==True:
		#	os.system('omxplayer -o local /home/pi/Music/WallE/wall-e3.mp3')
		redo=GPIO.input(stop)
		if redo==False:
			pause()
		undo=GPIO.input(restart)
		if undo==False:
			reset()

		#state=GPIO.input(butPin)
	        #if state==False:
        	#        pause()
                #other=GPIO.input(test)
                #if other==False:
                #        reset()
	if secs==0 and mins==0:
		secs=0
		pause()
		#rndmp3 ()
    prevSec = newSec
	#state=GPIO.input(butPin)
        #if state==False:
         #       pause()
        #other=GPIO.input(test)
        #if other==False:
        #        reset()

	#if mins==0:
       	#if secs == 0:
           #secs = 59
           #mins = mins - 1
	#   		secs=0
	 ######  		pause()
	#if mins == 0:
		#if secs == 0:
    #state=GPIO.input(butPin)
    #if state==False:
     #   pause()
    #BK exit(0) exits program
    #state=GPIO.input(butPin)
    #if state==False:
		
	
                #hours = hours - 1
              #  if hours < 0:
               #     hours = 0
                #    mins = 0
                 #   secs = 0
                 #   clock.config(bg='dark red')
    time2 = '%02d:%02d' % (mins, secs)
    # if time string has changed, update it
    if time2 != time1:
       time1 = time2
       clock.config(text=time2)
    # calls itself every 200 milliseconds
    # to update the display as needed
    # could use >200 ms, but display gets jerky
    clock.after(200, tick)
tick()
def start_btn():
    global running
    clock.config(bg='green')
    btn_start.config(state='disabled',background=defaultColour)
    btn_stop.config(state='normal',bg='dark red')
    btn_reset.config(state='disabled')
    running = True
def stop_btn():
    global running
    clock.config(bg='red')
    btn_start.config(state='normal',bg='green')
    btn_stop.config(state='disabled',bg=defaultColour)
    btn_reset.config(state='normal')
    running = False
def reset_btn():
    global prevSec, time1, secs, mins, hours, running
    clock.config(bg=defaultColour)
    hours = 0
    mins = 2
    secs = 0
    prevSec = ''
    time1 = ''
    running = False
    btn_stop.config(state='disabled',bg=defaultColour)
    btn_start.config(state='normal',bg='green')
    btn_reset.config(state='disabled')
def pause():
    global running
    clock.config(bg='red')
    btn_start.config(state='normal',bg='green')
    btn_stop.config(state='disabled',bg=defaultColour)
    btn_reset.config(state='normal')
    running = False
def reset():
    global prevSec, time1, secs, mins, hours, running
    clock.config(bg=defaultColour)
    hours = 0
    mins = 0
    secs = 30
    prevSec = ''
    time1 = ''
    running = False
    btn_stop.config(state='disabled',bg=defaultColour)
    btn_start.config(state='normal',bg='green')
    btn_reset.config(state='disabled')
def rndmp3 ():
   randomfile = random.choice(os.listdir("/home/pi/Music/Music"))
   file = '/home/pi/Music/Music/' + randomfile
   os.system ('omxplayer -o local ' + file)
   time.sleep(4)
 
btn_reset = Button(rootWindow, state='disabled', text = 'Reset', command = reset_btn)
btn_reset.grid(sticky=EW, row = 1, column = 3, padx = 5, pady = (5,2))
btn_start = Button(rootWindow, text = 'Start', bg='green', command = start_btn)
btn_start.grid(sticky=EW, row = 2, column = 3, padx = 5, pady = 2)
btn_stop = Button(rootWindow, state='disabled', text = 'Stop', command = stop_btn)
btn_stop.grid(sticky=EW, row = 3, column = 3, padx = 5, pady = (2,5))
btn_exit = Button(rootWindow, text = 'exit', command = exit)
btn_exit.grid(row = 4, column = 1, padx = 5, pady = 5)

rootWindow.mainloop()

