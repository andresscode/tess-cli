import os

import click

from src.compiler import compile_cmd, compilable_files
from src.initializer import make_template
from src.logger import make_debug_file, source_files
from src.runner import runnable_files, test_cases, run_solution
from src.scripts import make_completion_script
from src.stresser import run_stress


@click.group()
def cli():
    pass


@click.command('auto-complete')
@click.option('-s', '--shell', default='bash',
              type=click.Choice(['bash', 'zsh', 'fish'], case_sensitive=False),
              help='Target shell.')
@click.argument('destination', type=click.Path(exists=True))
def auto_complete(shell, destination):
    """Creates a script to enable tess commands auto-completion."""
    try:
        script = make_completion_script(shell, destination)
        click.echo(f'Script created at: {script}')
    except (NotADirectoryError, ValueError) as err:
        click.echo(err)


@click.command('init')
@click.option('-l', '--lang', default='py',
              type=click.Choice(['py', 'cpp', 'java'], case_sensitive=False),
              help='Preferred programming language.')
@click.option('-e', '--empty', is_flag=True,
              help='Creates an empty project.')
def init(lang, empty):
    """Creates a new tess project within the actual directory."""
    try:
        make_template(os.getcwd(), lang, empty)
        click.echo('Project initialized correctly.')
    except SystemError as err:
        click.echo(err)


@click.command('build')
@click.argument('file', required=False,
                type=click.STRING, autocompletion=compilable_files)
def build(file):
    """Compiles source code files."""
    try:
        compile_cmd(file)
        if file:
            click.echo('File compiled successfully.')
        else:
            click.echo('All files compiled successfully.')
    except FileNotFoundError as err:
        click.echo(err)


@click.command('run')
@click.argument('file', required=True,
                type=click.STRING, autocompletion=runnable_files)
@click.argument('test', required=False,
                type=click.STRING, autocompletion=test_cases)
def run(file, test):
    """Tests an algorithm using pre-defined test cases."""
    run_solution(file, test)


@click.command('stress')
@click.argument('model', required=True,
                type=click.STRING, autocompletion=runnable_files)
@click.argument('solution', required=True,
                type=click.STRING, autocompletion=runnable_files)
@click.option('-s', '--seed', default=1,
              help='Seed used by the random number generator.')
@click.option('-n', '--number', default=-1,
              help='How many test cases to execute.')
@click.option('-a', '--args',
              prompt='Arguments (separated by spaces)',
              help='Arguments required by the generator.')
@click.option('-l', '--line', default=0,
              help='Selects line <l> to be compared.')
def stress(model, solution, seed, number, args, line):
    """Compares two algorithms using auto-generated test cases."""
    run_stress(model, solution, seed, number, args.split(), line)


@click.command('debug')
@click.argument('file', required=True,
                type=click.STRING, autocompletion=source_files)
def debug(file):
    make_debug_file(file)


cli.add_command(auto_complete)
cli.add_command(init)
cli.add_command(build)
cli.add_command(run)
cli.add_command(stress)
cli.add_command(debug)


def main():
    cli()
