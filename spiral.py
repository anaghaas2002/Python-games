# -*- coding: utf-8 -*-
"""
Created on Sat Oct  8 18:26:34 2022

@author: HP
"""
import random
import turtle
turtle.bgcolor("black")
anagha=turtle.Turtle()

width=5
height=7

dot_distance=25

anagha.setpos(-250,250)

anagha.penup()
list_color=["white","yellow","orange","red","blue","pink"]


def spiral(m,n):
    k=0  #index of starting row
    l=0  #index of starting column
    f=0
    col=random.randint(0,5)
    anagha.color(list_color[col])
    

    while(k<m and l<n):
        #printing first row from remaining rows
        
        if(f==1):
           
            anagha.right(90)
        
        for i in range(l,n):
            #print(a[k][i],end=" ")
            anagha.dot()
            anagha.forward(dot_distance)
        k=k+1
        f=1
        
        anagha.right(90)
        col=random.randint(0,5)
        anagha.color(list_color[col])
        #printing last column
        for i in range(k,m):
            anagha.dot()
            anagha.forward(dot_distance)
            #print(a[i][n-1],end=" ")
        n=n-1
        #printing last row from remaining rows
        anagha.right(90)
        col=random.randint(0,5)
        anagha.color(list_color[col])
        if(k<m):
            for i in range(n-1,l-1,-1):
                anagha.dot()
                anagha.forward(dot_distance)
                #print(a[m-1][i],end=" ")
            m=m-1
        anagha.right(90)
        col=random.randint(0,5)
        anagha.color(list_color[col])
        if(l<n):
            #printing the first col from the remaining col
            for i in range(m-1,k-1,-1):
                anagha.dot()
                anagha.forward(dot_distance)
                #print(a[i][l],end=" ")
            l=l+1

spiral(10,10)
turtle.done()
        

