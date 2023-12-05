# Local GUI for cloud tool

import tkinter as tk
from tkinter import ttk
from tkinter import filedialog
from tkinter import messagebox
import os
import sys
import subprocess
import time
import threading
import queue
import re
import json
import logging


class AutomatorGUI(tk.Tk):
    def open_file(self):
        ## this function open a file dialog to select a file
        ## and return the file path
        self.file_path = filedialog.askopenfilename(
            initialdir=".",
            title="Select a file",
            filetypes=(("json files", "*.json"), ("all files", "*.*")),
        )
        if self.file_path:
            self.logger.info(f"open file: {self.file_path}")
            self.config_file_path.set(self.file_path)
            self.load_config()
        else:
            self.logger.info("no file selected")
            self.config_file_path.set("")

    def save_file(self):
        ## this function save the config to a file
        ## and return the file path
        self.file_path = filedialog.asksaveasfilename(
            initialdir=".",
            title="Save a file",
            filetypes=(("json files", "*.json"), ("all files", "*.*")),
        )
        if self.file_path:
            self.logger.info(f"save file: {self.file_path}")
            self.config_file_path.set(self.file_path)
            self.save_config()
        else:
            self.logger.info("no file selected")
            self.config_file_path.set("")

    def create_menu(self):
        ## this function creat menu bar and show
        ## file, edit, help
        self.menu_bar = tk.Menu(self)
        self.file_menu = tk.Menu(self.menu_bar, tearoff=0)
        self.file_menu.add_command(label="Open", command=self.open_file)
        self.file_menu.add_command(label="Save", command=self.save_file)

    ## this class create an windows with menu bar includes file, edit, help
    ## and a main frame to display the content

    def create_main_frame(self):
        self.main_frame = ttk.Frame(self)
        self.main_frame.pack(fill=tk.BOTH, expand=1)

    def create_status_bar(self):
        self.status_bar = ttk.Frame(self)
        self.status_bar.pack(fill=tk.X, side=tk.BOTTOM)
        self.config_file_path = tk.StringVar()
        self.config_file_path.set("")
        self.status_label = ttk.Label(
            self.status_bar, textvariable=self.config_file_path
        )
        self.status_label.pack(fill=tk.X, side=tk.LEFT)

    def create_logger(self):
        self.logger = logging.getLogger("automator")
        self.logger.setLevel(logging.DEBUG)
        self.logger.propagate = False
        self.logger.addHandler(logging.StreamHandler(sys.stdout))
        self.logger.addHandler(logging.StreamHandler(sys.stderr))

    def create_thread(self):
        self.thread = threading.Thread(target=self.run, daemon=True)
        self.thread.start()

    def create_queue(self):
        self.queue = queue.Queue()

    def create_config(self):
        self.config = {
            "sourceFolder": "",
            "targetFolder": "",
            "sourcePattern": "",
            "targetPattern": "",
            "mappingRule": "",
            "subs": False,
            "subsPattern": "",
        }

    def __init__(self):
        super().__init__()
        self.run = False
        self.title("Automator")
        self.geometry("800x600")
        self.resizable(0, 0)
        self.create_menu()

        self.create_main_frame()
        self.create_status_bar()
        self.create_logger()
        self.create_thread()
        self.create_queue()
        self.create_config()


def main():
    app = AutomatorGUI()
    app.mainloop()


if __name__ == "__main__":
    main()
