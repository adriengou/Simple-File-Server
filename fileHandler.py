import os
import json
from pathlib import Path


class FileHandler:

    def __init__(self, dl_path, up_path):
        self.download_path = Path(dl_path)
        self.upload_path = Path(up_path)
        
        if not os.path.exists(self.download_path):
            os.mkdir(self.download_path)
        
        if not os.path.exists(self.upload_path):
            os.mkdir(self.upload_path)


    def load_file(self, file_path):
        path = self.download_path / Path(file_path)
        if path.is_file():

            with open(path, 'r')as file:
                data = file.read()
            
            return data
        
        else:

            return False


    def list_files(self, path):
        data = []
        if path.exists():

            if path.is_dir():
                
                for child in os.listdir(path):
                    data.append(*self.list_files(path / child))

            else:
                file_path = str(path).replace('\\', '/')
                file_path = file_path.replace("files/download/", '')
                data.append(file_path)
                

        return data


    def load_folder(self, dir_path):
        path = self.download_path / dir_path
        print(path)
        data = json.dumps(self.list_files(path), indent=4)
        
        if data:
            return data
        else:
            return False


    def create_file(self, name, data):
        
        path = self.upload_path
        
        if not path.is_dir():
            path.mkdir()
        
        with open(path / name, 'w') as file:
            file.write(data)



if __name__ == '__main__':
    fh = FileHandler('files/download', 'files/upload')
    #fh.create_file('', 'test.mp3', 'This is an upload test !')
    print(fh.list_files(Path("files/download/dossier_test")))
    
    

    