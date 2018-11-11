python3 setup.py sdist bdist_wheel

twine upload --repository-url https://test.pypi.org/legacy/ dist/*

rm -r build
rm -r dist
rm -r sunflower_low_level.egg-info
