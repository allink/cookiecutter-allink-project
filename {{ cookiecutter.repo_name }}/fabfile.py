project_python = '{{ cookiecutter.project_name }}'

try:
    from allink_essentials.fabfiles.proxima_class_fabfile import *  # noqa
    from allink_essentials.fabfiles.proxima_class_fabfile import _setup_path
except ImportError:

    print "Try to execute python fabfile.py first"

else:
    env.project_python = project_python

    def production():
        env.unique_identifier = '{{ cookiecutter.project_name }}_production'
        env.git_repository = 'git@github.com:{{ cookiecutter.repo_organisation }}/{{ cookiecutter.repo_name }}.git'
        env.environment = 'production'
        env.git_branch = 'master'
        env.git_remote = 'origin'
        env.hosts = ['.nine.ch']
        env.user = 'www-data'
        env.project = '{{ cookiecutter.repo_name }}'
        env.root = '/home/www-data/projects'
        env.is_stage = False

        _setup_path()

    env.deployments = ('production',)


if __name__ == '__main__':
    import os
    import subprocess

    os.path.dirname(os.path.abspath(__file__))

    if not os.path.isdir("media"):
        os.mkdir("media")
    if not os.path.isfile(".git/hooks/pre-commit"):
        os.symlink("../../pre-commit", ".git/hooks/pre-commit")

    with open('.env', 'w') as f:
        f.write('DATABASE_URL=postgres://%s:%s@localhost/%s\n' % (
            os.environ['PGUSER'],
            os.environ['PGPASSWORD'],
            '{{ cookiecutter.project_name }}',
        ))

    # install requirements
    subprocess.call(["pip", "install", "--upgrade", "wheel"])
    subprocess.call(["pip", "install", "--upgrade", "Fabric"])
    subprocess.call(["pip", "install", "--requirement", "REQUIREMENTS_LOCAL"])
