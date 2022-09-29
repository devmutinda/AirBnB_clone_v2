#!/usr/bin/python3
"""
This script creates and distributes an archive to your web servers,
using the function deploy
"""
from datetime import datetime
from fabric.api import put, run, env, local
import os

env.hosts = ['3.236.46.187', '3.239.83.68']
env.user = "ubuntu"


def do_pack():
    """
    Creates a .tgz archive
    """
    time = datetime.now().strftime('%Y%m%d%H%M%S')
    path = "versions/web_static_{}.tgz".format(time)
    local("mkdir -p versions")

    if local("tar -cvzf {} web_static".format(path)).succeeded:
        return path


def do_deploy(archive_path):
    """
    deploys archive to web server
    """
    path = archive_path.split('/')[-1]
    line = path.split('.')[0]
    if not os.path.isfile(archive_path):
        return False
    if put(archive_path, "/tmp/{}".format(path)).failed:
        return False
    if run("rm -rf /data/web_static/releases/{}"
            .format(line)).failed:
        return False
    if run("mkdir -p /data/web_static/releases/{}/"
            .format(line)).failed:
        return False
    if run("tar -xzf /tmp/{} -C /data/web_static/releases/{}/"
            .format(path, line)).failed:
        return False
    if run("rm /tmp/{}".format(path)).failed:
        return False
    if run("mv /data/web_static/releases/{}/web_static/* "
            "/data/web_static/releases/{}/".format(line, line)).failed:
        return False
    if run("rm -rf /data/web_static/releases/{}/web_static"
            .format(line)).failed:
        return False
    if run("rm -rf /data/web_static/current").failed:
        return False
    if run("ln -s /data/web_static/releases/{}/ /data/web_static/current"
            .format(line)).failed:
        return False

    return True


def deploy():
    """
    Deploys changes to webserver
    """
    path = do_pack()
    if not path:
        return False

    return do_deploy(path)
