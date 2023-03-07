#Write a Python program to count the number of lines in a text file.
import os

path = 'tsis5/row.txt'
with open( path , 'r', encoding='UTF8') as f:
    lines = f.readlines()
    print( len(lines) )