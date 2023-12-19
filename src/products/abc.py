from abc import ABC, abstractmethod
from typing import Optional



class ABCProductService(ABC):

    @abstractmethod
    def get_all(self, name : Optional[str]):
        """Get all products or search by name"""

