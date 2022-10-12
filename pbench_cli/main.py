#!/usr/bin/python3

import click
from pbench_cli.results import results as results_cmd
from pbench_cli.tools import tools as tools_cmd

@click.group("cli")
def cli():
    print()
    pass

@cli.group()
def results():
    '''
    about results command
    '''
    pass

@cli.group()
def tools():
    '''
    about tools command
    '''
    pass

tools.add_command(tools_cmd.register)
tools.add_command(tools_cmd.list)
tools.add_command(tools_cmd.clean)

results.add_command(results_cmd.move)
results.add_command(results_cmd.copy)
results.add_command(results_cmd.clean)