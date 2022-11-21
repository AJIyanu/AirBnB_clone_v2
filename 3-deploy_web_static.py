#!/usr/bin/python3
"""Pack and deploy remotely"""


from . import 1-pack_web_static as pack
from . import 2-do_deploy_web_static as deploy

import os
env.hosts = ['44.192.72.216', '44.192.52.223']


def deploy():
    """ready to deploy??"""
    path = pack.do_pack()
    if path is not None:
        return (do_deploy(path))
    return (False)
