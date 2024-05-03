import csv
from typing import List, Dict


class ProcessJobs:
    def __init__(self) -> None:
        self.jobs_list = list()

    def read(self, path) -> List[Dict]:
        with open(path, mode="r") as file:
            reader = csv.DictReader(file)
            lista = list(reader)
            self.jobs_list = lista

    def get_unique_job_types(self) -> List[str]:
        pass

    def filter_by_multiple_criteria(self) -> List[dict]:
        pass
