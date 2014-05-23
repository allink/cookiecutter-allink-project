project_python = '{{ cookiecutter.project_name }}'

try:
    from allink_essentials.fabfiles.proxima_class_fabfile import *  # noqa
    from allink_essentials.fabfiles.proxima_class_fabfile import _setup_path
except ImportError:

    print "Try to execute python fabfile.py first"

else:
    env.project_python = project_python

    def production():
        _setup_path('production')

    env.deployments = ('production',)


if __name__ == '__main__':
    import os
    import subprocess

    os.path.dirname(os.path.abspath(__file__))

    if not os.path.isdir("media"):
        os.mkdir("media")
    if not os.path.isfile(".git/hooks/pre-commit"):
        os.symlink("../../pre-commit", ".git/hooks/pre-commit")

    # install requirements
    subprocess.call(["pip", "install", "--upgrade", "wheel"])
    subprocess.call(["pip", "install", "--upgrade", "Fabric"])
    subprocess.call(["pip", "install", "--requirement", "REQUIREMENTS_LOCAL"])
