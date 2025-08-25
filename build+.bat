py -m build
copy dist\*.whl <full_path_to_pypi_win>\*.* /Y
rmdir /s /Q venv
py -m venv venv
venv\Scripts\activate