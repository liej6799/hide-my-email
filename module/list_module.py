import datetime
from email.utils import parsedate_to_datetime
import click
import pandas as pd
import time


from tabulate import tabulate
from module.common.common_config import get_json_base_path
from module.helpers.json import read_file
from module.helpers.network import post_data_with_bearer


url_list = read_file(get_json_base_path())["URL_LIST"]


def list_module():

    result = post_data_with_bearer(url_list, None)
    if result is not None:
        if 'success' in result:      
            df = pd.DataFrame(result["result"]["hmeEmails"])
            
            df.createTimestamp = df.createTimestamp.apply(lambda d: datetime.datetime.fromtimestamp(d/1000))

            click.echo(tabulate(df[['label', 'hme', 'createTimestamp']], headers=['Label', 'Hide My Email', 'Timestamp'], tablefmt='psql'))
                