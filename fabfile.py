#!/usr/bin/python3
"""Deploy Socket to remote server"""
from fabric.api import local, run, sudo, env, put, cd
from datetime import datetime
from dotenv import load_dotenv
from os import getenv

load_dotenv()
PSN = getenv('PROJECT_SHORT_NAME', 'python')  # from environment
ARCHIVE_DIR = 'versions/'
FILES = [
    '.env', 'requirements.txt', 'extract_questions.py', 'questions.txt', 'api', 'models'
]  # update this list according to your purposes


def create_archive():
    """Archive the entire project"""
    current_time = datetime.utcnow().strftime("%Y-%m-%d-%H-%M-%S")
    local("mkdir -p {}".format(ARCHIVE_DIR))
    archive_path = '{}/{}_{}.tar.gz'.format(ARCHIVE_DIR, PSN, current_time)
    local("tar -czvf {} {}".format(archive_path, ' '.join(FILES)))
    return archive_path


def copy_and_unpack_archive(archive_path):
    """Move arcive to remote"""
    archive_name = archive_path.split('/')[-1]
    run("mkdir -p {}".format(PSN))
    put(archive_path, PSN)
    run("tar -xzvf {}/{} -C {}".format(PSN, archive_name, PSN))
    run("rm {}/{}".format(PSN, archive_name))


def install_dependencies():
    """Install remote dependencies"""
    put('requirements.txt', '{}'.format(PSN))
    run('pip install -r {}/requirements.txt --break-system-packages'.format(PSN))


def start_socket_service():
    """Starts remote Socket service"""
    sudo('systemctl start {}.service'.format(PSN))


def stop_socket_service():
    """Stops remote Socket service"""
    sudo('systemctl stop {}.service'.format(PSN))


def remove_existing():
    """Removes all existing project files in remote server"""
    sudo('rm -rf {}'.format(PSN))


def upload_service_script():
    """Uploads, Enables and Start service script"""
    put(
        '{}.service'.format(PSN),
        '/etc/systemd/system/{}.service'.format(PSN),
        use_sudo=True
    )
    sudo('systemctl enable {}.service'.format(PSN))
    start_socket_service()


def restart_socket_service():
    """Restarts remote Socket service"""
    sudo('systemctl restart {}.service'.format(PSN))


def deploy():
    """Deploys Socket to remote"""
    archive_path = create_archive()
    remove_existing()
    copy_and_unpack_archive(archive_path=archive_path)
    install_dependencies()


def update():
    """Updates remote Socket"""
    deploy()
    restart_socket_service()

# TODO
# write a funxtion to install the following list of apt packages
# pkg-config libmysqlclient-dev python3-pip
