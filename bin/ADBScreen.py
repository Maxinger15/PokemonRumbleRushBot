from PIL import Image
import os
import shutil


class ADBScreen:

    def __init__(self, device):
        self.device = device
        self.screenfile = self.get_screenfile()

    def get_screen(self) -> Image:
        """
        Creates a screenshot on the device, copies the screenshot to the pc and opens it with PIL
        :param device: ADB-Device from pure-python-adb
        :return: PIL-Image
        """
        self.device.shell("screencap -p /sdcard/screen.png")
        self.device.pull("/sdcard/screen.png", "screen.png")
        screens = ""
        try:
            screens = Image.open('screen.png')
        except Exception:
            self.log("fehler beim laden")
            return -1
        return screens

    def shell(self, command):
        return self.device.shell(str(command))

    def get_screen_size(self):
        values = self.shell("dumpsys window displays | grep DisplayFrames")
        values = values.strip(" ")
        values = values.split(" ")

        size = [-1, -1]
        for string in values:
            if "w=" in string:
                size[0] = int(string.split("w=")[1])
            if "h=" in string:
                size[1] = (string.split("h=")[1])

        if -1 in size:
            print("Screen width can´t be detected. Please check the screen configuration and insert the values manually")
        return values


    def get_model_name(self):
        print()
        model = self.shell("getprop | grep 'ro.product.model'")
        model = model.split(":")
        model = model[1]
        model = model.strip(" ")
        model = model.strip('[')
        model = model.rstrip()
        model = model.strip("]")
        model = model.replace(" ", "_")

        return model
    def get_screenfile(self):
        dirname = os.path.dirname(__file__)
        name = self.get_model_name()
        return os.path.join(dirname, '../conf/screens/' + str(name + ".json"))


    def create_model_template(self):
        new_file = self.get_screenfile()
        dirname = os.path.dirname(__file__)
        new_file_dir = os.path.join(dirname, '../conf/screens/')
        if os.path.isfile(new_file):
            #raise ValueError("The config already exists. Please delete the config if you want to make a new one")
            print("The config already exists. Please delete the config if you want to make a new one")
        else:
            src_file = os.path.join(dirname, '../conf/screens/template/template.json')
            shutil.copy(src_file, new_file_dir)
            os.rename(os.path.join(new_file_dir, "template.json"), new_file)

    def fill_model_template(self):
        raise NotImplementedError("Currently not implemented")