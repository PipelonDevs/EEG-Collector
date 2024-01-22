from dataclasses import asdict
import json
from typing import TYPE_CHECKING
import os.path

from .ISavingStrategy import ISavingStrategy

if TYPE_CHECKING:
    from utils.dict_types import DataClassInstance 
    
class SaveToFile(ISavingStrategy):

    def pull(self, url: str) -> dict:
        if not os.path.isfile(url):
            return {}

        with open(url, 'r') as f:
            return json.load(f)
        

    def push(self, data: 'DataClassInstance', url: str) -> None:
        with open(url, 'w+', encoding='utf-8') as f:
            json.dump(asdict(data), f, ensure_ascii=False, indent=4)