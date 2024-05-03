from src.pre_built.counter import count_ocurrences

path = "data/jobs.csv"


def test_counter():
    assert count_ocurrences(path, "develop") == 9049
