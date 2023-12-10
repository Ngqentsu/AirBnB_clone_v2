#!/usr/bin/python3
"""
Fabric script that deletes out-of-date archives
"""

from fabric.api import env, run, local
from datetime import datetime

env.user = 'your_username'
env.hosts = ['<IP web-01>', '<IP web-02>']

def do_clean(number=0):
    """Deletes out-of-date archives"""
    try:
        number = int(number)
        number = 1 if number < 1 else number + 1

        # Local clean
        local("ls -t versions | tail -n +{} | xargs -I {{}} rm versions/{{}}".format(number))

        # Remote clean
        run("ls -t /data/web_static/releases | tail -n +{} | xargs -I {{}} rm -rf /data/web_static/releases/{{}}".format(number))
        run("ls -t /data/web_static/releases | tail -n +{} | xargs -I {{}} rm -rf /data/web_static/releases/{{}}".format(number))
        return True
    except:
        return False
