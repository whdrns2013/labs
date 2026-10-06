from configparser import ConfigParser

def load_config(path:str):
    config = ConfigParser()
    config.read(path)
    return config

secret = load_config("config/secret.ini")
config = load_config("config/config.ini")