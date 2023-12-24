"""Enderbyte Programs App data Library"""

from platform import system as oss
import os
import json
WINDOWS = oss() == "Windows"

APP_NAME = ""
def register_app_name(name:str):
    global APP_NAME
    APP_NAME = name

class AppDataFile:
    def __init__(self,name="data"):
        if WINDOWS:
            self.folder = os.path.expandvars(f"%APPDATA%\\{APP_NAME}")
        else:
            self.folder = os.path.expanduser(f"~/.local/share/{APP_NAME}")
        self.path = self.folder + "/" + name + ".json"
        self.default = {}
        self.data = self.default
    def setdefault(self,data:dict):
        self.default = data
        self.data = self.default
    def load(self) -> dict:
        if not os.path.isfile(self.path):
            return self.default
        else:
            try:
                with open(self.path) as f:
                    d = f.read()
                rz = json.loads(d)
                self.data = rz
                return rz
            except:
                return self.default
    def update(self,data):
        self.data = data
        with open(self.path,"w+") as f:
            f.write(json.dumps(self.data))