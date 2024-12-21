"""
Unit tests for the city distance calculator.
"""
import unittest
from src.calculator import CityDistanceCalculator
from src.data_source import LocalDataSource

class TestCityDistanceCalculator(unittest.TestCase):
    def setUp(self):
        self.test_data = {
            "测试市": [
                {"name": "测试区1", "latitude": 30.0, "longitude": 120.0},
                {"name": "测试区2", "latitude": 30.1, "longitude": 120.1}
            ]
        }
        self.data_source = LocalDataSource(self.test_data)
        self.calculator = CityDistanceCalculator(self.data_source)

    def test_haversine_distance(self):
        # TODO: Add distance calculation tests
        pass
