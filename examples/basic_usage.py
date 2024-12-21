"""
Basic usage example of the city distance calculator.
Shows how to calculate distances between districts and city centers.
"""
from calculator import CityDistanceCalculator
from data_source import LocalDataSource

def main():
    # 示例城市数据
    city_districts = {
        "上海市": [
            {"name": "浦东新区", "latitude": 31.2214, "longitude": 121.5447},
            {"name": "黄浦区", "latitude": 31.2317, "longitude": 121.4858},
            {"name": "徐汇区", "latitude": 31.1889, "longitude": 121.4365},
        ]
    }

    # 创建数据源和计算器实例
    data_source = LocalDataSource(city_districts)
    calculator = CityDistanceCalculator(data_source)

    # 计算指定城市的区域距离
    cities = ["上海市"]
    calculator.process_all_cities(cities, "shanghai_distances.csv")

if __name__ == "__main__":
    main()
