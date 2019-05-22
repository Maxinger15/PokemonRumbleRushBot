from PIL import Image

class ADBScreen:

    def __init__(self, device):
        self.device = device

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