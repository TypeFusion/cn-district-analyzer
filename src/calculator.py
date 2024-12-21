"""
City distance calculator implementation.
Calculates distances between city districts and city centers.
"""
from typing import List, Dict
import math
import pandas as pd
import numpy as np
from data_source import DataSource

class CityDistanceCalculator:
    # 地球半径（单位：公里）
    EARTH_RADIUS_KM = 6371.0

    def __init__(self, data_source: DataSource):
        self.data_source = data_source

    @staticmethod
    def haversine_distance(lat1: float, lon1: float, lat2: float, lon2: float) -> float:
        """
        Calculate the great circle distance between two points on the earth.

        Args:
            lat1: Latitude of point 1 in degrees
            lon1: Longitude of point 1 in degrees
            lat2: Latitude of point 2 in degrees
            lon2: Longitude of point 2 in degrees

        Returns:
            Distance between points in kilometers
        """
        # 将经纬度转换为弧度
        lat1_rad = math.radians(lat1)
        lon1_rad = math.radians(lon1)
        lat2_rad = math.radians(lat2)
        lon2_rad = math.radians(lon2)

        # 计算经纬度差值
        delta_lat = lat2_rad - lat1_rad
        delta_lon = lon2_rad - lon1_rad

        # Haversine公式
        a = math.sin(delta_lat/2)**2 + \
            math.cos(lat1_rad) * math.cos(lat2_rad) * \
            math.sin(delta_lon/2)**2

        c = 2 * math.atan2(math.sqrt(a), math.sqrt(1-a))

        # 计算距离
        distance = CityDistanceCalculator.EARTH_RADIUS_KM * c

        return round(distance, 2)  # 保留两位小数

    @staticmethod
    def calculate_city_center(districts: List[Dict]) -> Dict:
        """
        Calculate the center point of a city based on its districts.
        Uses the average of coordinates weighted by district importance.

        Args:
            districts: List of district dictionaries containing coordinates

        Returns:
            Dictionary with calculated center coordinates
        """
        if not districts:
            raise ValueError("No districts provided")

        # 使用numpy计算加权平均值
        latitudes = np.array([d['latitude'] for d in districts])
        longitudes = np.array([d['longitude'] for d in districts])

        # 目前使用简单平均，未来可以添加权重
        center_lat = np.mean(latitudes)
        center_lon = np.mean(longitudes)

        return {
            'latitude': float(center_lat),  # 转换numpy类型为Python原生类型
            'longitude': float(center_lon)
        }

    def process_all_cities(self, cities: List[str], output_file: str) -> None:
        """
        Process distance calculations for multiple cities and save to CSV.

        Args:
            cities: List of city names to process
            output_file: Path to save the output CSV file
        """
        results = []
        for city in cities:
            districts = self.data_source.get_city_districts(city)
            if not districts:
                print(f"Warning: No districts found for {city}")
                continue

            center = self.calculate_city_center(districts)
            for district in districts:
                distance = self.haversine_distance(
                    district['latitude'],
                    district['longitude'],
                    center['latitude'],
                    center['longitude']
                )
                results.append({
                    'city': city,
                    'district': district['name'],
                    'district_lat': district['latitude'],
                    'district_lon': district['longitude'],
                    'center_lat': center['latitude'],
                    'center_lon': center['longitude'],
                    'distance_km': distance
                })

        if not results:
            raise ValueError("No results to save")

        df = pd.DataFrame(results)
        df.to_csv(output_file, index=False, encoding='utf-8')
        print(f"Results saved to {output_file}")
