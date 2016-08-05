#!/usr/bin/python

import time
import gtk.gdk
import pynotify
today = time.strftime("%d/%m/%y")



def check_for_event():
    file = open("/root/events.txt")
    for line in file:
        if today in line:
            notify(line)
    file.close()

def notify(arg):
    pynotify.init("Basic")
    n = pynotify.Notification("Remind me : "+arg)
    #n.set_hint('x', gtk.gdk.screen_width()/10.)
    #n.set_hint('y', gtk.gdk.screen_height()/10.)
    n.show()

check_for_event()