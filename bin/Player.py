from adb.client import Client as AdbClient
from time import sleep
import time
from PIL import Image
import pytesseract
import os
import configparser
from io import BytesIO

from bin.Settings import Settings
class Player:

    def __init__(self):
        client = AdbClient(host="127.0.0.1", port=5037)
        devices = client.devices()
        if len(devices) <= 0:
            raise ValueError("No device connected")
        self.device = client.device(str(devices[0].get_serial_no()))
        self.settings = Settings("config.cfg")
    def log(self, message):
        """

        :param message: String to print in de console
        :return: nothing
        """
        if self.settings.debug:
            print(str(message))


    def get_screen(self, device) -> Image:
        """
        Creates a screenshot on the device, copies the screenshot to the pc and opens it with PIL
        :param device: ADB-Device from pure-python-adb
        :return: PIL-Image
        """
        device.shell("screencap -p /sdcard/screen.png")
        device.pull("/sdcard/screen.png", "screen.png")
        screens = ""
        try:
            screens = Image.open('screen.png')
        except Exception:
            self.log("fehler beim laden")
            return -1
        return screens


    def check_string(self, device, string) -> bool:
        """
        Checks if a string is displayed on the screen of the device
        :param device: ADB-Device from pure-python-adb
        :param string: string to search on the display
        :return: boolean
        """
        screens = self.get_screen(device)
        while screens is -1:
            screens = self.get_screen(device)
            sleep(3.5*self.settings.speed_multi)
        area = (50, 840, 1078, 1918)
        lscreens = screens.crop(area)
        lscreens.save("lscreens.png")

        pytesseract.pytesseract.tesseract_cmd = self.settings.tesseract_dir
        erg = pytesseract.image_to_string(lscreens).lower()
        erg.rstrip("\n\r")
        erg.replace(" ", "")
        #self.log(erg.replace(" ", "")+" found by tesseract")
        if string.lower() in erg:
            # log("String: "+string+" ist in "+erg+" enthalten")
            return True
        else:
            # changes all whats not red into red and whats red to black. This
            # could be better recognized by tesseract
            # should help to improve the accuracy to detect that you have to many ores
            newimdata = []
            redcolor = (255, 10, 0, 255)
            blackcolor = (0, 0, 0, 255)
            for color in lscreens.getdata():
                if color[0] == 255 and color[0] == 255:
                    newimdata.append(blackcolor)
                else:
                    newimdata.append(redcolor)
            new = Image.new(lscreens.mode, lscreens.size)
            new.putdata(newimdata)
            erg = pytesseract.image_to_string(new).lower()
            if string.lower() in erg:
                #self.log("String: " + string + " ist in " + erg + " enthalten")
                return True
            else:
                return False


    def check_end_of_fight(self, device) -> bool:
        if self.check_string(device, self.settings.language_pack[0]):
            return True
        else:
            return False

    def grind(self):
        device = self.device
        # Abenteuerbutton
        self.log("    pressed adventure button")
        device.shell("input tap 550 1670")
        sleep(2.4*self.settings.speed_multi)
        # einen der drei buttons drücken
        self.log("    Select level")
        if self.settings.selected_raid == 1:
            device.shell("input tap 330 1150")
        elif self.settings.selected_raid == 2:
            device.shell("input tap 330 1312")
        else:
            device.shell("input tap 330 1463")
        sleep(1.2*self.settings.speed_multi)
        self.log("    Starting round")
        device.shell("input tap 559 1050")
        count = 0
        while not self.check_end_of_fight(device):
            self.log("      Fight not finished")
            if count == 8:
                # Führt jetzt den Special-Move aus
                self.log("    starting special move")
                device.shell("input tap 1000 1835")
            count = count + 1
            sleep(4*self.settings.speed_multi)
        self.log("    pressing forward buttons")
        foreward = True
        while self.check_string(device, self.settings.language_pack[0]) or foreward:
            self.log("    forward....")
            device.shell("input tap 559 1050")
            foreward = False
            sleep(0.5*self.settings.speed_multi)
        self.log("    finished forward buttons")
        if self.check_string(device,self.settings.language_pack[1]):
            self.log("  found finished button")
            device.shell("input tap 559 1050")

        sleep(4.8*self.settings.speed_multi)

        if self.check_string(device, self.settings.language_pack[2]):
            self.log("    to many ores")
            device.shell("input tap 835 1476")
            sleep(1.6*self.settings.speed_multi)
            device.shell("input tap 734 1067")
            sleep(2.5*self.settings.speed_multi)
            device.shell("input tap 560 1790")
            sleep(1*self.settings.speed_multi)
        self.log("  Finished")

    def start(self):
        #print(self.check_string(self.device,"dein"))
        for i in range(self.settings.rounds):
            self.log("Starting round " + str(i + 1))
            self.grind()
            sleep(2.5*self.settings.speed_multi)
