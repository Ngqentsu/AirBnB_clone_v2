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


def deploy():
    """ creates and distributes an archive to your web servers
    """
    new_archive_path = do_pack()
    if exists(new_archive_path) is False:
        return False
    result = do_deploy(new_archive_path)
    return result
