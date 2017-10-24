"""Create virtualenv and print a thank you note."""
from textwrap import dedent

import subprocess
import sys


try:
    import venv
    VIRTUALENV_AVAILABLE = True
except ImportError:
    VIRTUALENV_AVAILABLE = False


create_virtualenv = True if '{{ cookiecutter.create_virtualenv }}' == 'Yes' else False


if VIRTUALENV_AVAILABLE and create_virtualenv:
    try:
        venv.create('env', with_pip=True)
        proc = subprocess.Popen(
            ['env/bin/pip', 'install', '-r', 'requirements.txt'],
            shell=sys.platform.startswith('win'),
            cwd='.'
        )
        proc.wait()
    except subprocess.CalledProcessError:
        print('It was not possible to create the virtualenv. Maybe inside tox?')
    except FileNotFoundError as e:
        print(subprocess.check_output(['ls', './env/bin/']), str(e))


msg = dedent("""
    ===============================================================================
    Websauna Application.
    Package {{ cookiecutter.repo_name }} was generated.
    Now, code it, create a git repository, push to your Github account.
    To deploy this Websauna package with Ansible, use the following variables

        - package_name: {{ cookiecutter.repo_name }}
        - package_path: {{ cookiecutter.namespace }}/{{ cookiecutter.package_name }}

    Read more about Websauna deployment:
      https://websauna.org/docs/tutorials/deployment/index.html

    Sorry for the convenience.
    ===============================================================================
""")

print(msg)
