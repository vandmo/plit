import click
import sys


def msg(message):
    click.echo(click.style('plit:', fg='cyan') + ' ' + message)


def warn(message):
    click.echo(click.style('plit:', fg='yellow') + ' ' + message)


def errordie(message, code=-1):
    click.echo(click.style('plit:', fg='red') + ' ' + message, err=True)
    sys.exit(code)