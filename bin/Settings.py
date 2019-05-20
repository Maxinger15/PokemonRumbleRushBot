import configparser
from pathlib import Path
import json
import os
class Settings:
    def __init__(self, ini_name):
        cparser = configparser.ConfigParser()
        dirname = os.path.dirname(__file__)
        ini_file = Path(os.path.join(dirname, "..\conf\\"+ini_name))

        if ini_file.is_file():
            cparser.read(ini_file)
        else:
            raise ValueError("Config file name not valid")
        self.language = "DE"
        #loads the config information
        try:
            self.language = cparser.get("custom", "language")
            self.speed_multi = cparser.getfloat("custom", "speed_multi")
            self.selected_raid = cparser.get("custom", "selected_raid")
            self.tesseract_dir = cparser.get("custom", "tesseract_directory")
            self.rounds = cparser.getint("custom", "rounds")
            self.debug = cparser.getboolean("custom", "debug")
        except Exception as e:
            raise ValueError("Couldn´t read config file")

        try:
            with open(os.path.join(dirname, '../conf/languages.json')) as json_file:
                data = json.load(json_file)
                self.language_pack = data[self.language]
        except Exception:
            raise ValueError("Language not found. check your config file and update the languages.json")

