"""Validate variables."""
import sys


# Validate that package_name is not named site
package_name = '{{ cookiecutter.package_name }}'

if package_name == 'site':
    print(
        'Sorry, you may not name your package "site". '
        'The package name "site" has a special meaning in '
        'Python.  Please name it anything except "site".'
    )

    # exits with status 1 to indicate failure
    sys.exit(1)
