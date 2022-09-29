#!usr/bin/python3
"""
This script deletes out-of-date archives, using the function do_clean
"""
from fabric.api import local, env, run

env.hosts = ["3.236.46.187", "3.239.83.68"]
env.user = "ubuntu"


def do_clean(number=0):
    """
    Deletes archives
    """
    # delete locally
    answer = local("ls versions", capture=True)
    files = answer.splitlines()
    count = len(files)
    number = int(number)

    for file in files:
        if count <= number or count == 1 and number == 0:
            break
        local("rm versions/{}".format(file))
        count -= 1

    # delete in remote servers
    output = run("ls /data/web_static/releases")
    files = output.stdout.split("\r\n")
    count = len(files)
    number = int(number)

    for file in files:
        if count <= number or count == 1 and number == 0:
            break
        run("rm -rf /data/web_static/releases/{}".format(file.split('.')[0]))
        count -= 1
