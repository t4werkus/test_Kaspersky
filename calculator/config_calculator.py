from math import log
from calculator.config import Config
import sys


def calculate_config(user_choice: int, config: Config, *args, **kwargs) -> dict:
    config_after_operation = {}
    match user_choice:
        case 1:  # Kafka
            sys.stdout.write("Kafka Config:\n")
            config_after_operation = calculate_kafka_config(config.agents, config.mail_traffic, config.distributed,
                                                            config.nodes)
        case 2:  # elastic search
            sys.stdout.write("elastic search Config:\n")
            config_after_operation = calculate_elastic_search_config(config.agents, config.distributed)
        case 3:  # processor
            sys.stdout.write("processor Config:\n")
            config_after_operation = calculate_processor_config(config.agents, config.storage, config.traffic,
                                                                config.distributed,
                                                                config.nodes)
        case 4:  # server
            sys.stdout.write("server Config:\n")
            config_after_operation = calculate_server_config(config.agents, config.storage, config.traffic,
                                                             config.distributed,
                                                             config.nodes)
        case 5:  # database server
            sys.stdout.write("database server Config:\n")
            config_after_operation = calculate_database_server_config(config.agents, config.storage, config.distributed,
                                                                      config.nodes)
        case 6:  # clickhouse
            sys.stdout.write("clickhouse Config:\n")
            config_after_operation = calculate_clickhouse_config(config.agents, config.storage, config.distributed)
        case 7:  # synchronizer
            sys.stdout.write("synchronizer Config:\n")
            config_after_operation = calculate_synchronizer_config(config.agents, config.storage, config.distributed)
        case 8:  # scanner
            sys.stdout.write("scanner Config:\n")
            config_after_operation = calculate_scanner_config(config.agents, config.distributed)
    return config_after_operation


def calculate_kafka_config(agents: int, mail_traffic: float,
                           distributed: bool, nodes: int, *args, **kwargs) -> dict:
    replicas: int = 3 if distributed else 1
    memory: float = mail_traffic * 0.5 if distributed else 100
    cpu: float = round((0.000169 * agents + 0.437923) * nodes / 3, 2)
    storage: float = round(0.0004 * agents + 0.3231, 3)
    return {
        "replicas": replicas,
        "memory": memory,
        "cpu": cpu,
        "storage": storage
    }


def calculate_elastic_search_config(agents: int, distributed: bool, *args, **kwargs) -> dict:
    replicas: int = 3 if distributed else 1
    memory: float = 0
    cpu: int = 3
    storage: float = 0.256 if agents < 5000 else (0.512 if agents < 10000 else 1)
    return {
        "replicas": replicas,
        "memory": memory,
        "cpu": cpu,
        "storage": storage
    }


def calculate_processor_config(agents: int, storage: float, traffic: float, distributed: bool, nodes: int, *args,
                               **kwargs) -> dict:
    replicas: int = (3 if distributed else 0) if agents > 0 and storage > 0 else 0
    memory: float = traffic * 0.5 if distributed else 100
    cpu: int = 3
    storage: float = round(-4.25877 + 0.98271 * log(agents),
                           3) if nodes > 0 else 0  # при agents < 76.2258 будет отрицательное число
    return {
        "replicas": replicas,
        "memory": memory,
        "cpu": cpu,
        "storage": storage
    }


def calculate_server_config(agents: int, storage: float, traffic: float, distributed: bool, nodes: int, *args,
                            **kwargs) -> dict:
    replicas: int = (min(agents, 2)) if agents > 0 and storage > 0 else 0
    memory: float = round(traffic * 0.5, 3) if distributed else 100
    cpu: int = 1
    storage: float = round(0.0019 * agents + 2.3154, 3) if nodes > 0 else 0
    return {
        "replicas": replicas,
        "memory": memory,
        "cpu": cpu,
        "storage": storage
    }


def calculate_database_server_config(agents: int, storage: float, distributed: bool, nodes: int, *args,
                                     **kwargs) -> dict:
    replicas: float = (max(round(agents / 15000, 1), 1) if distributed else 1) if agents > 0 else 0
    memory: float = round(storage * 1.6, 3) if distributed else 100
    cpu: int = 1
    storage: float = round((0.00000002 * agents * agents + 0.00067749 * agents + 4.5) * agents / nodes,
                           3) if nodes > 0 else 0
    return {
        "replicas": replicas,
        "memory": memory,
        "cpu": cpu,
        "storage": storage
    }


def calculate_clickhouse_config(agents: int, storage: float, distributed: bool, *args, **kwargs) -> dict:
    replicas: float = (max(round(agents / 15000, 1), 1) if distributed else 1) if agents > 0 else 0
    memory: float = round(storage * 1.6, 3) if distributed else 100
    cpu: int = 1
    storage: float = round(0.0000628 * agents + 0.6377, 3) if distributed else 0
    return {
        "replicas": replicas,
        "memory": memory,
        "cpu": cpu,
        "storage": storage
    }


def calculate_synchronizer_config(agents: int, storage: float, distributed: bool, *args, **kwargs) -> dict:
    replicas: int = 1 if agents > 0 else 0
    memory: float = round(storage / 5000, 3) * 1.6 if distributed else 100
    cpu: int = 1
    storage: float = round(0.0002 * agents + 0.6, 3) if distributed else 0
    return {
        "replicas": replicas,
        "memory": memory,
        "cpu": cpu,
        "storage": storage
    }


def calculate_scanner_config(agents: int, distributed: bool, *args, **kwargs) -> dict:
    replicas: int = 1 if agents > 0 else 0
    memory: int = 300
    cpu: int = 1
    storage: float = round(0.0002 * agents + 0.6, 3) if distributed else 0
    return {
        "replicas": replicas,
        "memory": memory,
        "cpu": cpu,
        "storage": storage
    }
