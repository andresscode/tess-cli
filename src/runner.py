import datetime
import os
import subprocess

import click

from src.directories import Directory
from src.navigator import list_files, cases_absolute_path, \
    build_absolute_path, solutions_absolute_path
from src.resources import runners_meta


def runnable_files(ctx, args, incomplete):
    meta = runners_meta()
    files = []
    files.extend(list_files(Directory.BUILD))
    for lang in meta['interpreted']:
        files.extend(list_files(Directory.SOLUTIONS, lang['extension']))
    return [file for file in files if incomplete in file]


def test_cases(ctx, args, incomplete):
    return [file for file in list_files(Directory.CASES) if incomplete in file]


def runner_meta(file):
    _, ext = os.path.splitext(file)
    if not ext:
        return None
    metadata = runners_meta()
    for lang in metadata['compiled']:
        if lang['extension'] == ext:
            tmp = lang
            tmp['type'] = 'compiled'
            return tmp
    for lang in metadata['interpreted']:
        if lang['extension'] == ext:
            tmp = lang
            tmp['type'] = 'interpreted'
            return tmp
    raise ValueError(f'Error running {file}')


def concat_cases_absolute_path(tests: list):
    root_dir = cases_absolute_path()
    t = []
    for test in tests:
        t.append(f'{root_dir}/{test}')
    return t


def resolve_test_content(tests: list):
    t = concat_cases_absolute_path(tests)
    content = []
    for test in t:
        with open(test, 'r') as file:
            content.append(file.read())
    return content


def run_timed_subprocess(_args, _input):
    start_time = datetime.datetime.now()
    output = subprocess.run(_args,
                            input=_input,
                            encoding='utf-8',
                            capture_output=True)
    end_time = datetime.datetime.now()
    time_taken = end_time - start_time
    millis = round(time_taken.total_seconds() * 1000, 2)
    return output, millis


def run_tests(args: list, tests: list):
    for test in tests:
        with open(test, 'r') as test_file:
            content = test_file.read().rstrip()
            click.echo(f'\n\nTest case: {os.path.basename(test)}')
            click.echo(content)
            output, millis = run_timed_subprocess(args, content)
            if output.stderr:
                click.echo(f'{output.stderr.strip()}')
            else:
                click.echo(
                    f'[Output] Time: {millis}ms\n{output.stdout.strip()}')


def concat_file_absolute_path(file, meta=None):
    if not meta or meta['type'] == 'compiled':
        return f'{build_absolute_path()}/{file}'
    else:
        return f'{solutions_absolute_path()}/{file}'


def resolve_file_name(file, meta=None):
    name, ext = os.path.splitext(file)
    if ext == '.class':
        return concat_file_absolute_path(name, meta)
    else:
        return concat_file_absolute_path(file, meta)


def runner_args(filename: str) -> list:
    meta = runner_meta(filename)
    if not meta:
        args = [f'{resolve_file_name(filename)}']
    else:
        filename = resolve_file_name(filename, meta)
        args = [f'{meta["runner"]}']
        if meta['runner'] == 'java':
            args.append('-cp')
            args.append(build_absolute_path())
            args.append(os.path.split(filename)[1])
        else:
            args.append(filename)
        if 'flags' in meta:
            args.extend(meta['flags'])
    return args


def run_solution(file, test):
    if test:
        tests = concat_cases_absolute_path([test])
    else:
        tests = concat_cases_absolute_path(list_files(Directory.CASES))
    args = runner_args(file)
    run_tests(args, tests)
