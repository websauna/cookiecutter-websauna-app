"""Validate variables."""
import sys


namespace = '{{ cookiecutter.namespace }}'
package_name = '{{ cookiecutter.package_name }}'

failed = False

# Validate that namespace is not named websauna
if namespace == 'websauna':
    print(
        'Sorry, your application namespace should not be "websauna". '
        'The namespace "websauna" is reserved for the framework '
        'and using it could lead to issues.'
    )
    failed = True

# Validate that package_name is not named site
if package_name == 'site':
    print(
        'Sorry, you may not name your package "site". '
        'The package name "site" has a special meaning in '
        'Python.  Please name it anything except "site".'
    )
    failed = True


if failed:
    # exits with status 1 to indicate failure
    sys.exit(1)
