from ctypes import HRESULT
import tkinter as tk
import random
from unittest import result

window = tk.Tk()
 

window.geometry("600x400")

window.config(bg="#065569")
 
window.resizable(width=False,height=False)
 

window.title('Number Guessing Game')
 
 
TARGET = random.randint(0, 1000)
RETRIES = 0
 
 
def upate_result(text):
    result.configure(text=text)

def new_game():
    guess_button.config(state='normal')
    global TARGET, RETRIES
    TARGET = random.randint(0, 1000)
    RETRIES = 0
HRESULT(text="Guess a number between\n 1 and 1000")

def play_game():
    global RETRIES
 
    choice = int(number_form.get())
     
    if choice != TARGET:
        RETRIES += 1
     
        result = "Wrong Guess!! Try Again"
        if TARGET < choice:
            hint = "The required number lies between 0 and {}".format(result)
        else:
            hint = "The required number lies between {} and 1000".format(choice)
        result += "\n\nHINT :\n" + hint
     
    else:
        result = "You guessed the correct number after {} retries".format(RETRIES)
        guess_button.configure(state='disabled')
        result += "\n" + "Click on Play to start a new game"
        
