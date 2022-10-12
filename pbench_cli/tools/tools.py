import click
from lib import tools

@click.command()
@click.argument("toolname")
def register(toolname):
    tools.tool_register(toolname)

@click.command()
def list():
    tools.tool_list()

@click.command()
def clean():
    tools.tool_clean()
