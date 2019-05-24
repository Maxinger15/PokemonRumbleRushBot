import configparser
from pathlib import Path
import json
import os
from bin.ADBScreen import ADBScreen
from adb.client import Client as AdbClient

class Settings:
    def __init__(self, ini_name):
        #Loading config.cfg
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
            self.autodetect_buttons = cparser.get("screen","autodeteckt_buttons")
        except Exception as e:
            raise ValueError("Couldn´t read config file")

        try:
            with open(os.path.join(dirname, '../conf/languages.json')) as json_file:
                data = json.load(json_file)
                self.language_pack = data[self.language]
        except Exception:
            raise ValueError("Language not found. Check your config file and update the languages.json")

        client = AdbClient(host="127.0.0.1", port=5037)
        devices = client.devices()
        if len(devices) <= 0:
            raise ValueError("No device connected")

        adbscreen = ADBScreen(client.device(str(devices[0].get_serial_no())))
        try:
            with open(os.path.join(dirname, '../conf/screens/'+str(adbscreen.get_model_name()+".json"))) as json_file:
                data = json.load(json_file)
                self.screen = data
        except Exception:
            raise ValueError("Screenconfig not found. Start the python script with the --init argument to create a config.")

        self.check_screen_values()

    def check_screen_values(self):
        for key, array in self.screen.items():
            errmsg = "Not all coordinates are set correctly in your screen config. The values have to be greater than zero. The error ocured at the field " + str(key)
            for nested in array:
                if isinstance(nested, int):
                    if int(nested) < 0:

                        raise ValueError(errmsg)
                else:
                    for nested2 in nested:
                        if int(nested2) < 0:
                            raise ValueError(errmsg)
