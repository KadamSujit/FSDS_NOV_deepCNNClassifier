from dataclasses import dataclass
from pathlib import Path

#instead of using namedtuple approach, we can use below approach of class variables
#advantage of this approach is here we can define datatype of each variable.
@dataclass(frozen=True)
class DataIngestionConfig:
    root_dir: Path
    source_URL: str
    local_data_file: Path
    unzip_dir: Path