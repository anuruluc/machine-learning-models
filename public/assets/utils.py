import os
import json
import logging
from typing import Any, Dict, List, Optional, Union
import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split

logger = logging.getLogger(__name__)

def load_json(filepath: str) -> Dict[str, Any]:
    """Load JSON file from the given filepath."""
    try:
        with open(filepath, 'r') as f:
            data = json.load(f)
        return data
    except Exception as e:
        logger.error(f"Error loading JSON file: {e}")
        raise

def save_json(data: Dict[str, Any], filepath: str) -> None:
    """Save data to a JSON file at the given filepath."""
    try:
        with open(filepath, 'w') as f:
            json.dump(data, f, indent=4)
    except Exception as e:
        logger.error(f"Error saving JSON file: {e}")
        raise

def split_data(
    X: Union[np.ndarray, pd.DataFrame],
    y: Union[np.ndarray, pd.Series],
    test_size: float = 0.2,
    random_state: Optional[int] = None
) -> tuple:
    """Split data into training and testing sets."""
    return train_test_split(X, y, test_size=test_size, random_state=random_state)

def create_directory(dirpath: str) -> None:
    """Create a directory if it does not exist."""
    if not os.path.exists(dirpath):
        os.makedirs(dirpath)

def get_file_extension(filepath: str) -> str:
    """Return the file extension from the given filepath."""
    return os.path.splitext(filepath)[1].lower()

def validate_file_extension(filepath: str, valid_extensions: List[str]) -> bool:
    """Check if the file has a valid extension."""
    extension = get_file_extension(filepath)
    return extension in valid_extensions

def setup_logging(log_file: Optional[str] = None, level: int = logging.INFO) -> None:
    """Configure logging for the project."""
    logging.basicConfig(
        level=level,
        format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
        handlers=[logging.StreamHandler()]
    )
    if log_file:
        file_handler = logging.FileHandler(log_file)
        file_handler.setLevel(level)
        file_handler.setFormatter(logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s'))
        logging.getLogger().addHandler(file_handler)