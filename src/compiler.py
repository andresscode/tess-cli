import json
import os
import subprocess

import click
from pkg_resources import resource_string

from src.directories import Directory
from src.navigator import find_root_directory


def get_source_files(root_dir):
    source_files = []
    for _, _, filenames in os.walk(f'{root_dir}/{Directory.SOLUTIONS}'):
        source_files.extend(filenames)
        break
    return source_files


def load_dict(pkg, file):
    return json.loads(resource_string(pkg, file).decode('utf-8'))


def get_files_to_compile(files, meta):
    to_compile = {}
    for key, lang in meta.items():
        to_compile[key] = []
        for file in files:
            if os.path.splitext(file)[1] in lang['extensions']:
                to_compile[key].append(file)
    return to_compile


def compile_cpp_files(files, meta, root_dir):
    for file in files:
        click.echo(f'Compiling {file}')
        args = [
            meta['compiler'],
            '-o', f'{root_dir}/{Directory.BUILD}/{os.path.splitext(file)[0]}',
            f'{root_dir}/{Directory.SOLUTIONS}/{file}']
        args.extend(meta['flags'])
        subprocess.run(args)


def compile_java_files(files, meta, root_dir):
    for file in files:
        click.echo(f'Compiling {file}')
        args = [meta['compiler'],
                f'{root_dir}/{Directory.SOLUTIONS}/{file}', '-d',
                f'{root_dir}/{Directory.BUILD}']
        args.extend(meta['flags'])
        subprocess.run(args)


def compile_files(files, meta, root_dir):
    for key, value in files.items():
        if key == 'cpp':
            compile_cpp_files(value, meta[key], root_dir)
        elif key == 'java':
            compile_java_files(value, meta[key], root_dir)
        else:
            raise KeyError(f'Programming language not supported <{key}>')


def get_compilable_files(cwd):
    root_dir = find_root_directory(cwd)
    source_files = get_source_files(root_dir)
    compilers_meta = load_dict('templates.config', 'compilers.json')
    return get_files_to_compile(source_files, compilers_meta)


def compilable_files(ctx, args, incomplete):
    to_compile = []
    for _, files in get_compilable_files(os.getcwd()).items():
        to_compile.extend(files)
    return [file for file in to_compile if incomplete in file]


def compile_cmd(file):
    root_dir = find_root_directory(os.getcwd())
    source_files = get_source_files(root_dir)
    compilers_meta = load_dict('resources.config', 'compilers.json')
    to_compile = get_files_to_compile(source_files, compilers_meta)
    if file:
        _, ext = os.path.splitext(file)
        to_compile = {ext[1:]: [file]}
    compile_files(to_compile, compilers_meta, root_dir)