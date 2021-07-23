from dataclasses import dataclass
from typing import Optional


# clean architecture in django -> https://medium.com/21buttons-tech/clean-architecture-in-django-d326a4ab86a9

@dataclass
class Report:
    data: str
    id: Optional[int] = None
