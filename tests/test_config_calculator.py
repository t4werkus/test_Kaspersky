import pytest
from calculator.config_calculator import *
from calculator.json_input import read_json


def test_kafka_config_calculation():
    config = calculate_config(1, Config(1000, 100, 50, 10, True, 5))
    assert config == {
        "replicas": 3,
        "memory": 5.0,
        "cpu": 1.01,
        "storage": 0.723
    }


def test_elastic_search_config_calculation():
    config = calculate_config(2, Config(1000, 100, 50, 10, True, 5))
    assert config == {
        "replicas": 3,
        "memory": 0,
        "cpu": 3,
        "storage": 0.256
    }


def test_processor_config_calculation():
    config = calculate_config(3, Config(1000, 100, 50, 10, True, 5))
    assert config == {
        "replicas": 3,
        "memory": 25.0,
        "cpu": 3,
        "storage": 2.53
    }


def test_server_config_calculation():
    config = calculate_config(4, Config(1000, 100, 50, 10, True, 5))
    assert config == {
        "replicas": 2,
        "memory": 25.0,
        "cpu": 1,
        "storage": 4.215
    }


def test_database_server_config_calculation():
    config = calculate_config(5, Config(10000, 1000, 500, 100, True, 10))
    assert config == {
        "replicas": 1,
        "memory": 1600.0,
        "cpu": 1,
        "storage": 13274.9
    }


def test_clickhouse_config_calculation():
    config = calculate_config(6, Config(20000, 2000, 1000, 200, True, 20))
    assert config == {
        "replicas": 1.3,
        "memory": 3200.0,
        "cpu": 1,
        "storage": 1.894
    }


def test_synchronizer_config_calculation():
    config = calculate_config(7, Config(1000, 100, 50, 10, True, 5))
    assert config == {
        "replicas": 1,
        "memory": 0.032,
        "cpu": 1,
        "storage": 0.8
    }


def test_scanner_config_calculation():
    config = calculate_config(8, Config(1000, 100, 50, 10, True, 5))
    assert config == {
        "replicas": 1,
        "memory": 300,
        "cpu": 1,
        "storage": 0.8
    }


def test_json_input():
    json = read_json("json_file.json")
    assert json == (1000, 100, 50, 10, True, 5)


def test1_json_input():
    json = read_json("json_file1.json")
    assert json == (0, 0.0, 0.0, 0.0, False, 0)

if __name__ == "__main__":
    pytest.main()



