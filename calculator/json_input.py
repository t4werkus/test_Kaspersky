import json
import sys


def read_json(json_file: str, *args, **kwargs) -> tuple:
    agents, storage, traffic, mail_traffic, distributed, nodes = 0, 0.0, 0.0, 0.0, False, 0
    try:
        with open(json_file, "r") as file:
            data = json.load(file)  # Предполагается, что JSON файл содержит все необходимые параметры
            agents = data["agents"]
            storage = data["storage"]
            traffic = data["traffic"]
            mail_traffic = data["mail_traffic"]
            distributed = data["distributed"]
            nodes = data["nodes"]
    except FileNotFoundError:
        sys.stdout.write("File not found")
    except json.JSONDecodeError:
        sys.stdout.write("Invalid JSON file")
    return agents, storage, traffic, mail_traffic, distributed, nodes
