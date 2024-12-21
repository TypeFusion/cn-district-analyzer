"""
Data source interface and implementations for city district data.
"""
from abc import ABC, abstractmethod
from typing import Dict, List

class DataSource(ABC):
    @abstractmethod
    def get_city_districts(self, city: str) -> List[Dict]:
        pass

class LocalDataSource(DataSource):
    def __init__(self, city_districts: Dict):
        self.city_districts = city_districts

    def get_city_districts(self, city: str) -> List[Dict]:
        return self.city_districts.get(city, [])
