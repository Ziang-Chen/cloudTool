from src.path import path
import shutil
from src.setting import *
import os


class file:
    def __init__(self, raw_address: str):
        self.raw_address = raw_address
        self.path = path(raw_address)

    def deliver(self, p: path):
        if IS_DEBUG:
            print("copy from {:} to {:}".format(self.raw_address, p.get_raw()))
        else:
            shutil.copy(self.raw_address, p.get_raw())

    def rename(self, new_name):
        source_file_name = self.path.p.name
        os.rename(source_file_name, new_name)


class folder:
    def __init__(self, raw_address: str):
        self.raw_address = raw_address
        self.path = path(raw_address)
        self.subs = self.path.iterator_on_same_level()

    def deliver(self, p: path):
        for s in self.subs:
            if IS_DEBUG:
                print(str(self.path.p / s))
            else:
                shutil.copy(str(self.path.p / s), p.get_raw())

    def rename(self, new_name):
        source_file_name = self.path.p.name
        os.rename(source_file_name, new_name)
