from flask import Flask, render_template, url_for, send_file
from flask import request
import asyncio
from asgiref.wsgi import WsgiToAsgi
import os
import sys

app = Flask(__name__)


# url_for("static", filename="style.css")
# url_for("static", filename="index.html")


@app.route("/")
def index():
    return send_file("index.html")


@app.route("/style.css")
def style():
    return send_file("style.css")


@app.route("/ui.js")
def ui():
    return send_file("ui.js")


@app.route("/run", methods=["POST"])
def run():
    if request.method == "POST":
        # print(request.form["command"])
        cmd = request.get_json()["command"]
        os.system("python3 automator.py " + cmd + "> output.txt")
        with open("output.txt", "r") as f:
            r = ""
            for line in f:
                r += '<p class="infomationText"> ' + line + "</p>"
            return r


@app.route("/information", methods=["POST"])
def information():
    if request.method == "POST":
        # print(request.form["command"])
        print(request.get_json()["content"])
        return "ok"


@app.route("/filelist")
def file_list():
    os.system("ls > file_list.txt")
    with open("file_list.txt", "r") as f:
        r = ""
        for line in f:
            r += "<p> " + line + "</p>"
        return r


@app.route("/async_test")
async def async_test():
    print("async_test")
    await asyncio.sleep(1)
    return "async_test_return"


@app.route("/async_test_2")
async def async_test_2():
    print("async_test")
    await asyncio.sleep(1)
    return "async_test_return"


@app.route("/async_test_3")
async def async_test_3():
    print("async_test")
    await asyncio.sleep(1)
    return "async_test_return"
