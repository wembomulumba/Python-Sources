#! /usr/bin/env python3

import random

number = random.randint(1, 10)
tries = 1

uname = input("Hello , What is your username ? ")
print("Hello ",  uname + ".", )

question = input("Would you like to play a game ? [Y/N]")

if question == "n":
    print("oh..okay")
if question == "y":
    print("I'm thinking og a number between 1 & 10")
    guess = int(input("Have a guest:"))
if guess > number:
        print("Guess lower...")
if guess < number :
    print("Guess higher..")
while guess != number :
    tries += 1
    guess  = int(input("Try again: ")) 
    if guess < number :
        print("guess number")   
if guess == number :
    print("the number you have chosen is right !", number,"and it only ", tries, "tries!")
