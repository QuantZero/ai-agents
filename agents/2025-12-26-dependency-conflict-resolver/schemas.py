# schemas.py

from pydantic import BaseModel, FilePath
from typing import List, Dict


class DependencyConflictInput(BaseModel):
    requirements_file: FilePath


class DependencyConflictOutput(BaseModel):
    conflicts: Dict[str, List[str]]  # Example: {'package_name': ['version1', 'version2']}
    resolution: Dict[str, str]  # Example: {'package_name': 'resolved_version'}
