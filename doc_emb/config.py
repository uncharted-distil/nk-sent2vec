import os
from pathlib import Path


def get_model_path():
    current_dir = os.path.dirname(os.path.abspath(__file__))
    parent_dir = Path(current_dir).parent
    return str(parent_dir / 'models' / 'torontobooks_unigrams.bin')


MODEL_PATH = os.getenv('MODEL_PATH', get_model_path())
