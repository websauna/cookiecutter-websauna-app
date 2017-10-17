"""{{ cookiecutter.project_name }} views."""
from websauna.system.http import Request
from websauna.system.core.route import simple_route


# Configure a sample view provided by this addon
@simple_route("/", route_name="home", renderer='{{ cookiecutter.repo_name }}/home.html')
def home(request: Request):
    """Render site homepage."""
    return {"project": "{{ cookiecutter.project_name }}"}
