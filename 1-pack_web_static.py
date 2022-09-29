#!/usr/bin/python3
"""
This fabric script generates a .tgz archive from the contents of the web_static
folder of your AirBnB Clone repo, using the function do_pack
"""
from fabric.api import local
from datetime import datetime

def do_pack():
    """
    Creates a .tgz archive
    """
    time = datetime.now().strftime('%Y%m%d%H%M%S')
    path = f"versions/web_static_{time}.tgz"
    local("mkdir -p versions")

    if local(f"tar -cvzf {path} web_static").failed:
        return None
    else:
        return path
