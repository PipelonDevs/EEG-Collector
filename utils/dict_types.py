from typing import Dict, List
from dataclasses import field
from pydantic.dataclasses import dataclass as pdataclass

@pdataclass
class DataClassInstance(dict):
    pass

@pdataclass
class Device(dict):
    device_name: str = field(default="")
    unit_name: str = field(default="")
    clock_rate: int = field(default=0)
    channels: int = field(default=0)
    displayable_rows: Dict[str, List[int]] = field(default_factory=dict)

@pdataclass
class Annotation(dict):
    start: int = field(default=0)
    end: int = field(default=0)
    label: str = field(default="")


@pdataclass
class Meta(dict):
    device: Device = field(default_factory=Device)
    duration: int = field(default=0)
    notes: str = field(default="")

@pdataclass
class Annotations(dict):
    meta: Meta = field(default_factory=Meta)
    data: list[Annotation] = field(default_factory=list)


if __name__ == '__main__':
    from storage import ISavingStrategy
    from storage import SaveToFile

    s: ISavingStrategy = SaveToFile()
    a = Annotations(**s.pull('shit2dw.json'))
    
