
import pathlib


def get_json_base_path():
    return str(pathlib.Path(__file__).parent.absolute()) + "/urls.json"

def get_creds_path():
    return str(pathlib.Path(__file__).parent.absolute()) + "/creds.json"


    