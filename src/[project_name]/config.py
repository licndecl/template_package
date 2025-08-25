import os, sys
from decouple import config, AutoConfig

# determine if application is a script file or frozen exe       
if getattr(sys, 'frozen', False):
    exe_dir = os.path.dirname(sys.executable)
elif __file__:
    # exe_dir = C:\WINDOWS\system32 for service
    exe_dir = os.path.dirname(os.path.abspath(__file__))
config = AutoConfig(exe_dir)
