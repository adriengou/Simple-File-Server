import json
import os

from flask import Flask, request
from config_loader import Config
from fileHandler import FileHandler

app = Flask(__name__)


@app.route('/download', methods=['GET'])
def download():

    target = request.args.get("target")
    path = request.args.get("path")
    print(target, path)
    fh = FileHandler(Config.files("download_path"), Config.files("upload_path"))


    if not target or not path:
        return "A parameter is missing."


    if target == "folder":
        r = fh.load_folder(path)

    elif target == "file":
        r = fh.load_file(path)

    else:
        return 'Worng "target" parameter.'


    return r or "Path is missing"


@app.route('/upload', methods=['POST'])
def upload():

    name = request.values['name']
    data = request.values['data']

    if name and data:
        fh = FileHandler(Config.files("download_path"), Config.files("upload_path"))
        fh.create_file(name, data)
        return "File created !"
    else:
        return "Parameters missing or wrong."


@app.route('/', methods=['GET', 'POST'])
def hello():
    return "Hello, world !"


if __name__ == "__main__":

    host = Config.server("host")
    port = Config.server("port")
    app.run(debug=True, host=host, port=port)
