# -*- coding: utf-8 -*-
"""
Created on Sat Oct  8 10:12:50 2022

@author: HP
"""

import numpy
board=numpy.array([['-','-','-'],['-','-','-'],['-','-','-']])
pl1='X'
pl2='O'

def check_rows(symbol):
    for r in range(3):
        count=0
        for c in range(3):
            if board[r][c]==symbol:
                count=count+1
        if(count==3):
            print(symbol, " won")
            return True
    return False

def check_col(symbol):
    for c in range(3):
        count=0
        for r in range(3):
            if board[r][c]==symbol:
                count=count+1
        if(count==3):
            print(symbol, " won")
            return True
    return False

def check_diagonal(symbol):
    if(board[0][2]==board[1][1] and board[1][1]==board[2][0] and board[2][0]==board[0][2]):
        print(symbol, " won")
        return True
    if(board[0][0]==board[1][1] and board[1][1]==board[2][2] and board[2][2]==board[0][0]):
        print(symbol, " won")
        return True
    return False
    

def won(symbol):
    
    return  check_rows(symbol) or check_col(symbol) or check_diagonal(symbol)

def place(symbol):
    print(numpy.matrix(board))
    while(1):
        row=int(input("Enter row position - 1 , 2 or 3: "))
        col=int(input("Enter column position - 1 , 2 or 3: "))
        if(row>0 and row<4 and col>0 and col<4 and board[row-1][col-1]=='-'):
            break
        else:
            print("Invalid input please enter again")
    board[row-1][col-1]=symbol
    
  

def play():
    for turn in range(9):
        if(turn%2==0):
            print("X turn")
            place(pl1)
            if won(pl1):
                break
        else:
            print("O turn")
            place(pl2)
            if won(pl2):
                break
    if(not(won(pl1)) and not(won(pl2))):
        print("Draw")
        

play()
    