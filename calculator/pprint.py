import sys


def pprint(config: dict, *args, **kwargs) -> None:
    sys.stdout.write("\t")
    print(*[f"{key}: {value}" for key, value in config.items()], sep="\n\t")
