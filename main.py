from os import lseek

import click

from module.list_module import list_module

@click.group()
def cli():
    pass

@click.command()
def list():
    """- List all hide-my-email data"""
    list_module();

cli.add_command(list)
if __name__ == '__main__':
    cli();