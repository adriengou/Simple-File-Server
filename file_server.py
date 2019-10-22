import json
import os

from flask import Flask, request, jsonify, send_file
from config_loader import Config
from pathlib import Path

app = Flask(__name__)

def file_tree(path):
    file_list = []
    for child in path.iterdir():

        if child.is_file():
            file_list.append(str(child))
        elif child.is_dir():
            file_list.extend(file_tree(child))
    
    return file_list
    

@app.route('/download', methods=['GET'])
def download():
    root = Path('files/download')
    path = root / Path(request.args.get("path"))
    print(root, path)

    if path.is_file():
        with open(path, 'r') as file:
            data = file.read()
    
        return data, 200, {'Content-Type': 'text/plain; charset=utf-8'}

        
    if path.is_dir():
        data = file_tree(path)
        return jsonify(data)

    else:
        return "No file or directory"
        
    
    


@app.route('/upload', methods=['POST'])
def upload():

    name = request.values['name']
    data = request.values['data']

    if name and data:
        path = Path( Config.files("download_path") )
        
        with open(path / name, 'w') as file:
            file.write(data)
    
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
