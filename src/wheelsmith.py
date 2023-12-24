#!/usr/bin/python3
import cursesplus
import curses
import sys

sys.path.insert("/usr/lib/wheelsmith")

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

curses.wrapper(main)