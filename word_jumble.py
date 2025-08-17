# -*- coding: utf-8 -*-
"""
Created on Sat Aug 16 14:47:37 2025

@author: gudiy
"""
import random
import time

def choose():
    word = [
    "apple", "table", "chair", "water", "school",
    "flower", "money", "river", "phone", "train",
    "garden", "market", "travel", "yellow", "mother",
    "doctor", "planet", "window", "animal", "silver",
    "elephant", "triangle", "hospital", "democracy", "computer",
    "language", "vacation", "mountain", "football", "director",
    "psychology", "literature", "astronomy", "experiment", "motivation",
    "dictionary", "electricity", "independence", "environment", "agriculture"]
   # word=['rainbow','math','science','pragramming','player','reverese','water','board']
    pick=random.choice(word)
    return pick

def jumble(word):
    jumbled= "".join(random.sample(word,len(word)))
    return jumbled

def thank(p1,p2,p1s,p2s):
    print(f"\nPlayer 1, Score is {p1s}.")
    print(f"Plyaer 2, Score is {p2s}.")
    if p1s > p2s:
        print(f"\n Winner is {p1} with {p1s} points!")
    elif p2s > p1s:
        print(f"\n Winner is {p2} with {p2s} points!")
    else:
        print("\n It's a Tie!")

    print("\nThanks for Playing this game.")
    print("Have a nice day.")
    
    


def play():
    print("\n Welcome to Word Jumble Game ")
    p1=input("Enter Player 1 Name= ")
    p2=input("Enter Player 2 Name= ")
    
    p1s=0
    p2s=0
    turn=0
    
    
    print("====================================")
    print(f"Player 1: {p1}  |  Player 2: {p2}")
    print("====================================\n")

    
    while(1):
        pick_word=choose()
        qn=jumble(pick_word)
        print(qn)
        
        if turn%2==0:
            print(p1,"Your turn's...")
            ans=input("Whats your Answer= ")
            
            if ans==pick_word:
                p1s+=1
                print(f"Your Score is {p1s}")
                
            else:
                print("Better Luck next time. I thought: ", pick_word)
            
            c=int(input("Press 1 to Continue and 0 to Quit= "))
            if c==0:
                thank(p1,p2,p1s,p2s)
                time.sleep(6)
                break
        
        else:
            print(p2,"Your turn's...")
            ans=input("Whats your Answer= ")
            
            if ans==pick_word:
                p2s+=1
                print(f"Your Score is {p2s}")
            
            else:
                print("Better Luck next time. I thought: ", pick_word)
                
            c=int(input("Press 1 to Continue and 0 to Quit= "))
            if c==0:
                thank(p1,p2,p1s,p2s)
                time.sleep(6)
                break
        
        turn+=1

play()
                