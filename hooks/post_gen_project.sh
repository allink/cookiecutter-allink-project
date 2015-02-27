#! /usr/bin/env bash

git init
unzip {{cookiecutter.project_name}}/static/lib.zip -d {{cookiecutter.project_name}}/static
rm {{cookiecutter.project_name}}/static/lib.zip
git add --all
git commit -m "initial commit"
git checkout -b develop
