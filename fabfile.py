from fabric.api import env, run
from fabric.operations import sudo

GIT_REPO = 'https://github.com/zmxia/blogproject.git'

env.user = 'root'
env.password = 'Xia43722'
env.hosts = '39.106.30.80'
env.port = '22'

def deploy();
    source_folder = '/home/xiafr/sites/demo.zmxia.top/blogproject'

    run('cd %s && git pull' % source_folder)
    run("""
        cd {} &&     
        ../env/bin/pip install -r requirements.txt &&
        ../env/bin/python3 manage.py collectstatic --noinput &&
        ../env/bin/python3 manage.py migrate
        """.format(source_folder))
    sudo('systemctl start xiafr')
    sudo('nginx -s reload')
