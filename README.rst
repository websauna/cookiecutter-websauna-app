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
* `Tox`_ testing: Setup to easily test for Python 3.4 and above.

Usage
=====

To generate a new Websauna application package, first install Cookiecutter and websauna.j2secret:

    .. code-block:: shell

        $ pip install cookiecutter websauna.j2secret


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
        repo_name [websauna.package]: company.application
        namespace [company]: company
        package_name [application]: application
        release_date [today]:
        year [2017]:
        version [1.0.0a1]:
        authentication_random [82e7affc6b55e58dd962e74e37dedc19679c92b9]:
        authomatic_random [22539423a5ceb1fe6f7c6cd1a3a1867315236f25]:
        session_random [1261a92aa68dc52877d8d2606943a4fb69ca0879]:


.. note:: We recommend you accept the values presented for authentication_random, authomatic_random, session_random
          as they were generated for this execution.


After a while, the generation will be finished and the following message will be displayed:

    .. code-block::

        ===============================================================================
        Websauna Application.
        Package company.application was generated.
        Now, code it, create a git repository, push to your Github account.
        Sorry for the convenience.
        ===============================================================================


Next Steps
==========

* Code the package
* Create a git repository
* Push to Github (or any other platform)


.. _`Websauna`: https://websauna.org
.. _`Cookiecutter`: https://github.com/audreyr/cookiecutter
.. _`Travis-CI`: https://travis-ci.org
.. _`Tox`: https://tox.readthedocs.io
