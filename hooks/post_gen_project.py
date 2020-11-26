import os


if "{{ cookiecutter.git_init }}" == "y":
    os.system("git init")

if "{{ cookiecutter.poetry_install }}" == "y":
    os.system("poetry install")

if "{{ cookiecutter.pre_commit_install }}" == "y":
    os.system("pre-commit install")
