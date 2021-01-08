from os import walk

import src.resources as res
from src.directories import Directory
from src.navigator import make_dirs, make_files


def make_template(path, lang, empty):
    for _, dirs, _ in walk(path):
        if '.tess' in dirs:
            raise SystemError('tess project initialized, already.')
    dirs = make_dirs(path)
    if empty:
        make_files(path, res.generator_template('empty.py'))
    else:
        make_files(path, res.generator_template('sum_template.py'))
        make_files(dirs[Directory.CASES], res.test_case_templates())
        make_files(dirs[Directory.SOLUTIONS], res.lang_templates(lang))
