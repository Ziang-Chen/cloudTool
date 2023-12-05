

import pathlib
import os
import sys


def platform():
    platforms = {
        "linux1": "Linux",
        "linux2": "Linux",
        "darwin": "Mac Os",
        "win32": "Windows",
    }
    if sys.platform not in platforms:
        return sys.platform
    return platforms[sys.platform]


class path:
    """
    Path object [file/folder]
    """

    def __init__(self, rawstr="./"):
        self.sysname = platform()

        ## TDB: select method according to the OS

        self.p = pathlib.Path(rawstr)

    def add_sub(self, sub):
        """
        add sub path
        """
        self.p = self.p / sub

    def get_raw(self):
        """
        get raw path
        """
        return str(self.p)

    def get_latest_folder(self):
        return self.p.parents[0]

    def iterator_on_same_level(self, pattern="*"):
        return self.p.glob(pattern)
