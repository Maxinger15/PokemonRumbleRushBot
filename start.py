from adb.client import Client as AdbClient
from time import sleep
import time
from PIL import Image
import pytesseract
import os
from io import BytesIO
local_path = os.path.dirname(os.path.abspath(__file__))+"\\tmp\\"
selected_raid = 1
debug = True
def log(message):
    if debug:
        print(str(message))

def check_string(device,string):

    screens = get_screen(device)
    while screens is -1:
        screens = get_screen(device)
        sleep(3.5)
    area = (50, 840, 1078, 1918)
    lscreens = screens.crop(area)
    lscreens.save("lscreens.png")

    pytesseract.pytesseract.tesseract_cmd = r'D:\tesseract_ocr\tesseract'
    erg = pytesseract.image_to_string(lscreens).lower()
    if string.lower() in erg:
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
            return True
        else:
            return False
#
# The Method with the Problem
#
#
def get_screen(device):
    device.shell("screencap -p /sdcard/screen.png")
    device.pull("/sdcard/screen.png", "screen.png")
    screens = ""
    try:
        screens = Image.open('screen.png')
    except Exception:
       log("fehler beim laden")
       return -1
    return screens


def check_end_of_fight(device):
    if check_string(device,"weiter"):
        return True
    else:
        return False


def grind():
    client = AdbClient(host="127.0.0.1", port=5037)
    devices = client.devices()
    device = client.device(str(devices[0].get_serial_no()))
    #Abenteuerbutton
    log("    pressed adventure button")
    device.shell("input tap 550 1670")
    sleep(2.4)
    #einen der drei buttons drücken
    log("    Select level")
    if selected_raid == 1:
        device.shell("input tap 330 1150")
    elif selected_raid == 2:
        device.shell("input tap 330 1312")
    else:
        device.shell("input tap 330 1463")
    sleep(1.2)
    log("    Starting round")
    device.shell("input tap 559 1050")
    count = 0
    while not check_end_of_fight:
        print("      Fight not finished")
        if count == 14:
            # Führt jetzt den Special-Move aus
            log("    starting special move")
            device.shell("input tap 1000 1835")
        count = count+1
        sleep(4)
    #1 mal muss immer gedrückt werden
    log("    pressing forward buttons")
    foreward = True
    while check_string(device,"weiter") or foreward:
        log("    forward....")
        device.shell("input tap 559 1050")
        foreward = False
        sleep(1.5)
    log("    finished forward buttons")
    if check_string(device,"fertig"):
        log("  found fertig button")
        device.shell("input tap 559 1050")

    sleep(5.5)

    if check_string(device,"dein"):
        log("    to many ores")
        device.shell("input tap 835 1476")
        sleep(2.5)
        device.shell("input tap 734 1067")
        sleep(2.5)
        device.shell("input tap 560 1790")
        sleep(1)
    log("  Finished")

for i in range(10):
    log("Starting round "+str(i+1))
    grind()
    sleep(2.5)


#To test the result of tesseract
#client = AdbClient(host="127.0.0.1", port=5037)
#devices = client.devices()
#device = client.device(str(devices[0].get_serial_no()))
#check_string(device,"dein")