#!/usr/bin/python3
"""
A Fabric script that generates a .tgz archive from the
contents of the build directory and deploy to the listed hosts.
"""

from fabric.api import local, env, run, put, sudo
from datetime import datetime
import os


def do_pack():
    """Compress the contents of build"""

    #  create `versions` dir if not exists
    # local('mkdir -p versions')
    # local('mkdir versions')

    #  update build before packing
    local('npm run build')

    #  create compressed tgz file
    time_stamp = datetime.now().strftime('%Y%m%d%H%M%S')
    path = 'versions/build_' + time_stamp + '.tgz'
    result = local('tar -cvzf {} build/'.format(path))
    if result.succeeded:
        return path
    else:
        return None


def do_deploy(archive_path):
    """distributes an archive to env.hosts web servers"""

    #  if empty argument passed
    if not os.path.exists(archive_path):
        return False

    basename = os.path.basename(archive_path)
    path = basename.replace('.tgz', '')
    path = '/data/mindpal/releases/{}'.format(path)

    #  upload archive to server
    put(archive_path, '/tmp/')
    run('mkdir -p {}'.format(path))
    run('tar -xvzf /tmp/{} -C {}'.format(basename, path))
    run('mv {}/build/* {}'.format(path, path))
    run('rm -rf {}/build/'.format(path))
    run('rm /data/mindpal/current')
    run('ln -s {} /data/mindpal/current'.format(path))
    return True


def deploy():
    """creates and distributes an archive to web servers"""
    path = do_pack()
    if path is None:
        return False
    return do_deploy(path)


def do_clean(number=0):
    """ Deletes out-of-date archives."""

    #  check if path `versions/` exists
    if not os.path.exists('versions/'):
        return

    #  resolve least number of archives to keep
    if number == 0:
        number = 1

    #  capture list of archives : local
    archives = local('ls -t versions/', capture=True)
    archives = archives.split('\n')

    archives = archives[int(number):]

    #  remove local archives
    for archive in archives:
        local('rm versions/{}'.format(archive))

    #  capture list of archives : remote
    archives = run('ls -t /data/mindpal/releases')
    archives = archives.split('\n')

    archives = archives[int(number):]

    if 'test' in archives:
        archives.remove('test')

    for archive in archives:
        run('rm -rf /data/mindpal/releases/{}'.format(
            archive))

    return
