py -m build
copy dist\*.whl <FULL_PATH_TO_PYPI_WIN>\*.* /Y
rmdir /s /Q venv
py -m venv venv
venv\Scripts\activate