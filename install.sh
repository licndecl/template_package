echo пересоздание виртуального окружения...
rm -R -f venv
python3.12 -m venv venv
source venv/bin/activate
pip install <full_path_to_pypi_lnx>/<project_name>-<version>-py3-none-any.whl --no-index --find-links=<full_path_to_pypi_lnx>
sudo cp <project_name>.service /etc/systemd/system/
sudo systemctl status <project_name>