import requests
from jinja2 import Environment, FileSystemLoader
import json

env = Environment(loader=FileSystemLoader("."), trim_blocks=True, lstrip_blocks=True)


def fetch_data():
    servers = requests.get("http://localhost:5000/api/servers").json()

    return servers


def render_configurations(data):
    server_template = env.get_template("server_config.ja2")

    servers = data["servers"]
    switches = data["switches"]
    config = server_template.render(servers=servers, switches=switches)
    print(f"\nRendered config:\n{config}\n")


if __name__ == "__main__":
    data = fetch_data()
    data = json.loads(data)
    render_configurations(data)
