from calculator import input_config
from calculator.config import Config
from calculator.config_calculator import calculate_config
from calculator.json_input import read_json
from calculator.pprint import pprint


def choice_input_for_config(choice_config, choice_input, *args, **kwargs) -> None:
    config = Config()
    match choice_input:
        case 1:
            config = input_config.choice_config(choice_config)
        case 2:
            json_file = input("Enter the JSON file name or path: ")
            config: Config = Config(*read_json(json_file))
    pprint(calculate_config(choice_config, config))
