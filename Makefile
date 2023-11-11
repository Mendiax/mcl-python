test:
	python3 -m unittest discover

publish:
	python3 setup.py sdist bdist_wheel --universal
	python3 -m twine upload --repository-url https://upload.pypi.org/legacy/ dist/*

update_local:
	pip install --upgrade .

install_local:
	pip install .

format:
	black .

coverage:
	coverage run -m unittest discover
	coverage report -m
	coverage html