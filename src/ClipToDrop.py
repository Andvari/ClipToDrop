#!/usr/bin/env python
# -*- coding: UTF-8 -*-

'''
Created on Dec 7, 2012

@author: nemo
'''

import gtk
import pynotify
import os
from datetime import datetime

text = gtk.clipboard_get(gtk.gdk.SELECTION_CLIPBOARD).wait_for_text().encode('utf-8')

filename = "Clipboard.txt"

if (text.find("http:") == 0):
    filename = "Links.txt"

try:
    log = open(os.environ['HOME'] + "/Dropbox/" + filename , "a+")
    log.write(str(datetime.now()) + ":\n")
    log.write(gtk.clipboard_get(gtk.gdk.SELECTION_CLIPBOARD).wait_for_text().encode('utf-8'))
    log.write("\n---------------------------------------------------------------------------------------------------------\n\n")
    log.close()
    pynotify.init("Null")
    n = pynotify.Notification ("Clipboard saved", filename, "Null")
    n.show()
except:
    pynotify.init("Null")
    n = pynotify.Notification ("Clipboard not saved", "", "Null")
    n.show()
    
    
