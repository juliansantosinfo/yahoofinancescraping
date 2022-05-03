#! /bin/bash

pip install setuptools wheel twine

rm -rf dist build *.egg-info

python3 ./setup.py sdist
python3 ./setup.py bdist_wheel

twine upload -r testpypi dist/*