from adb.client import Client as AdbClient
from bin.ADBScreen import ADBScreen
from time import sleep
import time
from PIL import Image
import pytesseract
import os
import configparser
from io import BytesIO

from bin.Settings import Settings
class Player:

    def __init__(self, init=False):
        client = AdbClient(host="127.0.0.1", port=5037)
        devices = client.devices()
        if len(devices) <= 0:
            raise ValueError("No device connected")
        self.device = client.device(str(devices[0].get_serial_no()))
        self.settings = Settings("config.cfg", init=init)
        self.adbscreen = ADBScreen(self.device)
    def log(self, message):
        """

        :param message: String to print in de console
        :return: nothing
        """
        if self.settings.debug:
            print(str(message))

    def get_coordinates(self, jsonname, layers=1, selected_layer= 0):
        if layers == 1:
            return str(self.settings.screen[jsonname][0])+" "+str(self.settings.screen[jsonname][1])
        else:                                 #row       pos 1 array    pos 2 array in 1 array
            return str(self.settings.screen[jsonname][selected_layer][0])+" "+str(self.settings.screen[jsonname][selected_layer][1])


    def check_string(self, string) -> bool:
        """
        Checks if a string is displayed on the screen of the device
        :param device: ADB-Device from pure-python-adb
        :param string: string to search on the display
        :return: boolean
        """
        screens = self.adbscreen.get_screen()
        while screens is -1:
            screens = self.adbscreen.get_screen()
            sleep(3.5*self.settings.speed_multi)
        area = (50, 840, 1078, 1918)
        # currently removed because of an size issue
        #lscreens = screens.crop(area)
        #lscreens.save("lscreens.png")
        lscreens = screens
        pytesseract.pytesseract.tesseract_cmd = self.settings.tesseract_dir
        erg = pytesseract.image_to_string(lscreens).lower()
        #erg = erg.rstrip("\n\r")
        #erg = erg.replace(" ", "")
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
            whitecolor = (255, 255, 255, 255)
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
                # changes all whats not red into red and whats white to black. This
                # could be better recognized by tesseract
                # should help to improve the accuracy to detect the skip buttons
                newimdata = []
                for color in lscreens.getdata():
                    if color[0] == 255 and color[1] == 255 and color[2] == 255:
                        newimdata.append(blackcolor)
                    else:
                        newimdata.append(whitecolor)
                new = Image.new(lscreens.mode, lscreens.size)
                new.putdata(newimdata)
                erg = pytesseract.image_to_string(new).lower()
                if string.lower() in erg:
                    # self.log("String: " + string + " ist in " + erg + " enthalten")
                    return True
                else:
                    return False


    def check_end_of_fight(self, device) -> bool:
        if self.check_string(self.settings.language_pack[0]):
            return True
        else:
            return False

    def grind(self):
        adbscreen = self.adbscreen
        # Tap the adventure button in the Main menue
        self.log("    pressed adventure button")
        adbscreen.shell("input tap "+self.get_coordinates("adventurebutton"))
        sleep(3.2*self.settings.speed_multi)
        # Tap one of the three raids
        self.log("    Select level")
        if self.settings.selected_raid == "1":
            adbscreen.shell("input tap "+self.get_coordinates("select_raids", layers=3, selected_layer=0))
        elif self.settings.selected_raid == "2":
            adbscreen.shell("input tap "+self.get_coordinates("select_raids", layers=3, selected_layer=1))
        else:
            adbscreen.shell("input tap "+self.get_coordinates("select_raids", layers=3, selected_layer=2))
        sleep(1.8*self.settings.speed_multi)
        self.log("    Starting round")
        #Tap the start button
        adbscreen.shell("input tap "+self.get_coordinates("startbutton"))
        count = 0
        #This loop runs till the fight is finished
        while not self.check_end_of_fight(adbscreen):
            self.log("      Fight not finished")
            if count == 8:
                # Start the special attack
                self.log("    starting special move")
                adbscreen.shell("input tap "+self.get_coordinates("specialmovebtn"))
            count = count + 1
            sleep(2.5*self.settings.speed_multi)
        self.log("    pressing forward buttons")

        """
        foreward = True
        #This loop runs while there are items displayed after the match
        while self.check_string( self.settings.language_pack[0]) or foreward:
            self.log("    forward....")
            # Tap the result screen to continue
            adbscreen.shell("input tap "+self.get_coordinates("nextbutton"))
            foreward = False
            sleep(0.6*self.settings.speed_multi)
        self.log("    finished forward buttons")
        # This skips the last resultscreen
        if self.check_string(self.settings.language_pack[1]):
            self.log("  found finished button")
            #Tap the last result screen to continue
            adbscreen.shell("input tap "+self.get_coordinates("donebutton"))
        """
        for i in range(0, self.settings.taps_resultscreen):
            adbscreen.shell("input tap " + self.get_coordinates("nextbutton"))
            sleep(0.6)
        sleep(4.9*self.settings.speed_multi)

        #Looks if you have to many ores. If you have to many ores it deletes the new ore.
        if self.check_string(self.settings.language_pack[2]):
            self.log("    to many ores")
            #Tap the delete button
            adbscreen.shell("input tap "+self.get_coordinates("ore_trashcanbutton"))
            sleep(2*self.settings.speed_multi)
            #Tap the yes button
            adbscreen.shell("input tap "+self.get_coordinates("ore_yesbutton"))
            sleep(3.9*self.settings.speed_multi)
            #Tap the quit button to go to main menue
            adbscreen.shell("input tap "+self.get_coordinates("ore_quitbutton"))
        else:
            # Tap the quit button to go to main menue
            adbscreen.shell("input tap " + self.get_coordinates("ore_quitbutton"))

        if(self.check_string(self.settings.language_pack[3])):
            print("No ore in factory")
            sleep(0.7 * self.settings.speed_multi)
            # Presses the button on the infomessage if no ore is currently going to be refined
            adbscreen.shell("input tap "+self.get_coordinates("ore_acceptNoOre"))
        sleep(1.1 * self.settings.speed_multi)

        self.log("  Finished")

    def start(self):
        #print(self.check_string("dein")
        for i in range(self.settings.rounds):
            self.log("Starting round " + str(i + 1))
            self.grind()
            sleep(2.5*self.settings.speed_multi)

    def init(self):
        self.adbscreen.create_model_template()

        #Not implemented
        #self.adbscreen.fill_model_template()