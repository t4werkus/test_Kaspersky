import sys


def choice_config_input(*args, **kwargs) -> tuple:
    sys.stdout.write("1) Kafka\n"
                     "2) elastic search\n"
                     "3) processor\n"
                     "4) server\n"
                     "5) database server\n"
                     "6) clickhouse\n"
                     "7) synchronizer\n"
                     "8) scanner\n")
    sys.stdout.write("Enter the choice: ")
    choice_config: int = int(sys.stdin.buffer.readline())
    while not (1 <= choice_config <= 8):
        sys.stdout.write("\nWrong input!\nEnter the number between 1 and 8!\n")
        sys.stdout.write("1) Kafka\n"
                         "2) elastic search\n"
                         "3) processor\n"
                         "4) server\n"
                         "5) database server\n"
                         "6) clickhouse\n"
                         "7) synchronizer\n"
                         "8) scanner\n")
        sys.stdout.write("Enter the choice: ")
        choice_config: int = int(sys.stdin.buffer.readline())

    sys.stdout.write("1) from console\n"
                     "2) from json file\n")
    sys.stdout.write("Enter the choice input data: ")
    choice_input: int = int(sys.stdin.buffer.readline())
    while not (1 <= choice_input <= 2):
        sys.stdout.write("\nWrong input!\nEnter 1 or 2!\n")
        sys.stdout.write("1) from console\n"
                         "2) from json file\n")
        sys.stdout.write("Enter the choice input data: ")
        choice_input: int = int(sys.stdin.buffer.readline())
    return choice_config, choice_input
