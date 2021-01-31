import os
import setuptools

NAME = 'tax-pipeline'

py_name = NAME.replace('-', '_')

with open(f'{py_name}{os.sep}VERSION') as fh:
    VERSION = fh.readline().strip()

# rewrite __init__.py with __version__
with open(f'{py_name}{os.sep}__init__.py', 'w') as fh:
    fh.writelines(
        [
            '# this file gets overwritten by setup.py \n',
            f'__version__ = "{VERSION}" \n'
        ]
    )

with open(f"..{os.sep}README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name=NAME,
    version=VERSION,
    author="Dennis Mahle",
    author_email="dennis.mahle@gmail.com",
    description="Tax pipeline package",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/gitjonez/tax",
    packages=[py_name],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)