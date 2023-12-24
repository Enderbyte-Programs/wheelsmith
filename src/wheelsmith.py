#!/usr/bin/python3
import cursesplus
import curses
import sys

sys.path.insert(0,"/usr/lib/wheelsmith")

import epappdata

defaultappdata = {
    "settings" : {
        
    },
    "setup" : False
}

APPDATA: epappdata.AppDataFile

def main(stdscr):
    global APPDATA
    epappdata.register_app_name("wheelsmith")
    APPDATA = epappdata.AppDataFile()
    APPDATA.setdefault(defaultappdata)
    APPDATA.load()
    if not APPDATA["setup"]:
        cursesplus.messagebox.showinfo(stdscr,["Welcome to wheelsmith.","We have some setup to do"],"Welcome")
        APPDATA["setup"] = True
    APPDATA.write()

curses.wrapper(main)