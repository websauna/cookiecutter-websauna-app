.. image:: https://raw.githubusercontent.com/websauna/cookiecutter-websauna-app/master/logo/logo-150.png

`Cookiecutter`_ template to create a `Websauna`_ Application.

.. |ci| image:: https://img.shields.io/travis/websauna/cookiecutter-websauna-app/master.svg?style=flat-square
    :target: https://travis-ci.org/websauna/cookiecutter-websauna-app/

.. |latest| image:: https://img.shields.io/pypi/v/cookiecutter-websauna-app.svg
    :target: https://pypi.python.org/pypi/cookiecutter-websauna-app/
    :alt: Latest Version

.. |license| image:: https://img.shields.io/pypi/l/cookiecutter-websauna-app.svg
    :target: https://pypi.python.org/pypi/cookiecutter-websauna-app/
    :alt: License

.. |versions| image:: https://img.shields.io/pypi/pyversions/cookiecutter-websauna-app.svg
    :target: https://pypi.python.org/pypi/cookiecutter-websauna-app/
    :alt: Supported Python versions

+-----------+-----------+-----------+-----------+
| |ci|      | |license| | |versions|| |latest|  |
+-----------+-----------+-----------+-----------+


Features
========

* `Websauna`_: Support to the latest version.
* Virtualenv automatically created and setup in development mode.
* `Travis-CI`_: Ready for Travis Continuous Integration testing.
* `Tox`_ testing: Setup to easily test for Python 3.5 and above.

Usage
=====

To generate a new Websauna application package, first install Cookiecutter:

    .. code-block:: shell

        $ pip install cookiecutter


Now run it against this repo:

    .. code-block:: shell

        $ cookiecutter gh:websauna/cookiecutter-websauna-app


You'll be prompted for some values. Provide them, then a Websauna application will be created for you.

**Warning**: After this point, change 'Amazing Team', 'websauna', etc to your own information.

Answer the prompts with your own desired options. For example:

    .. code-block::

        full_name [Amazing Team]: Amazing Team
        email [team@mycompany.com]: team@company.com
        company [Websauna]: Company
        github_username [websauna]: company
        project_name [My Package]: My Application
        project_short_description [A nice and short description.]: Another Websauna application
        tags [python package websauna pyramid]: python package websauna pyramid
        repo_name [my.app]: company.application
        namespace [my]: company
        package_name [app]: application
        release_date [today]:
        year [2017]:
        version [1.0.0a1]:
        Select create_virtualenv:
        1 - True
        2 - False
        Choose from 1, 2 [1]: 1


After a while, the generation will be finished and the following message will be displayed:

    .. code-block::

        ===============================================================================
        Websauna Application.
        Package my.app was generated.
        Now, code it, create a git repository, push to your GitHub account.
        To deploy this Websauna package with Ansible, use the following variables

            - package_name: my.app
            - package_path: my/app

        Read more about Websauna deployment:
          https://websauna.org/docs/tutorials/deployment/index.html

        Sorry for the convenience.
        ===============================================================================


Next Steps
==========

* Code the package
* Create a git repository
* Push to GitHub (or any other platform)


.. _`Websauna`: https://websauna.org
.. _`Cookiecutter`: https://github.com/audreyr/cookiecutter
.. _`Travis-CI`: https://travis-ci.org
.. _`Tox`: https://tox.readthedocs.io
