#!/usr/bin/python3
""" Fabric script that generates .tgz archive from web_static """

from fabric.api import local, run, env
from datetime import datetime

env.user = 'your_username'
env.hosts = ['your_host']


def do_pack():
    """ Function used to generates .tgz archive from web_static"""
    try:
        local("mkdir -p versions")
        date = datetime.now().strftime("%Y%m%d%H%M%S")
        filename = "versions/web_static_{}.tgz".format(date)
        local("tar -cvzf {} web_static".format(filename))
        return filename
    except Exception as e:
        return None
