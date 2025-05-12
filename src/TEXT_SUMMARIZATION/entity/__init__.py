from dataclasses import dataclass
from pathlib import Path

@dataclass(frozen = True) #frozen=True makes the object immutable, like a constant.
class DataIngestionConfig:
    root_dir:Path
    source_URL:str
    local_data_file:Path
    unzip_dir:Path

#or

"""class DataIngestionConfig:
    def __init__(self, root_dir, source_URL, local_data_file, unzip_dir):
        self.root_dir = root_dir
        self.source_URL = source_URL
        self.local_data_file = local_data_file
        self.unzip_dir = unzip_dir
"""
@dataclass(frozen = True)
class DataValidationConfig:
    root_dir:Path
    status_file:Path
    All_required_file:list


@dataclass(frozen=True)
class DataTransformationConfig:
    root_dir: Path
    data_path: Path
    tokenizer_name: Path


from dataclasses import dataclass
from pathlib import Path


@dataclass(frozen=True)
class ModelTrainerConfig:
    root_dir: Path
    data_path: Path
    model_ckpt: Path
    num_train_epochs: int
    warmup_steps: int
    per_device_train_batch_size: int
    weight_decay: float
    logging_steps: int
    eval_steps: int # added
    evaluation_strategy: str # added
    save_steps: int # changed from float to int
    gradient_accumulation_steps: int

@dataclass(frozen = True)
class ModelEvaluationConfig:
    root_dir: Path
    data_path: Path
    model_path: Path
    tokenizer_path: Path
    metric_file_name: Path