# -*- coding: utf-8 -*-
import click
from screen_commander.screen_commander import ScreenCommander


@click.group()
def screen_commander():
    """screen_commander command line utility."""
    pass


@screen_commander.command()
@click.argument('filename')
def run(filename):
    """run

        \b
        Runs a deployment read from a YAML file
        """

    sc = ScreenCommander()
    sc.run(filename)


@screen_commander.command()
@click.argument('filename')
def kill(filename):
    """kill

        \b
        Kills  a deployment  as named in a YAML file
        """

    sc = ScreenCommander()
    sc.kill(filename)
