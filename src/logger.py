from pathlib import Path

import click

from src.directories import Directory
from src.navigator import debug_solutions_absolute_path, list_files, \
    solutions_absolute_path


def source_files(ctx, args, incomplete):
    files = list_files(Directory.SOLUTIONS)
    return [file for file in files if incomplete in file]


def remove_log_comments(file: Path) -> str:
    with file.open() as f:
        lines = f.readlines()
        content = ''
        for line in lines:
            if '/*@log' in line or '*/' in line:
                line = ''
            elif '//@log' in line:
                line = line.replace('//@log ', '')
            content = content + line
    return content


def make_debug_file(filename: str):
    click.echo('Creating debuggable file.')
    file = Path(f'{solutions_absolute_path()}/{filename}')
    file_content = remove_log_comments(file)
    new_file = Path(f'{debug_solutions_absolute_path()}/{file.name}')
    new_file.touch()
    new_file.write_text(file_content)
    click.echo('File created.')