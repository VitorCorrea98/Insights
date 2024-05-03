from src.insights.jobs import ProcessJobs
from typing import List


class ProcessIndustries(ProcessJobs):
    def __init__(self):
        super().__init__()

    def get_unique_industries(self) -> List[str]:
        lista_de_industries = [
            job["industry"] for job in self.jobs_list if bool(job["industry"])
        ]
        lista = list(set(lista_de_industries))
        return lista
