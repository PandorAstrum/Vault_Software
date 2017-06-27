# responsible to make a zip archive

import os
from zipfile import *


import shutil


class Make_presskit():
    def __init__(self, file_name):
        self.file_name = file_name
        self.main_content = []
        self.userhome = os.path.expanduser('~')
        self.desktop = self.userhome + "\\Desktop\\"
        self.CacheDir = os.getenv("LOCALAPPDATA") + "\\PandorAstrum\\Cache\\"
        self.imgDir = os.getenv("LOCALAPPDATA") + "\\PandorAstrum\\Image\\"
        self.screenshots = 0
        self.generatedPdf = "presskit.pdf"

    def make_presskit(self):
        outDir = os.path.join(self.desktop, self.file_name)
        zip_archive = ZipFile(outDir, 'w', ZIP_DEFLATED)
        for dirname, subdirs, files in os.walk(self.CacheDir):
            for filename in files:
                absname = os.path.abspath(self.CacheDir + filename)
                arcname = absname[len(self.CacheDir) + 0:]
                zip_archive.write(absname, arcname)
                os.remove(absname)
        ZipFile.close(zip_archive)

    def minimum_requirements(self):
        self.screenshots = 0

    def normal_requirements(self):
        self.screenshots = 3
    def full_requirements(self):
        self.screenshots = 5
    options = {"minimum" : minimum_requirements, "normal" : normal_requirements, "full" : full_requirements,}

    def Validate_presskit(self):

        # check for the items needed

            # depending on mode
        # if error then throw a message with link to go there in GUI
        # generate and copy everything to cache
        return False


