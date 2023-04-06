#!/usr/bin/python3
"""
Fabric script method:
    do_deploy: deploys archive to webservers
Usage:
    fab -f 2-do_deploy_web_static.py
    do_deploy:archive_path=versions/web_static_20170315003959.tgz
    -i my_ssh_private_key -u ubuntu
"""
from fabric.api import env, put, run
from os.path import exists
env.hosts = ['35.229.54.225', '35.231.225.251']


def do_deploy(archive_path):
    '''distributes an archive to my web servers'''
    if not exists(archive_path):
        return False
    try:
        file_name = archive_path.split("/")[-1].split(".")[0]
        put(archive_path, "/tmp/")

        run("mkdir -p /data/web_static/releases/{}".format(file_name))

        run("tar -xzf /tmp/{}.tgz -C /data/web_static/releases/{}/"
            .format(file_name, file_name))

        run('rm -rf /tmp/{}.tgz'.format(file_name))

        run(('mv /data/web_static/releases/{}/web_static/* ' +
            '/data/web_static/releases/{}/')
            .format(file_name, file_name))

        run('rm -rf /data/web_static/releases/{}/web_static'
            .format(file_name))

        run('rm -rf /data/web_static/current')

        run(('ln -s /data/web_static/releases/{}/' +
            ' /data/web_static/current')
            .format(file_name))
        return True
    except Exception:
        return False
