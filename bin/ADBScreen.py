from PIL import Image
import os
import shutil


class ADBScreen:

    def __init__(self, device):
        self.device = device
        self.screenfile = ""

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
        self.device.shell(str(command))

    def get_model_name(self):
        return self.device.shell("cat /system/build.prop | grep 'ro.product.model'")

    def create_model_template(self):
        dirname = os.path.dirname(__file__)
        name = self.get_model_name()
        new_file = os.path.join(dirname, '../conf/screens/' + str(name+".json"))
        new_file_dir = os.path.join(dirname, '../conf/screens/')
        if os.path.isfile(new_file):
            raise ValueError("The config already exists. Please delete the config if you want to make a new one")
        src_file = os.path.join(dirname, '../conf/screens/template/template.json')
        shutil.copy(src_file, new_file_dir)
        os.rename(os.path.join(new_file_dir,"template.json"), new_file)
        self.screenfile = new_file

    def fill_model_template(self):
        raise NotImplementedError("Currently not implemented")