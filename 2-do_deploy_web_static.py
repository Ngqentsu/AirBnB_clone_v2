#!/usr/bin/python3
"""
Fabric script that distributes an archive to your web servers
"""

from fabric.api import run, put, env
from os.path import exists
from datetime import datetime

env.hosts = ['<IP web-01>', '<IP web-02>']


def do_deploy(archive_path):
    """Distributes an archive to the web servers"""
    if not exists(archive_path):
        return False

    try:
        # Upload the archive to the /tmp/ directory of the web server
        put(archive_path, '/tmp/')

        # Get the filename without extension
        filename = archive_path.split('/')[-1].split('.')[0]

        # Uncompress the archive to the folder /data/web_static/releases/<filename>
        run('mkdir -p /data/web_static/releases/{}'.format(filename))
        run('tar -xzf /tmp/{} -C /data/web_static/releases/{}/'
            .format(filename + '.tgz', filename))

        # Delete the archive from the web server
        run('rm /tmp/{}'.format(filename + '.tgz'))

        # Delete the symbolic link /data/web_static/current
        run('rm -f /data/web_static/current')

        # Create a new symbolic link /data/web_static/current
        run('ln -s /data/web_static/releases/{} /data/web_static/current'
            .format(filename))

        return True
    except:
        return False
