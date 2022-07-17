import requests
import click

from module.common.common_config import get_creds_path
from module.helpers.json import read_file

# Proxyman Code Generator (1.0.0): Python + Request
# GET https://p42-maildomainws.icloud.com/v1/hme/list

def post_data_with_bearer(path, data):
    try:
        response = requests.get(url=path,headers=get_header_auth(),data=data)

        if 'reason' in response.json():
            if (response.json()["reason"] == 'Invalid global session'):
                click.echo("Cookie is expired")
                return None

        return response.json()
    except requests.exceptions.RequestException:
        click.echo('HTTP Request failed')


def get_header_auth():
    return {
        "Origin": "https://www.icloud.com",    
        "Cookie": get_cookie()
    }

def get_cookie():
    return read_file(get_creds_path())["Cookie"]
    
