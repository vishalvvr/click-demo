import click
from lib import results

@click.command()
def move():
    results.results_move()

@click.command()
def copy():
    results.results_copy()

@click.command()
def clean():
    results.results_clean()

