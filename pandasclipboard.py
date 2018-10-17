import pandas as pd
import numpy as np
import pyautogui as p
import pyperclip as c
import os
import sys
##
def press(key,times):
    for i in range(0,times):
        p.press(key)



df = pd.read_csv("test.csv", encoding = "ISO-8859-1", dtype=object)
df.columns = df.columns.str.strip().str.replace(' ', '_').str.replace('(', '').str.replace(')', '')



for i, row in df.iterrows(): #iterate through each row with with row value and row content
    a = (row['Order'])
    c.copy(a)
    b = c.paste()
    p.click(75,753)
    p.PAUSE = 5
    p.typewrite('text')
    press('enter',3)
    p.typewrite('2')
    p.press('enter')
    p.typewrite('40')
    p.keyDown('shift') 
    press('f4',1)
    p.keyUp('shift')
    p.typewrite('text')
    press('enter',1)
    p.typewrite(b)
    press('enter',1)
    press('f8',1)
    press('f6',1)
    p.PAUSE = .1
    # now we will try and captue qty needed
    press('down',8)
    press('right',64)
    # works fine above, just cant figure out how to copy in values well

    p.keyDown('shift')
    p.press('c')
    p.keyUp('crl')
    b = c.paste()
    #print(b)
    

    #sys.exit()
    df.set_value(i, 'Test', b)
