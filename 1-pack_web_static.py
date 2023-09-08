#!/usr/bin/python3
"""Generate a .tgz archive from the content of the web_static folder"""
from fabric.api import local
import time

def do_pack():
    """Generate a .tgz from a web_static folder"""
    try:
        local("mkdir -p versions")
        local("tar -cvzf versions/web_static_{}.tgz web_static/".
              format(time.strftime("%Y%m%d%H%M%S")))
        return ("versions/web_static_{}.tgz".format(time.
                                                    strftime("%Y%m%d%H%M%S")))
    except:
        return None
