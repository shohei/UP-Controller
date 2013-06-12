#-*- coding:utf-8 -*-

from pywinauto import application
import autopy
from autopy import key
import time

app = application.Application.start("C:\Program Files\UP1.17\UP.exe")


def initUP():
    key.tap(key.K_ALT)
    key.tap(key.K_RIGHT)
    for x in range(5):
        key.tap(key.K_DOWN)
    key.tap(key.K_RETURN)
    
def maintainUP():
    key.tap(key.K_ALT)
    key.tap(key.K_RIGHT)
    for x in range(6):
        key.tap(key.K_DOWN)
    key.tap(key.K_RETURN)
    time.sleep(1)
    for x in range(8):
        key.tap('\t')
    key.type_string("130")
    time.sleep(1)
    key.tap('\t',key.MOD_SHIFT)
    time.sleep(1)
    key.tap(key.K_RETURN)

    #key.tap(key.K_TAB)
    #key.tap(key.K_TAB)

def openFile():
    key.tap('o', key.MOD_CONTROL)
    time.sleep(1)
    key.type_string("test.stl")
    key.type_string(string)
    key.tap(key.K_RETURN)

def startPrint():
    key.tap('p', key.MOD_CONTROL)



#initUP()
#maintainUP()
startPrint()


#top = app.top_window_
#app.MenuItem("File").click()
#mainwin = app.window_(title = 'UP!  V1.17  www.PP3DP.com')
#mainwin = app.window_(title_re = r'*www.PP3DP.com')
#print app.window_().Exists()
#mainwin = app.top_window_()
#app.TypeKeys("%FO")
#mainwin.TypeKeys("%FO")




