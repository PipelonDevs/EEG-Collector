from abc import ABC, abstractmethod
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from utils.dict_types import DataClassInstance

class ISavingStrategy(ABC):
    @abstractmethod
    def pull(self, url: str) -> dict:
        pass
    
    @abstractmethod
    def push(self, data: 'DataClassInstance', url: str) -> None:
        pass

    