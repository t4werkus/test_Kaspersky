from calculator.choice_input_for_config import choice_input_for_config
from calculator.choice_config_input import choice_config_input


def main() -> None:
    choice_input_for_config(*choice_config_input())


if __name__ == "__main__":
    main()
