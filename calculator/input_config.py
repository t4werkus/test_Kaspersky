from calculator.config import Config
import sys


# Порядок ввода данных в некоторых функциях нарушен в угоду принципа DRY
def choice_config(user_choice: int, *args, **kwargs) -> Config:
    agents, storage, traffic, mail_traffic, distributed, nodes = 0, 0.0, 0.0, 0.0, False, 0
    match user_choice:
        case 1:  # kafka
            agents, distributed = input_case_for_agents_distributed()

            sys.stdout.write("Enter the mail traffic amount: ")
            mail_traffic: float = float(sys.stdin.buffer.readline())
            while mail_traffic < 0:
                sys.stdout.write("\nWrong input!\nEnter the natural number or 0!\n")
                sys.stdout.write("Enter the mail traffic amount: ")
                mail_traffic: float = float(sys.stdin.buffer.readline())
            nodes: int = input_nodes()

        case 2:  # elastic_search
            agents, distributed = input_case_for_agents_distributed()

        case 3:  # processor
            agents, storage, traffic, distributed, nodes = input_case_for_processor_and_server()
            while agents < 76.2258:
                sys.stdout.write("\nWith such agents there will be negative! (Enter more that 76)\n")
                sys.stdout.write("Enter the number of agents: ")
                agents: int = int(sys.stdin.buffer.readline())

        case 4:  # server
            agents, storage, traffic, distributed, nodes = input_case_for_processor_and_server()

        case 5:  # database_server
            agents, storage, distributed, nodes = input_case_for_agents_storage_distributed_nodes()

        case 6:  # clickhouse
            agents, storage, distributed = input_case_for_agents_storage_distributed()

        case 7:  # synchronizer
            agents, storage, distributed = input_case_for_agents_storage_distributed()

        case 8:  # scanner
            agents, distributed = input_case_for_agents_distributed()

    return Config(agents, storage, traffic, mail_traffic, distributed, nodes)


def input_case_for_agents_distributed(*args, **kwargs) -> tuple:
    sys.stdout.write("Enter the number of agents: ")
    agents: int = int(sys.stdin.buffer.readline())
    while agents < 0:
        sys.stdout.write("\nWrong input!\nEnter the natural number or 0!\n")
        sys.stdout.write("Enter the number of agents: ")
        agents: int = int(sys.stdin.buffer.readline())

    sys.stdout.write(
        "Is the service distributed (0 is false, but everything else is true): ")
    distributed: bool = bool(sys.stdin.buffer.readline())

    return agents, distributed


def input_case_for_agents_storage_distributed(*args, **kwargs) -> tuple:
    agents, distributed = input_case_for_agents_distributed()

    sys.stdout.write("Enter the storage amount: ")
    storage: float = float(sys.stdin.buffer.readline())
    while storage < 0:
        sys.stdout.write("\nWrong input!\nEnter the natural number or 0!\n")
        sys.stdout.write("Enter the storage amount: ")
        storage: float = float(sys.stdin.buffer.readline())
    return agents, storage, distributed


def input_case_for_agents_storage_distributed_nodes(*args, **kwargs) -> tuple:
    agents, storage, distributed = input_case_for_agents_storage_distributed()

    nodes: int = input_nodes()

    return agents, storage, distributed, nodes


def input_case_for_processor_and_server(*args, **kwargs) -> tuple:
    agents, storage, distributed, nodes = input_case_for_agents_storage_distributed_nodes()

    sys.stdout.write("Enter the traffic amount: ")
    traffic: float = float(sys.stdin.buffer.readline())
    while traffic < 0:
        sys.stdout.write("\nWrong input!\nEnter the natural number or 0!\n")
        sys.stdout.write("Enter the traffic amount: ")
        traffic: float = float(sys.stdin.buffer.readline())

    return agents, storage, traffic, distributed, nodes


def input_nodes(*args, **kwargs) -> int:
    sys.stdout.write("Enter the number of nodes: ")
    nodes: int = int(sys.stdin.buffer.readline())
    while nodes < 0:
        sys.stdout.write("\nWrong input!\nEnter the natural number or 0!\n")
        sys.stdout.write("Enter the number of nodes: ")
        nodes: int = int(sys.stdin.buffer.readline())
    return nodes
