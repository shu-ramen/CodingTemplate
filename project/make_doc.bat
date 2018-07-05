sphinx-apidoc -f -o docs/apis project
sphinx-build -b html docs/ docs/_build
cd docs
make html
cd ..