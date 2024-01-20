import json
from typing import Dict, List
from dataclasses import dataclass, asdict

@dataclass
class Annotation(dict):
    start: int
    end: int
    label: str

@dataclass
class Meta:
    device: str
    unit_name: str
    clock_rate: int
    channels: int
    displayable_rows: Dict[str, List[int]]
    notes: str

@dataclass
class Annotations(dict):
    meta: Meta
    data: list[Annotation]

    def __init__(self, file_path):
        with open(file_path, 'r') as f:
            data = json.load(f)
        self.meta = Meta(**data['meta'])
        self.data = [Annotation(**d) for d in data['data']]
        
    def save_annotations(self, file_path: str) -> None:
        with open(file_path, 'w', encoding='utf-8') as f:
            json.dump(asdict(self), f, ensure_ascii=False, indent=4)

if __name__ == '__main__':
    d = Annotations('Datasets/GameDatasets/user123_league of legends_2024-01-15/user123_league of legends_2024-01-15_22-59.json')
    
    print(d.meta.device)
    d.save_annotations('Datasets/GameDatasets/user123_league of legends_2024-01-15/user123_league of legends_2024-01-15_22-59.json')
