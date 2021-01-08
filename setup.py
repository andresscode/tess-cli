import setuptools

with open('README.md', 'r', encoding='utf-8') as f:
    long_description = f.read()

setuptools.setup(
    name='tess-username',
    version='0.0.1',
    author='Andres Martinez',
    author_email='andressbox90@gmail.com',
    description='Stress testing CLI tool.',
    long_description=long_description,
    long_description_content_type='text/markdown',
    url='https://github.com',
    packages=setuptools.find_packages(),
    package_data={
        'templates': ['*.json', '*.cpp', '*.java', '*.py', '*.txt'],
    },
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.7',
    install_requires=[
        'Click',
    ],
    entry_points='''
        [console_scripts]
        tess=src.cli:main
    '''
)
