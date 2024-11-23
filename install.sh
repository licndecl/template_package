echo пересоздание виртуального окружения...
rm -R venv
python3.12 -m venv venv
source venv/bin/activate
pip install <FULL_PATH_TO_PYPI_LNX>/<PROJECT_NAME>-0.0.1-py3-none-any.whl --no-index --find-links=<FULL_PATH_TO_PYPI_LNX>