import os
import json


class Config:

    PATH = os.path.join(os.getcwd(), "config.json")
    with open(PATH) as file:
        configuration = json.load(file)

    @classmethod 
    def server(self, key):
        """Get server values from config.json"""
        return self.configuration['SERVER'][key]

    @classmethod
    def files(self, key):
        """Get files values from config.json"""
        return self.configuration['FILES'][key]

    